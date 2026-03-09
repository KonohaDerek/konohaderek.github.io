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
8. >> hugo server --port=13133 -D --watch

## AI 技術筆記流程
1. 用 [prompt/blog_prompt.txt](/workspaces/konohaderek.github.io/prompt/blog_prompt.txt) 把 ChatGPT 問題處理結果整理成 JSON。
2. 把整理好的 JSON 放進 [conversations/ghcr-error.json](/workspaces/konohaderek.github.io/conversations/ghcr-error.json) 同層目錄。
3. push 到 master 後，[.github/workflows/ai-blog.yml](/workspaces/konohaderek.github.io/.github/workflows/ai-blog.yml) 會執行 [scripts/generate_post.py](/workspaces/konohaderek.github.io/scripts/generate_post.py)。
4. 文章會自動生成到 src/content/posts/YYYY/MM/slug/index.md。
