---
name: super-search
description: 基于 super-fetch 的聚合搜索工具，提供通用搜索、学术、技术、社媒、金融等多种领域的专业搜索能力。
user-invocable: true
dependencies:
  - super-fetch
---

# Super Search

基于 super-fetch 的多领域搜索工具集。

## 快速开始

### 通用搜索

```bash
# Bing（推荐）
python fetch.py "https://cn.bing.com/search?q=关键词" -e cffi

# 百度
python fetch.py "https://www.baidu.com/s?wd=关键词" -e cffi
```

### 新闻搜索

```bash
python fetch.py "https://www.baidu.com/s?wd=关键词&tn=news" -e cffi
python fetch.py "https://news.baidu.com/ns?word=关键词" -e cffi
```

### 图片搜索

```bash
python fetch.py "https://cn.bing.com/images/search?q=关键词" -e playwright -w 5
```

### 视频搜索

```bash
python fetch.py "https://www.bing.com/videos/search?q=关键词" -e playwright -w 5
```

## 搜索引擎速查表

| 类型 | 引擎 | URL 模板 | 推荐引擎 |
|------|------|----------|----------|
| 通用 | Bing | `https://cn.bing.com/search?q={q}` | cffi |
| 通用 | 百度 | `https://www.baidu.com/s?wd={q}` | cffi |
| 通用 | 搜狗 | `https://sogou.com/web?query={q}` | cffi |
| 通用 | 360 | `https://www.so.com/s?q={q}` | cffi |
| 新闻 | 百度新闻 | `https://news.baidu.com/ns?word={q}` | cffi |
| 图片 | Bing 图片 | `https://cn.bing.com/images/search?q={q}` | playwright |
| 视频 | Bing 视频 | `https://www.bing.com/videos/search?q={q}` | playwright |

## 使用规范

### 引擎选择

| 引擎 | 适用场景 |
|------|----------|
| `cffi`（默认）| 静态搜索结果页、速度优先 |
| `playwright` | 动态加载内容、需登录、有验证码 |

### 会话使用

```bash
# 无会话（默认）
python fetch.py "https://cn.bing.com/search?q=关键词"

# 使用默认会话
python fetch.py "https://cn.bing.com/search?q=关键词" -s

# 使用指定会话
python fetch.py "https://cn.bing.com/search?q=关键词" -s my_search.json
```

### 交互模式（处理验证码/登录）

```bash
python fetch.py "https://cn.bing.com/search?q=关键词" -i
```

## 领域搜索

### 学术搜索

| 平台 | 说明 | URL 模板 | 引擎 |
|------|------|----------|------|
| Arxiv | AI/物理/数学论文 | `https://arxiv.org/search/?query={q}` | cffi |
| PapersWithCode | 论文+代码 | `https://paperswithcode.com/search?q={q}` | cffi |
| Semantic Scholar | 语义搜索 | `https://www.semanticscholar.org/search?q={q}` | playwright |
| PubMed | 医学文献 | `https://pubmed.ncbi.nlm.nih.gov/?term={q}` | cffi |
| 知网 | 中文学术 | `https://kns.cnki.net/kns8s/defaultresult/index?kw={q}` | playwright |
| Google Scholar | 综合学术 | `https://scholar.google.com/scholar?q={q}` | playwright |

### 技术搜索

| 平台 | 说明 | URL 模板 | 引擎 |
|------|------|----------|------|
| GitHub | 代码仓库 | `https://github.com/search?q={q}&type=repositories` | playwright |
| StackOverflow | 技术问答 | `https://stackoverflow.com/search?q={q}` | cffi |
| V2EX | 中文社区 | `https://www.v2ex.com/?q={q}` | cffi |
| Hugging Face | AI 模型 | `https://huggingface.co/models?search={q}` | playwright |
| GitHub Issues | 问题搜索 | `https://github.com/search?q={q}&type=issues` | playwright |
| Read the Docs | 文档 | `https://readthedocs.org/search/?q={q}` | cffi |

### 社媒搜索

| 平台 | 说明 | URL 模板 | 引擎 |
|------|------|----------|------|
| 知乎 | 专业问答 | `https://www.zhihu.com/search?type=content&q={q}` | playwright |
| 小红书 | 生活百科 | `https://www.xiaohongshu.com/search_result?keyword={q}` | playwright |
| 微博 | 热点话题 | `https://s.weibo.com/weibo?q={q}` | cffi |
| YouTube | 视频 | `https://www.youtube.com/results?search_query={q}` | playwright |
| Bilibili | 视频 | `https://search.bilibili.com/all?keyword={q}` | playwright |
| 微信搜狗 | 公众号 | `https://weixin.sogou.com/weixin?type=2&query={q}` | cffi |

