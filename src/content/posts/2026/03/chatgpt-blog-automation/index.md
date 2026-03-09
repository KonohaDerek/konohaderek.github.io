---
title: "打造 ChatGPT 對話自動整理與技術筆記發布流程"
date: 2026-03-09T00:00:00Z
slug: "chatgpt-blog-automation"
subtitle: "將 ChatGPT troubleshooting 對話自動整理成技術文章，並在遮罩機敏資料後自動提交到 GitHub Pages repo。 "
tags:
  - "技術筆記"
  - "ChatGPT"
  - "GitHub Actions"
  - "Automation"
  - "DevOps"
  - "Troubleshooting"
source: "conversations/chatgpt-blog-automation.json"
draft: false
---

## 背景

原始內容描述了一套適合技術筆記型 blog 的自動化流程，目標是把 ChatGPT 上的問題處理過程，在解決後整理成可發布的文章，並自動送進 GitHub repo，形成長期可累積的 troubleshooting archive 或 DevOps knowledge base。文件中以 GitHub Pages repo、n8n、GitHub Actions、OpenAI、Markdown 與 PDF 匯出等方式，逐步構成完整方案。

## 問題

手動整理 ChatGPT 對話、移除雜訊、遮罩 token/password/IP/email/domain 等敏感資訊，再轉成可發佈的 Markdown 或 blog 文章，流程繁瑣且不易長期維護；若想穩定累積技術知識庫，需要一套可自動化、可重複執行、可直接整合到 repo 的處理流程。

## 調查過程

1. 先定義整體流程：ChatGPT conversation 匯出後，進入自動化管線，依序進行內容整理、敏感資料遮罩、文章生成、Markdown 輸出與 GitHub commit。
2. 比較兩種實作方向：一種是 n8n workflow，透過 Webhook、遮罩節點、OpenAI 節點與 GitHub API 完成；另一種是 repo 內建 scripts 搭配 GitHub Actions，自動監聽 conversations 目錄中的檔案變化。
3. 整理文章結構需求，固定輸出 title、background、problem、investigation、solution、lessons learned，並要求移除無關對話噪音、保留技術細節與必要 code block。
4. 設計敏感資料遮罩規則，使用 regex 處理 Bearer ********、GitHub token、password、私有 IP、AWS key、email 與私有網域，避免機敏資訊進入文章或 commit 歷史。
5. 規劃 repo 結構，例如 conversations、posts、scripts、prompt、.github/workflows，讓輸入資料、處理邏輯與輸出文章可分層管理。
6. 加入延伸能力，例如 slugify、自動 tags、frontmatter、Mermaid diagram、SEO title、PDF archive，讓系統從單次整理升級為可長期維運的知識庫。

## 解決方案

建立一套以 GitHub repo 為核心的自動文章生成系統：

text
ChatGPT conversation
 -> sanitize / mask sensitive data
 -> AI summarize and structure article
 -> generate Markdown post
 -> git add / commit / push
 -> GitHub Pages publish


建議 repo 結構：

text
.
├── conversations
│ └── ghcr-error.json
├── posts
│ └── 2026
│ └── 03
├── scripts
│ ├── generate_post.py
│ ├── mask_sensitive.py
│ ├── slugify.py
│ └── tagger.py
├── prompt
│ └── blog_prompt.txt
└── .github/workflows
 └── ai-blog.yml


敏感資料遮罩可先做成獨立模組：

python
import re

def mask(text):
 rules = [
 (r"ghp_[A-Za-z0-9]+", "ghp_********"),
 (r"Bearer\s+[A-Za-z0-9\._\-]+", "Bearer ********"),
 (r"AKIA[0-9A-Z]{16}", "AWS_KEY_********"),
 (r"\b\d{1,3}(\.\d{1,3}){3}\b", "10.x.x.x"),
 (r"password\s*=\s*\S+", "password=********),
 (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+", "user@example.com"),
 ]
 for pattern, replace in rules:
 text = re.sub(pattern, replace, text)
 return text


文章生成腳本讀取 conversations 檔案後，先遮罩內容，再把資料帶入 prompt，交給模型輸出 Markdown：

python
import os
import json
from datetime import datetime
from mask_sensitive import mask
from slugify import slug
from tagger import tags

file = os.listdir("conversations")[0]
data = json.load(open(f"conversations/{file}"))
title = data["title"]
conversation = mask(data["conversation"])
date = datetime.now().strftime("%Y-%m-%d")
slug_name = slug(title)
tag_list = tags(conversation)
output = f"posts/{datetime.now().year}/{datetime.now().month:02d}/{slug_name}.md"


GitHub Actions 則在 push conversations 檔案後自動執行：

yaml
name: AI Blog Generator
on:
 push:
 paths:
 - conversations/*.json
jobs:
 generate:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v4
 - uses: actions/setup-python@v5
 with:
 python-version: "3.11"
 - name: Install deps
 run: pip install openai
 - name: Generate post
 env:
 OPENAI_API_KEY: ********
 run: python scripts/generate_post.py
 - name: Commit post
 run: |
 git config user.name "ai-blog-bot"
 git config user.email "user@example.com"
 git add posts
 git commit -m "AI generated blog"
 git push


若要保留原始對話作備份，也可先把 conversation 轉成 Markdown，再輸出 PDF，形成 chat.md、chat.pdf 與 blog.md 三份產物。整體方案可從 MVP 的手動匯入 conversation.txt 開始，再逐步升級成 JSON 輸入、自動 tagging、Mermaid 圖表與知識庫型架構。

## 經驗總結

- 把 ChatGPT 對話變成可搜尋、可累積的技術資產，關鍵不只是生成文章，而是先定義一致的文章結構與輸出規格。
- 敏感資料遮罩必須前置處理，不能等到文章生成後才補救，否則機敏資訊可能已進入模型輸出或 git 歷史。
- MVP 可以先用 conversation.txt + shell script 啟動，但長期來看以 JSON 輸入、scripts 分層與 GitHub Actions 觸發會更穩定。
- slug、自動 tags、frontmatter 與目錄分層，會直接影響 blog 可維護性與知識庫成長品質。
- 同一份 conversation 可以同時輸出 Markdown 文章與 PDF archive，兼顧發佈需求與備份需求。

## 參考資料

- [KonohaDerek GitHub repository](https://github.com/KonohaDerek/konohaderek.github.io)
