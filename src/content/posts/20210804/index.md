---
title: "VSCode Dev Container 測試"
date: 2021-08-04T14:57:45Z
tags:
  - "vscode"
---

今天在測試 `.net core` 使用 `vscode debug` 的時候
發現了在遠端部分多出了 `DevVolumes` !
但是我一開始也不知道這是什麼，就點了 `Clone Repostry in Container Volume`
後面就挑出 `Clone a repository from GitHub in a Container Volume` !
沒想到這個可以直接把在 `GitHub` 上的專案直接用 `Docker` 執行起來!!!
這也太方便了吧!
如果已經有 `Dockerfile` 或 `docker-compose` 還可以直接使用，就把環境用 `Docker` 執行!
這個真的是福音啊!
終於可以不用再自己本機裝一堆東西，只要設定好 `devcontainer.json` 專案就帶著走啦!
只要有 `vscode` 哪裡都是相同的開發環境!
還有測試開啟 `golang` 跟 `.net core` 專案，也直接有 `go-cli` 跟 `dotnet-cli` 方便阿!
預設還有 `git-cli` 可以用!! 不過好像用 `vscode` 內建的就夠用了!
再來研究研究如何將 `Volume` 輸出到外部，或許這樣可以用 `fork` 來控制 `git` 項目!





