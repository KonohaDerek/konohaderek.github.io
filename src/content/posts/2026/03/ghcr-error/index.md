---
title: "修正 GHCR manifest unknown 拉取失敗"
date: 2026-03-09T00:00:00Z
slug: "ghcr-error"
subtitle: "記錄部署容器時遇到 ghcr.io 映像拉取失敗，最後確認是映像名稱大小寫與 tag 不一致造成的錯誤。"
tags:
  - "技術筆記"
  - "Docker"
  - "GitHub"
  - "GHCR"
  - "Troubleshooting"
  - "Linux"
source: "conversations/ghcr-error.json"
draft: false
---

## 背景

在伺服器上使用 docker compose 部署來自 GitHub Container Registry 的映像時，服務無法正常拉起，需要快速確認是權限、tag，還是 registry 名稱造成的問題。

## 問題

執行 docker compose up -d 後出現 manifest unknown，代表 registry 找不到指定的映像或 tag。

## 調查過程

1. 先確認 ghcr.io 的 repository 名稱與 owner 大小寫是否一致。
2. 檢查 GitHub Personal Access Token 是否具備 read:packages 權限。
3. 使用 docker pull 手動驗證映像完整路徑與 tag 是否存在。
4. 重新比對 CI 發布出的 tag 與部署檔案中的 tag 是否相同。

## 解決方案

確認映像名稱需與 GHCR 實際發布名稱一致，並改用存在的 tag 重新拉取後即可正常部署。

```bash
docker pull ghcr.io/konohaderek/bitfinex-strategy-bot:426aa46
docker compose up -d
```

## 經驗總結

- GHCR 的映像名稱與 owner 命名需要精準一致。
- 部署前可以先用 docker pull 驗證映像是否存在。
- 把部署用 tag 與 CI 輸出綁在一起，可以降低人工填錯機率。

## 參考資料

- [GitHub Container Registry 文件](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
