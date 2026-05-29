"""
Fetches a random AI/ML paper — tries ArXiv API first, falls back to curated list.
"""

import urllib.request
import xml.etree.ElementTree as ET
import random
import os
import sys
import json
import time
from datetime import datetime, timezone, timedelta

PKT = timezone(timedelta(hours=5))
now = datetime.now(PKT)
DATE  = now.strftime('%Y-%m-%d')
TIME  = now.strftime('%H:%M')
MONTH = now.strftime('%Y-%m')

CATEGORIES = ['cs.AI', 'cs.LG', 'cs.CV', 'cs.CL']
NS = {
    'atom':  'http://www.w3.org/2005/Atom',
    'arxiv': 'http://arxiv.org/schemas/atom',
}

# ── Try ArXiv API ──────────────────────────────────────────────────────────
def try_arxiv():
    query = '+OR+'.join([f'cat:{c}' for c in CATEGORIES])
    start = random.randint(0, 200)
    mirrors = [
        'https://export.arxiv.org/api/query',
        'https://arxiv.org/api/query',
    ]
    for base in mirrors:
        url = (f'{base}?search_query={query}'
               f'&sortBy=lastUpdatedDate&sortOrder=descending'
               f'&max_results=20&start={start}')
        for attempt in range(2):
            try:
                req = urllib.request.Request(
                    url, headers={'User-Agent': 'ai-papers-daily/1.0'})
                with urllib.request.urlopen(req, timeout=40) as r:
                    xml_data = r.read()
                root = ET.fromstring(xml_data)
                entries = root.findall('atom:entry', NS)
                if not entries:
                    continue
                entry = random.choice(entries)

                title = (entry.find('atom:title', NS).text or '').strip().replace('\n', ' ')
                abstract = (entry.find('atom:summary', NS).text or '').strip().replace('\n', ' ')[:280]
                link_text = (entry.find('atom:id', NS).text or '').strip()
                arxiv_id = link_text.split('/')[-1]
                paper_link = f'https://arxiv.org/abs/{arxiv_id}'
                authors = [(a.find('atom:name', NS).text or '').strip()
                           for a in entry.findall('atom:author', NS)
                           if a.find('atom:name', NS) is not None]
                authors_str = ', '.join(authors[:3]) + (' et al.' if len(authors) > 3 else '')
                cat_elem = entry.find('arxiv:primary_category', NS)
                category = cat_elem.get('term', 'cs.AI') if cat_elem is not None else 'cs.AI'

                return title, authors_str, category, paper_link, abstract
            except Exception as e:
                print(f'[WARN] {base} attempt {attempt+1}: {e}', file=sys.stderr)
                time.sleep(2)
    return None

# ── Curated fallback list ──────────────────────────────────────────────────
def from_curated():
    curated_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'papers.json')
    with open(curated_path, 'r', encoding='utf-8') as f:
        papers = json.load(f)
    paper = random.choice(papers)
    return (
        paper['title'],
        paper['authors'],
        paper['category'],
        paper['link'],
        paper['abstract'],
    )

# ── Main ───────────────────────────────────────────────────────────────────
result = try_arxiv()
source = 'ArXiv API'
if result is None:
    print('[INFO] ArXiv unavailable — using curated paper list', file=sys.stderr)
    result = from_curated()
    source = 'Curated'

title, authors_str, category, paper_link, abstract = result

# ── Write log ──────────────────────────────────────────────────────────────
os.makedirs('papers', exist_ok=True)
log_file = f'papers/{MONTH}.md'

if not os.path.exists(log_file):
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f'# 📄 AI Papers — {MONTH}\n\n')
        f.write('Auto-fetched daily · Categories: cs.AI · cs.LG · cs.CV · cs.CL\n\n---\n\n')

with open(log_file, 'a', encoding='utf-8') as f:
    f.write(f'\n## {title}\n\n')
    f.write(f'| | |\n|--|--|\n')
    f.write(f'| 📅 **Date** | {DATE} {TIME} PKT |\n')
    f.write(f'| 👤 **Authors** | {authors_str} |\n')
    f.write(f'| 🏷️ **Category** | `{category}` |\n')
    f.write(f'| 📡 **Source** | {source} |\n')
    f.write(f'| 🔗 **Link** | [{paper_link}]({paper_link}) |\n\n')
    f.write(f'> {abstract}...\n\n---\n')

# ── Counter ────────────────────────────────────────────────────────────────
count_file = 'counter.txt'
count = 0
if os.path.exists(count_file):
    try:
        count = int(open(count_file).read().strip())
    except ValueError:
        pass
with open(count_file, 'w') as f:
    f.write(str(count + 1))

# ── Commit message ─────────────────────────────────────────────────────────
commit_msg = f'📄 {DATE} {TIME} PKT — {title[:72]}'
with open('.commit_msg', 'w', encoding='utf-8') as f:
    f.write(commit_msg)

print(f'✅ [{source}] {title[:65]}')
print(f'   {authors_str[:60]}  |  {category}')
