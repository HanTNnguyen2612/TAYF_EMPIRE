# Khởi động dự án tayf
## Cài đặt Node runtime, python runtime => latest
1. Cài node: [Node](https://nodejs.org/en)
2. Cài Playwright MCP: 
```bash:
npm install -g @playwright/mcp (có thể sai, mn check bằng AI nhé), cc: HanTN38
```
3. Config để IDE nhận Playwright MCP:
a. Mở VS Code -> Ctrl + Shift + P
b. Tìm "MCP: User configuration"
c. Paste cái này vào:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    },
    "my-mcp-playwright": {
			"command": "đường dẫn vào thư mục dự án\\.venv\\Scripts\\python.exe",
			"args":[
				"mcp_server.py"
			],
			"type":"stdio"
	}
  }
}
```
4. Cài playwright
a. Clone project này về.
```bash
git clone 
```
b. Tạo virtual environment
```bash
py -m venv .venv
```
c. Kích hoạt venv
```bash
.venv\Scripts\activate
```
d. Cài dependencies, này mới là base, ai cài gì thêm thì update file requirements.txt nhé
```bash
pip install -r requirements.txt
```
e. Cài browser để chạy playwright
```bash
playwright install
```