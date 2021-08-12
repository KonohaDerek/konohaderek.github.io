---
title: "20210812"
date: 2021-08-12T13:55:21Z
tags:
  - "golang"
---

這幾日試著用 `golang` 建立一個 `CleanArchitecture` 的實作。
希望能用短短的時間來複習前幾日學習 `DDD` 的成果
也因為後面工作會稍微的用到 `golang` 所以就來重拾很久沒寫的 `golang` 希望不要跟以前差太多
也為了這個目標新開了一個專案 [GolangCleanArchitecture](https://github.com/KonohaDerek/GolangCleanArchitecture)  
希望這個小專案能夠有完成的一天（笑）

這邊來說說目前遇到的小困擾吧
1. `package name` 的引用，在過去都是在同一個 `package name` 下進行開發 ， 這次特別拆分了 `package name` 導致在引用的過程出現了很醜的程式碼，這部分要再來找找解決方案了

1. `interface` 的使用，在 `Repository` 的部份想用介面做隔離，降低相依性，但是沒辦法把 `struct` 拆出去，只能跟 `interface` 在同一層裡面，這樣就沒辦法把實作的地方轉到 `Infrastructure` 去，畢竟存取資料庫算是外部引用的層級，能夠搬出去使用 `DI` 的方式我覺得才是最好的，這個也是要在想辦法處理的！

以上就是目前覺得比較麻煩的困擾，而且目前也還沒做到 `DomainEvent` 的觸發，這部分也是要來好好思考怎麼處理跟同步狀態。
明天再繼續努力吧！加油

* 目前寫下來還是覺得 `C#` 輕鬆許多，大概也是因為寫得久跟有完整的`CQRS` 和 `DI` 處理 ，不像 `golang` 這邊有想法卻不知道怎麼實作
