# Hugo 

## 選擇Hugo原因
1. 以golang開發，效能好速度快
2. 不需要有太多的node_module
3. 可以使用 dokcer-compose 處理

## 如何開始
1. 執行 docker-compose up -d
2. docker-compose exec hugo bash
3. >> hugo new site blog
4. >> cd blog/ && git init
5. git submodule add https://github.com/vaga/hugo-theme-m10c.git src/themes/m10c
6. >> echo theme = \"m10c\" >> config.toml
7. >> hugo new posts/my-first-post.md
8. >> hugo --port=13133 -D --watch
