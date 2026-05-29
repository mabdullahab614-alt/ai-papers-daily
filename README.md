![header](https://capsule-render.vercel.app/api?type=waving&color=0:0a0e27,30:00d9ff,65:9d4edd,100:ff006e&height=230&section=header&text=%F0%9F%93%84%20AI%20Papers%20Daily&fontSize=55&fontColor=ffffff&fontAlignY=42&desc=Real%20ArXiv%20papers%20auto-fetched%20%26%20committed%20every%20day&descAlignY=63&descSize=18&animation=fadeIn)

<div align="center">

[![Daily Papers](https://github.com/mabdullahab614-alt/ai-papers-daily/actions/workflows/daily-papers.yml/badge.svg)](https://github.com/mabdullahab614-alt/ai-papers-daily/actions/workflows/daily-papers.yml)
&nbsp;
![Papers/Day](https://img.shields.io/badge/PAPERS%2FDAY-2%20%F0%9F%93%84-00d9ff?style=flat-square&labelColor=0a1e27)
&nbsp;
![Source](https://img.shields.io/badge/SOURCE-ArXiv%20API-ff006e?style=flat-square&labelColor=2e0a1a)
&nbsp;
![Categories](https://img.shields.io/badge/CATEGORIES-cs.AI%20%7C%20cs.LG%20%7C%20cs.CV%20%7C%20cs.CL-9d4edd?style=flat-square&labelColor=150a2e)
&nbsp;
![Status](https://img.shields.io/badge/STATUS-LIVE%20%F0%9F%9F%A2-00ff88?style=flat-square&labelColor=0a2e1a)

<br/>

[![VISIT PORTFOLIO](https://img.shields.io/badge/%F0%9F%8C%90%20%E2%96%BA%20VISIT%20PORTFOLIO-00d9ff?style=for-the-badge&labelColor=0a0e27)](https://portfolio-website-jet-iota-21.vercel.app)
&nbsp;
[![HUGGING FACE](https://img.shields.io/badge/%F0%9F%A4%97%20%E2%96%BA%20HUGGING%20FACE-ffcc00?style=for-the-badge&labelColor=1a1040)](https://huggingface.co/Abdullah-Javid)
&nbsp;
[![ARXIV](https://img.shields.io/badge/%F0%9F%93%84%20%E2%96%BA%20BROWSE%20ARXIV-ff006e?style=for-the-badge&labelColor=2e0a1a)](https://arxiv.org/list/cs.AI/recent)

</div>

---

## 📄 What Gets Committed

Every commit fetches a **real paper from ArXiv** — the world's largest AI research repository. No fake content, no filler. Actual research that matters.

```
📄 2026-05-31 10:00 PKT — Attention Is All You Need: Transformers for NLP
📄 2026-05-31 18:00 PKT — YOLOv9: Learning What You Want to Learn Using GELAN
```

---

## 🏷️ Paper Categories

<div align="center">

| Category | Full Name | Topics |
|:--------:|:----------|:-------|
| `cs.AI` | Artificial Intelligence | Agents, reasoning, planning |
| `cs.LG` | Machine Learning | Deep learning, optimization, theory |
| `cs.CV` | Computer Vision | Object detection, segmentation, GANs |
| `cs.CL` | Computation & Language | NLP, LLMs, transformers, BERT, GPT |

</div>

---

## ⚙️ How It Works

GitHub Actions fires **2 times daily**, fetches a random paper from ArXiv's free public API, and commits a formatted summary:

<div align="center">

| Run | Time (PKT) | UTC | Cron |
|:---:|:----------:|:---:|:----:|
| 🌅 Morning | **10:00 AM** | 05:00 | `0 5 * * *` |
| 🌆 Evening | **6:00 PM** | 13:00 | `0 13 * * *` |

</div>

Each run:
1. 🔍 Fetches **15 recent papers** from ArXiv's public API
2. 🎲 Picks one **randomly** from cs.AI · cs.LG · cs.CV · cs.CL
3. 📝 Appends a formatted summary to the **monthly log** in `/papers/`
4. 🔢 Increments the **paper counter** in `counter.txt`
5. ✅ Commits with the **paper title** as the commit message

---

## 📁 Repository Structure

```
ai-papers-daily/
├── .github/
│   └── workflows/
│       └── daily-papers.yml    # ⚙️ Workflow — runs 2× daily
├── scripts/
│   └── fetch_paper.py          # 🐍 ArXiv fetcher & log writer
├── papers/
│   ├── 2026-05.md              # 📄 Monthly paper logs (auto-generated)
│   └── 2026-06.md
├── counter.txt                 # 🔢 Total papers fetched
└── README.md
```

---

## 🚀 About Abdullah Javid

**AI Developer & ML Engineer** · Lahore, Pakistan

- 🧠 **11+ live AI projects** — Brain Tumor Detector (92.2%), YOLOv8 Animal Detector, Nexus AI
- 🤖 Deep learning · Computer vision · Multi-model chatbots
- 🌐 **20+ global platforms** · Claude API · GPT-4 · Gemini
- 🎓 BS Artificial Intelligence @ UMT Lahore

<div align="center">

[![Email](https://img.shields.io/badge/Email-mabdullah.ab614%40gmail.com-ff006e?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0a0e27)](mailto:mabdullah.ab614@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdullah%20Javid-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0a0e27)](https://linkedin.com/in/abdullah-javid-b217a2384)
[![GitHub](https://img.shields.io/badge/GitHub-mabdullahab614--alt-white?style=for-the-badge&logo=github&logoColor=black&labelColor=0a0e27)](https://github.com/mabdullahab614-alt)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live%20Site-00d9ff?style=for-the-badge&labelColor=0a0e27)](https://portfolio-website-jet-iota-21.vercel.app)

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=mabdullahab614-alt&style=for-the-badge&color=00d9ff&labelColor=0a0e27&label=PROFILE+VIEWS)

</div>

---

![footer](https://capsule-render.vercel.app/api?type=waving&color=0:ff006e,40:9d4edd,80:00d9ff,100:0a0e27&height=130&section=footer&animation=fadeIn)

<div align="center">

**Auto-updated 2× daily via ArXiv API · © 2026 Abdullah Javid · AI Developer · Lahore, Pakistan**

</div>
