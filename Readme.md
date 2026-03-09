# Hugo 

## 選擇Hugo原因
1. 以golang開發，效能好速度快
2. 不需要有太多的node_module
3. 可以使用 dokcer-compose 處理

## 如何開始
1. clone repo 後先初始化 submodule
2. 執行 docker-compose up -d
3. docker-compose exec hugo bash
4. 執行 hugo server --source=src --port=13133 -D --watch

```bash
git clone --recurse-submodules https://github.com/KonohaDerek/konohaderek.github.io.git
cd konohaderek.github.io

# 如果不是用 --recurse-submodules clone，第一次要補這一步
git submodule update --init --recursive

docker-compose up -d
docker-compose exec hugo bash
hugo server --source=src --port=13133 -D --watch
```

目前主題來自 [src/themes/beautifulhugo](src/themes/beautifulhugo)，對應設定在 [src/config.toml](src/config.toml)。

## AI 技術筆記流程
1. 用 [prompt/blog_prompt.txt](/workspaces/konohaderek.github.io/prompt/blog_prompt.txt) 把 ChatGPT 問題處理結果整理成 JSON。
2. 把整理好的 JSON 放進 [conversations/ghcr-error.json](/workspaces/konohaderek.github.io/conversations/ghcr-error.json) 同層目錄。
3. push 到 master 後，[.github/workflows/ai-blog.yml](/workspaces/konohaderek.github.io/.github/workflows/ai-blog.yml) 會執行 [scripts/generate_post.py](/workspaces/konohaderek.github.io/scripts/generate_post.py)。
4. 文章會自動生成到 src/content/posts/YYYY/MM/slug/index.md。

### 本地驗證

如果要在 push 前先本地生成文章與驗證站台：

```bash
python scripts/generate_post.py --input-dir conversations --output-dir src/content/posts
hugo --minify --config=config.toml --source=src
```