### 金融搜索

| 平台 | 说明 | URL 模板 | 引擎 |
|------|------|----------|------|
| 雪球 | A股/美股讨论 | `https://xueqiu.com/k?q={q}` | cffi |
| 东方财富 | 公告/财报 | `https://so.eastmoney.com/Search/Index?keyword={q}` | cffi |
| Yahoo Finance | 全球金融 | `https://finance.yahoo.com/lookup?s={q}` | playwright |
| 同花顺 | 行情 | `http://www.10jqka.com.cn/search?query={q}` | cffi |
|  TradingView | 图表 | `https://www.tradingview.com/search/?q={q}` | playwright |

### 购物/电商搜索

| 平台 | 说明 | URL 模板 | 引擎 |
|------|------|----------|------|
| 淘宝 | 综合电商 | `https://s.taobao.com/search?q={q}` | playwright |
| 京东 | 3C/家电 | `https://search.jd.com/Search?keyword={q}` | playwright |
| 拼多多 | 性价比 | `https://mobile.yangkeduo.com/search_result.html?search_key={q}` | playwright |
| 亚马逊 | 全球购 | `https://www.amazon.cn/s?k={q}` | cffi |

### 生活服务搜索

| 平台 | 说明 | URL 模板 | 引擎 |
|------|------|----------|------|
| 美团 | 本地生活 | `https://i.meituan.com/` | playwright |
| 大众点评 | 商家评价 | `https://www.dianping.com/search/keyword/0/0_{q}` | playwright |
| 携程 | 旅游/酒店 | `https://so.ctrip.com/hotels/?keyword={q}` | playwright |
| 12306 | 火车票 | `https://kyfw.12306.cn/otn/leftTicket/init` | playwright |
| 高德地图 | POI | `https://www.amap.com/search?query={q}` | playwright |

## 使用示例

### 示例 1: 快速搜索（静态页）

```bash
python fetch.py "https://cn.bing.com/search?q=python+教程" -e cffi
```

### 示例 2: 动态搜索（Playwright）

```bash
python fetch.py "https://github.com/search?q=python&type=repositories" -e playwright -w 5
```

### 示例 3: 带登录搜索

```bash
# 首次交互登录
python fetch.py "https://www.zhihu.com/search?q=AI" -i

# 后续使用会话
python fetch.py "https://www.zhihu.com/search?q=AI" -s
```

## 参数速查

| 参数 | 说明 | 搜索场景 |
|------|------|----------|
| `-e cffi` | 快速引擎 | 通用/新闻/静态页面 |
| `-e playwright` | JS 渲染引擎 | 动态内容/社媒/学术 |
| `-w 5` | 等待 5 秒 | 复杂动态页面 |
| `-i` | 交互模式 | 需要登录/验证码 |
| `-s` | 使用默认会话 | 复用之前的登录态 |
| `-s my.json` | 使用指定会话 | 多账号切换 |
| `-f` | 全量模式 | 需要完整内容时 |

## 数据存储

- **目录**: `~/.openclaw/super-fetch/`
- 与 super-fetch 共享会话和链接数据库

## AI 新闻搜索（重点）

AI 新闻需要多维度分层搜索，**重点关注：新模型、新产品、新应用动向**。

### AI 新闻搜索维度

#### A. 新模型发布（最高优先级 ⭐⭐⭐⭐⭐）

```bash
# OpenAI 模型动态
python fetch.py "https://www.bing.com/news/search?q=OpenAI+model+release+site:openai.com" -e playwright -w 3

# Anthropic 模型动态
python fetch.py "https://www.bing.com/news/search?q=Anthropic+Claude+model" -e playwright -w 3

# Google AI 模型动态
python fetch.py "https://www.bing.com/news/search?q=Google+DeepMind+AI+model+Gemini" -e playwright -w 3

# Meta AI 模型动态
python fetch.py "https://www.bing.com/news/search?q=Meta+AI+Llama+model+release" -e playwright -w 3

# Mistral AI 模型动态
python fetch.py "https://www.bing.com/news/search?q=Mistral+AI+model+release" -e playwright -w 3

# 国内大模型（百度/阿里/字节/DeepSeek）- 用 Bing 国际版搜索中文
python fetch.py "https://cn.bing.com/search?q=文心一言+OR+通义千问+OR+豆包+OR+DeepSeek+发布+2026" -e playwright -w 3
```

