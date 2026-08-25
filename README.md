# 昭群科技 JiaoKuan Technology — 已停用 / Retired

> **本站已遷移。正式站台為 <https://www.jktek.com.tw>。**
>
> **This site has moved. The live site is <https://www.jktek.com.tw>.**

本專案曾透過 GitHub Pages 發佈公司官網。網站已遷至自有網域，內容不再於此維護，
所有內頁 HTML 均已移除，僅保留 `index.html` 作為指向新網域的入口。

This repository used to publish the company website via GitHub Pages. The site
has moved to its own domain and is no longer maintained here. Every content page
has been removed; only `index.html` remains, pointing at the new domain.

請不要在此新增或修改內容 —— 任何變更都應在正式站台的來源庫進行。
Do not add or edit content here. Changes belong in the live site's repository.

## 現況 / What is left

| 路徑 Path | 說明 Description |
|---|---|
| `index.html` | 指向 <https://www.jktek.com.tw> 的入口頁，含 `rel=canonical` / Landing page carrying a `rel=canonical` to the new domain |
| `capy.jpg` | `index.html` 使用的標誌 / logo used by `index.html` |
| `.nojekyll` | 保留，使 GitHub Pages 原樣提供檔案 / kept so GitHub Pages serves files as-is |

其餘檔案（圖片、PDF、`.md` 原稿、`program.wasm` 等）仍在版本庫中，僅內頁 HTML 被移除。
完整歷史仍在 Git 中，若需取回任何一頁：

Other files (images, PDFs, `.md` sources, `program.wasm`) are still tracked; only
the content HTML was removed. The full history is still in Git, so any page can
be recovered:

```bash
# 列出移除該批檔案的提交 / find the commit that removed them
git log --diff-filter=D --name-only -- '*.html'

# 取回單一檔案 / restore one file
git checkout <commit>^ -- aboutus.html
```

## 已知後果 / Known consequences

移除內頁後，這些網址會回傳 404：`/aboutus.html`、`/projects.html`、`/patents.html`、
`/misc_ideas.html`、`/textbook/...`、`/misc/...`、`/dcd/...`、`/medicine/...`。
保留的 `index.html` 其導覽列仍連向其中四頁，因此那些連結目前是斷的。

These URLs now return 404: `/aboutus.html`, `/projects.html`, `/patents.html`,
`/misc_ideas.html`, and everything under `/textbook/`, `/misc/`, `/dcd/` and
`/medicine/`. The surviving `index.html` still has nav links to four of them, so
those links are currently broken.

搜尋引擎會在數週內將這些網址移出索引。舊網址並未轉址至新網域，因此原有的搜尋排名
不會轉移過去 —— 這是移除（而非設定轉址）的預期結果。

Search engines will drop these URLs over the following weeks. The old URLs are
not redirected to the new domain, so any accumulated search ranking is not
carried across. That is the expected outcome of removing them rather than
redirecting.

## Remotes

| Remote | URL | 用途 Purpose |
|---|---|---|
| `origin` | `git@github.com:jktekComTw/jktekComTw.github.io.git` | 本停用庫 / this retired repository |

正式站台改由自有主機提供，不再由推送至 `origin` 部署。
The live site is served from its own host; pushing here no longer deploys it.

## 授權 / License

© 昭群科技 JiaoKuan Technology. All rights reserved.
