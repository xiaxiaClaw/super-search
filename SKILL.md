---
name: super-search
description: 基于 super-fetch 的聚合搜索工具，支持多种领域的专业搜索。
user-invocable: true
dependencies:
  - super-fetch
---

# Super Search

基于 super-fetch 的全能搜索矩阵，支持通用搜索、学术研究、技术开发等多种领域。

## 快速开始

### 通用搜索（最常用）

```bash
# 激活环境
source /tmp/fetch-venv/bin/activate

# 通用网页搜索
python ~/.openclaw/skills/super-fetch/fetch.py "https://cn.bing.com/search?q=关键词" -e cffi
```

**推荐搜索引擎**：
| 引擎 | URL | 速度 |
|-----|-----|-----|
| Bing | `https://cn.bing.com/search?q={q}` | 快 |
| 360 | `https://www.so.com/s?q={q}` | 快 |
| 搜狗 | `https://sogou.com/web?query={q}` | 快 |

### 新闻搜索

```bash
# 百度新闻
python ~/.openclaw/skills/super-fetch/fetch.py "https://www.baidu.com/s?wd=关键词&tn=news" -e cffi
```

---

## 进阶使用

### 🎓 学术搜索

详细 URL 模板：

| 引擎 | 用途 | URL |
|-----|-----|-----|
| Arxiv | AI/物理论文 | `https://arxiv.org/search/?searchtype=all&query={q}` |
| PapersWithCode | 论文+代码 | `https://paperswithcode.com/search?q={q}` |
| Semantic Scholar | 语义搜索 | `https://www.semanticscholar.org/search?q={q}` |
| PubMed | 医学文献 | `https://pubmed.ncbi.nlm.nih.gov/?term={q}` |

### 💻 技术搜索

| 引擎 | 用途 | URL |
|-----|-----|-----|
| GitHub | 代码仓库 | `https://github.com/search?q={q}&type=repositories` |
| StackOverflow | 技术问答 | `https://stackoverflow.com/search?q={q}` |

### 📈 金融搜索

| 引擎 | 用途 | URL |
|-----|-----|-----|
| 雪球 | A股讨论 | `https://xueqiu.com/k?q={q}` |
| 东方财富 | 公告财报 | `https://so.eastmoney.com/Search/Index?keyword={q}` |

### 📱 社媒搜索

| 引擎 | 用途 | URL |
|-----|-----|-----|
| 知乎 | 专业问答 | `https://www.zhihu.com/search?type=content&q={q}` |
| YouTube | 视频 | `https://www.youtube.com/results?search_query={q}` |

---

## 搜索技巧

### Dorking 语法
- **精准匹配**：`"关键词"`
- **站内搜索**：`site:example.com 关键词`
- **文件类型**：`关键词 filetype:pdf`

### 引擎选择
- **静态页面**：用 CFFI（`-e cffi`）
- **动态渲染**：用 Playwright（`-e playwright -w 5`）
- **绕过验证**：用 `--interactive` 手动验证

---

## 完整示例

```bash
# 1. 搜索论文
python ~/.openclaw/skills/super-fetch/fetch.py "https://arxiv.org/search/?searchtype=all&query=deep+learning" -e cffi

# 2. 搜索 GitHub
python ~/.openclaw/skills/super-fetch/fetch.py "https://github.com/search?q=python&type=repositories" -e playwright -w 5

# 3. 搜索新闻（带会话）
python ~/.openclaw/skills/super-fetch/fetch.py "https://www.baidu.com/s?wd=今日热点&tn=news" -e cffi -s session.json
```

---

## 注意事项

1. 搜索引擎建议始终使用 Playwright 引擎（`-e playwright`）以获得最佳渲染效果
2. 会话文件默认保存在 `~/.openclaw/skills/super-fetch/session.json`
3. 使用完成后记得清理命名空间：`python ~/.openclaw/skills/super-fetch/get_link.py --clear <ns>`
