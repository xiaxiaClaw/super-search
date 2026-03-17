---
name: super-search
description: 基于 super-fetch 的聚合搜索工具，提供通用搜索、学术、技术等多种领域的专业搜索能力。
user-invocable: true
dependencies:
  - super-fetch
---

# Super Search

基于 super-fetch 的全能搜索矩阵。

## 快速开始

### 通用搜索

```bash
source /tmp/fetch-venv/bin/activate
python ~/.openclaw/skills/super-fetch/fetch.py "https://cn.bing.com/search?q=关键词" -e cffi
```

### 新闻搜索

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://www.baidu.com/s?wd=关键词&tn=news" -e cffi
```

### 图片搜索

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://cn.bing.com/images/search?q=关键词" -e playwright -w 5
```

### 视频搜索

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://v.baidu.com/v?word=关键词" -e playwright -w 5
```

## 推荐搜索引擎

| 类型 | 引擎 | URL | 速度 |
|-----|-----|-----|-----|
| 通用 | Bing | `https://cn.bing.com/search?q={q}` | 快 |
| 通用 | 百度 | `https://www.baidu.com/s?wd={q}` | 快 |
| 通用 | 360 | `https://www.so.com/s?q={q}` | 快 |
| 通用 | 搜狗 | `https://sogou.com/web?query={q}` | 快 |

## 搜索技巧

- **CFFI 模式**：快速，适合静态页面（`-e cffi`）
- **Playwright 模式**：渲染动态内容（`-e playwright -w 5`）
- **人工干预**：绕过验证（`--interactive`）

## 进阶领域

详见 references/ 目录：

- [学术搜索](./references/academic.md) - Arxiv、PapersWithCode、PubMed
- [技术搜索](./references/tech.md) - GitHub、StackOverflow、Hugging Face
- [金融搜索](./references/finance.md) - 雪球、东方财富
- [社媒搜索](./references/social.md) - 知乎、YouTube、微博
