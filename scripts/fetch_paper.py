"""
Fetches a random AI/ML paper from ArXiv and logs it to the monthly papers file.
Categories: cs.AI, cs.LG (Machine Learning), cs.CV (Computer Vision), cs.CL (NLP)
"""

import urllib.request
import xml.etree.ElementTree as ET
import random
import os
import sys
from datetime import datetime, timezone, timedelta

PKT = timezone(timedelta(hours=5))
now = datetime.now(PKT)
DATE = now.strftime('%Y-%m-%d')
TIME = now.strftime('%H:%M')
MONTH = now.strftime('%Y-%m')

CATEGORIES = [
    'cs.AI',   # Artificial Intelligence
    'cs.LG',   # Machine Learning
    'cs.CV',   # Computer Vision
    'cs.CL',   # Computation and Language (NLP)
]

QUERY = '+OR+'.join([f'cat:{c}' for c in CATEGORIES])
START = random.randint(0, 150)

BASE_URLS = [
    'https://export.arxiv.org/api/query',
    'https://arxiv.org/api/query',
]

NS = {
    'atom':  'http://www.w3.org/2005/Atom',
    'arxiv': 'http://arxiv.org/schemas/atom',
}

# ── Fetch with retry across mirror URLs ────────────────────────────────────
xml_data = None
for base in BASE_URLS:
    url = (
        f'{base}?search_query={QUERY}'
        f'&sortBy=lastUpdatedDate&sortOrder=descending'
        f'&max_results=15&start={START}'
    )
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'ai-papers-daily/1.0'})
            with urllib.request.urlopen(req, timeout=45) as r:
                xml_data = r.read()
            break
        except Exception as e:
            print(f'[WARN] Attempt {attempt+1} failed ({base}): {e}', file=sys.stderr)
            import time; time.sleep(3)
    if xml_data:
        break

if not xml_data:
    print(f'[ERROR] All ArXiv endpoints failed', file=sys.stderr)
    title = 'ArXiv API temporarily unavailable — will retry next run'
    authors_str = 'N/A'
    category = 'cs.AI'
    paper_link = 'https://arxiv.org/list/cs.AI/recent'
    abstract = 'The ArXiv API was unreachable. The next scheduled run will fetch a real paper.'
    entries = []
else:
    root = ET.fromstring(xml_data)
    entries = root.findall('atom:entry', NS)

# ── Parse ──────────────────────────────────────────────────────────────────
if entries:
    entry = random.choice(entries)

    title_elem = entry.find('atom:title', NS)
    title = (title_elem.text or '').strip().replace('\n', ' ') if title_elem is not None else 'Unknown'

    summary_elem = entry.find('atom:summary', NS)
    abstract = (summary_elem.text or '').strip().replace('\n', ' ')[:280] if summary_elem is not None else ''

    link_elem = entry.find('atom:id', NS)
    raw_link = (link_elem.text or '').strip() if link_elem is not None else ''
    arxiv_id = raw_link.split('/')[-1]
    paper_link = f'https://arxiv.org/abs/{arxiv_id}'

    author_elems = entry.findall('atom:author', NS)
    authors = [
        (a.find('atom:name', NS).text or '').strip()
        for a in author_elems
        if a.find('atom:name', NS) is not None
    ]
    authors_str = ', '.join(authors[:3])
    if len(authors) > 3:
        authors_str += ' et al.'

    cat_elem = entry.find('arxiv:primary_category', NS)
    category = cat_elem.get('term', 'cs.AI') if cat_elem is not None else 'cs.AI'

# ── Write log ──────────────────────────────────────────────────────────────
os.makedirs('papers', exist_ok=True)
log_file = f'papers/{MONTH}.md'

if not os.path.exists(log_file):
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f'# 📄 AI Papers — {MONTH}\n\n')
        f.write('Auto-fetched daily from ArXiv · Categories: cs.AI · cs.LG · cs.CV · cs.CL\n\n')
        f.write('---\n\n')

with open(log_file, 'a', encoding='utf-8') as f:
    f.write(f'\n## {title}\n\n')
    f.write(f'| | |\n|--|--|\n')
    f.write(f'| 📅 **Date** | {DATE} {TIME} PKT |\n')
    f.write(f'| 👤 **Authors** | {authors_str} |\n')
    f.write(f'| 🏷️ **Category** | `{category}` |\n')
    f.write(f'| 🔗 **Link** | [{paper_link}]({paper_link}) |\n\n')
    f.write(f'> {abstract}...\n\n')
    f.write('---\n')

# ── Update counter ─────────────────────────────────────────────────────────
count_file = 'counter.txt'
count = 0
if os.path.exists(count_file):
    try:
        count = int(open(count_file).read().strip())
    except ValueError:
        count = 0
with open(count_file, 'w') as f:
    f.write(str(count + 1))

# ── Write commit message ───────────────────────────────────────────────────
commit_msg = f'📄 {DATE} {TIME} PKT — {title[:72]}'
with open('.commit_msg', 'w', encoding='utf-8') as f:
    f.write(commit_msg)

print(f'✅ Paper fetched: {title[:60]}')
print(f'   Category: {category}')
print(f'   Authors:  {authors_str[:60]}')
print(f'   Link:     {paper_link}')