#### B. 新产品/新应用发布（最高优先级 ⭐⭐⭐⭐⭐）

```bash
# Product Hunt 新品
python fetch.py "https://www.producthunt.com/" -e playwright -w 5
python fetch.py "https://www.producthunt.com/search?q=AI" -e playwright -w 3

# AI 产品发布
python fetch.py "https://www.bing.com/news/search?q=AI+product+launch+2026" -e playwright -w 3

# AI 应用爆款
python fetch.py "https://www.reddit.com/r/MachineLearning/" -e playwright -w 3
```

#### C. 社区热度/病毒传播（关键维度）

```bash
# Reddit AI 热点
python fetch.py "https://www.reddit.com/search/?q=AI+viral+OR+AI+trending" -e playwright -w 3

# Hacker News AI
python fetch.py "https://news.ycombinator.com/" -e playwright -w 3

# GitHub Trending AI
python fetch.py "https://github.com/trending" -e playwright -w 5
```

#### D. 大厂动态/产品发布

```bash
# Bing AI 新闻
python fetch.py "https://www.bing.com/news/search?q=AI+product+launch+2026" -e playwright -w 3

# 搜狗 AI 新闻
python fetch.py "https://www.sogou.com/web?query=AI+大模型+发布+site:news.sina.com.cn" -e cffi
```

#### E. 垂直媒体/专业来源

```bash
# 36氪 AI
python fetch.py "https://www.36kr.com/search/articles/AI" -e playwright -w 3

# 机器之心
python fetch.py "https://www.jiqizhixin.com/" -e playwright -w 3

# Bing AI 专题
python fetch.py "https://www.bing.com/news/search?q=AI+model+release+China" -e playwright -w 3
```

### AI 新闻输出格式

```
## AI 新闻速递（YYYY-MM-DD）

### 🆕 新模型 / ⭐⭐⭐⭐⭐
1. [模型名称] - [一句话描述]
   > 🔗 来源 | 发布时间

### 🚀 新产品 / ⭐⭐⭐⭐
2. [产品名称] - [一句话描述]
   > 🔗 来源 | 发布时间

### 💡 新应用 / ⭐⭐⭐
3. [应用名称] - [一句话描述]
   > 🔗 来源 | 发布时间

### 🔥 社区热点 / ⭐⭐⭐⭐
4. [热点内容] - [一句话描述]
   > 🔗 来源 | 热度指标
```

### 热度判断标准（新模型/产品/应用优先）

| 类型 | 热度 | 说明 |
|------|------|------|
| **新模型发布** | ⭐⭐⭐⭐⭐ | OpenAI/Anthropic/Google/Meta/国内大厂 |
| **新产品发布** | ⭐⭐⭐⭐⭐ | Product Hunt 热门、AI 应用爆款 |
| **新应用上线** | ⭐⭐⭐⭐ | AI 落地案例、行业应用 |
| **大厂官宣** | ⭐⭐⭐⭐ | 大厂 AI 动态 |
| **社区病毒传播** | ⭐⭐⭐⭐ | GitHub star暴涨、刷屏 |
| **论文/研究突破** | ⭐⭐⭐ | 学术进展 |

### AI 新闻源速查

| 来源 | 类型 | URL | 引擎 |
|------|------|-----|------|
| 机器之心 | 垂直媒体 | https://www.jiqizhixin.com/ | playwright |
| 36氪 | 科技媒体 | https://www.36kr.com/ | playwright |
| Reddit r/MachineLearning | 社区 | https://www.reddit.com/r/MachineLearning/ | playwright |
| Hacker News | 社区 | https://news.ycombinator.com/ | cffi |
| GitHub Trending | 开源趋势 | https://github.com/trending | playwright |
| Product Hunt | 产品发布 | https://www.producthunt.com/ | playwright |
| 百度 AI 新闻 | 搜索聚合 | https://www.baidu.com/s?wd=AI+新闻 | playwright |

## 详细领域文档

详见 references/ 目录：

- [学术搜索](./references/academic.md) - Arxiv、PapersWithCode、PubMed、知网等
- [技术搜索](./references/tech.md) - GitHub、StackOverflow、Hugging Face 等
- [社媒搜索](./references/social.md) - 知乎、小红书、微博、B站等
- [金融搜索](./references/finance.md) - 雪球、东方财富、Yahoo Finance 等
- [购物搜索](./references/shopping.md) - 淘宝、京东、拼多多、亚马逊等
- [生活服务](./references/lifestyle.md) - 美团、大众点评、携程、12306 等
- [新闻搜索](./references/news.md) - 百度新闻、新浪、网易、澎湃等
