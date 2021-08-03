---
title: "Ｄocker dotnet-symbol 安裝方式"
date: 2021-08-03T08:31:59Z
tags:
  - "生活記事"
---


## 緣由
今日前同事在line上面問我說要如何安裝 `dotnet-symbol` ？
因為他在安裝上出現下面錯誤

```
Could not execute because the application was not found or a compatible .NET SDK is not installed.
Possible reasons for this include:
  * You intended to execute a .NET program:
      The application 'tool' does not exist.
  * You intended to execute a .NET SDK command:
      It was not possible to find any installed .NET SDKs.
      Install a .NET SDK from:
        https://aka.ms/dotnet-download
```
看了一下，他的環境是我之前用的 `Docker` ，裡面用的 `base image` 是 `mcr.microsoft.com/dotnet/aspnet:5.0`

這個 `image` 裡面只會有 `runtime` 難怪他不能安裝，那麼就來實驗看看怎麼安裝吧！

## 安裝方式

其實也很簡單，因為該 `image` 為 `ubuntu base`，那麼我們就直接來用 `apt-get` 安裝吧

1. 安裝
  ``` bash
  wget https://packages.microsoft.com/config/ubuntu/21.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
  dpkg --purge packages-microsoft-prod && dpkg -i packages-microsoft-prod.deb
  apt-get update
  apt-get install -y dotnet-sdk-5.0
  dotnet tool install -g dotnet-symbol
  ```

安裝後就可以使用拉～
