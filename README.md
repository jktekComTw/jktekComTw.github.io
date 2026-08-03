# 昭群科技 JiaoKuan Technology — 官方網站 / Company Website

公司官網原始碼，以純靜態 HTML 建置，透過 GitHub Pages 發佈。
Source for the company homepage — a plain static HTML site published via GitHub Pages.

**Live:** <https://jktekComTw.github.io>

昭群科技位於高雄市鳳山區，專注於 GNU/Linux 與 RTOS 嵌入式系統軟韌體開發、馬達變頻器 FOC
控制、電力電子產品設計、網頁與手機 App 開發、機構 3D 設計及 FPGA 設計。除公司介紹與專案
實績外，本站另收錄技術筆記、除錯報告與課程學習指南。

JiaoKuan Technology is a Kaohsiung-based embedded systems and software/firmware team.
Alongside company and project pages, this site hosts technical notes, debugging
write-ups, and course study guides.

## 網站結構 / Layout

| 路徑 Path | 說明 Description |
|---|---|
| `index.html` | 首頁 — 服務項目與技術領域 / Homepage |
| `aboutus.html` | 公司簡介 / About the company |
| `projects.html` | 專案實績 / Project portfolio |
| `misc_ideas.html` | 技術筆記與學習指南索引 / Index of notes & study guides |
| `misc/` | 技術筆記：SIL/dSIL 設計、device-tree IOMMU Q&A、SMMU RBF 載入失敗、VCU118 電源診斷、URSI GASS 2026 |
| `textbook/` | 課程學習指南 / Study guides — `radio_circuit`、`magnetelectronics`、`Signal&system`、`dcd` |
| `dcd/` | 數位電路設計與 Verilog 學習指南 / Digital circuit design & Verilog study guide |
| `medicine/` | 藥物穩態劑量計算 / Steady-state dosing calculator |
| `hsmc_pin_map.html` | Terasic DE25 FPGA HSMC ↔ ADA 腳位對照表 / Pin map |
| `webasm.html`, `program.wasm` | WebAssembly Fibonacci 示範 / demo |
| `webgl_test.html`, `webgl-cube.js` | WebGL 3D 立方體示範 / demo |

## 開發 / Development

無建置流程、無相依套件 — 直接編輯 HTML 並以瀏覽器開啟即可。
No build step and no dependencies. Edit the HTML and open it in a browser.

```bash
# 本機預覽 / Serve locally (any static server works)
python -m http.server 8000    # → http://localhost:8000
```

`.nojekyll` 存在，GitHub Pages 會原樣提供檔案，不經 Jekyll 處理 —
底線開頭的目錄與檔案因此不會被忽略。
`.nojekyll` makes GitHub Pages serve files as-is, bypassing Jekyll, so paths
beginning with an underscore are not skipped.

## Git LFS

PDF 以 Git LFS 追蹤（見 `.gitattributes`：`*.pdf filter=lfs diff=lfs merge=lfs -text`）。
複製本專案前請先安裝 git-lfs，否則取得的 PDF 只會是指標檔。

PDFs are tracked with Git LFS. Install git-lfs before cloning, or you will get
pointer files instead of the real PDFs.

```bash
git lfs install
git clone <repo-url>
git lfs pull        # 既有複本 / for an existing clone
```

Windows/MSYS2 note: `git-lfs` ships with Git for Windows but is not on the MSYS2
`PATH`. **Append** it — prepending shadows `/usr/bin/git` and breaks repos on
network shares:

```bash
export PATH="$PATH:/c/Program Files/Git/mingw64/bin"
```

## Remotes

| Remote | URL | 用途 Purpose |
|---|---|---|
| `origin` | `git@github.com:jktekComTw/jktekComTw.github.io.git` | 正式站台來源 / publishes the live site |
| `gitea` | `git@gitea.rflab.lan:chma/company.git` | 內網私有鏡像 / private LAN mirror |

推送到 `origin` 即部署；`gitea` 僅作為內部備份。
Pushing to `origin` deploys the site. `gitea` is an internal backup only.

內網鏡像的反向代理限制請求本體約 1 MB，超過的 LFS 物件會回傳 HTTP 413；
需直接上傳至 `:3000` 埠繞過代理。
The LAN mirror sits behind a reverse proxy that caps request bodies at ~1 MB, so
LFS objects above that fail with HTTP 413 and must be uploaded directly to port
`:3000`, bypassing the proxy.

## 授權 / License

© 昭群科技 JiaoKuan Technology. All rights reserved.
本網站內容與程式碼未經授權不得轉載或再散布。
Site content and code may not be redistributed without permission.
