---
title: "20210809"
date: 2021-08-09T09:46:35Z
tags:
  - "生活記事"
---

這幾天去參加了 `Teddy` 的 `領域驅動設計與簡潔架構入門實作班`

雖然只有 8/5~8/8 短短的三天，但我覺得真的是收穫滿滿

一開始 `Teddy` 會由 `Event Storming` 慢慢帶入 `DDD`，之後才會提到 `CQRS` & `Clean Architecture`

`Teddy` 上課方式真的很生動又有趣，`Teddy` 會不斷地舉生活中的案例讓學員們更好地瞭解

後面讓大家在做 `Event Storming` 時也是慢慢地給大家觀念之後才讓大家一步一步的實作

進入 `DDD` 後也是用實例＋ `EzKanban` 讓大家了解各種戰術設計及拆分理由

後面也就自然地帶入了 `CQRS` + `Clean Architecture`

原本之前在實作的時候都會先用 `Clean Architecture` 拆分再去歸類 `CQRS` 項目，但其實應該是反過來

由 `Event Storming` 得知有哪些 `Command` 跟 `Domain Event` 再去套用 `CQRS` 整個就明確了許多

後面再把 `Clean Architecture` 分層加入，就整個串連了起來。

以前在看 `jasontaylordev/CleanArchitecture` 這個專案，總是用 `API` 去套用，現在終於了解以前不明白的地方了

上完 `Teddy` 的課後再重新看這專案，很簡單就明白了為何是這樣分層，也更清楚了 `DomainEventHandler` 處理的理由和 `MediatR IPipelineBehavior` 作用

真的很慶幸自己決定花這個錢去上課，雖然不知道未來的團隊夥伴是否有用 `DDD` ， 但我相信我自己的專案可以用這個方式來重新處理過。

加油！希望未來寫的程式能夠不需要說明文件或交接文件只要看資料結構就像閱讀文章一樣！

這次也很謝謝同組的夥伴們！雖然中間我們對一些事物的定義及看法不一樣，但我覺得這是件很好的事情，透過不一樣的想法跟激盪，也讓我學到了許多。
當然課後我們也開了 `Line` 群組，希望大家在未來也能夠一起討論架構，一起努力前進！


