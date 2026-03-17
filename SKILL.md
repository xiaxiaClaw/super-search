---
name: super-search
description: 全能型聚合搜索路由指令集。基于 super-fetch 引擎，支持学术、技术、金融、法律、社媒等 20+ 领域的高级信息挖掘。
version: 1.0.0
user-invocable: true
dependencies:
  - super-fetch
---

# Super Search (The Intelligence Matrix)

本技能通过提供覆盖全领域的 **URL 构造模板**，指导 Agent 动态构造搜索请求，并驱动底层的 **`super-fetch`** 模块执行高精度的网页抓取与正文提取。

## 🌐 1. 全领域搜索矩阵 (URL Templates)

请将 `{q}` 替换为经过 URL 编码（URL Encoded）的关键词。

### 🏢 通用搜索 (General)
| 引擎 | 核心优势 | URL 模板 |
| :--- | :--- | :--- |
| **Bing** | 全球通用，渲染效果极佳 | `https://cn.bing.com/search?q={q}` |
| **Google** | 索引最全，支持高级 Dorking 语法 | `https://www.google.com/search?q={q}` |
| **Baidu** | 中国境内机构、政府、新闻 | `https://www.baidu.com/s?wd={q}` |

### 🎓 学术与研究 (Research)
| 引擎 | 适用领域 | URL 模板 |
| :--- | :--- | :--- |
| **Arxiv** | AI、物理、数学论文预印本 | `https://arxiv.org/search/?searchtype=all&query={q}` |
| **PapersWithCode** | AI 论文及其 GitHub 实现代码 | `https://paperswithcode.com/search?q={q}` |
| **SemanticScholar** | 语义化文献关联与引文分析 | `https://www.semanticscholar.org/search?q={q}` |
| **Hugging Face** | AI 模型、数据集、Spaces 应用 | `https://huggingface.co/models?search={q}` |
| **PubMed** | 医学、生命科学专业文献 | `https://pubmed.ncbi.nlm.nih.gov/?term={q}` |
| **CNKI (知网)** | 中国学术期刊 (需 --login 模式) | `https://kns.cnki.net/kns8s/defaultresult/index?kw={q}` |

### 💻 技术与编程 (Dev & Tech)
| 引擎 | 适用领域 | URL 模板 |
| :--- | :--- | :--- |
| **GitHub** | 全球开源项目、代码仓库 | `https://github.com/search?q={q}&type=repositories` |
| **StackOverflow** | 编程报错排查与技术问答 | `https://stackoverflow.com/search?q={q}` |
| **Phind** | 程序员专用 AI 搜索引擎 | `https://www.phind.com/search?q={q}` |
| **V2EX** | 极客社区、中文技术讨论 | `https://www.google.com/search?q=site:v2ex.com/t+{q}` |

### 📈 金融与商业 (Finance)
| 引擎 | 适用领域 | URL 模板 |
| :--- | :--- | :--- |
| **雪球 (Xueqiu)** | A股/美股/港股投资讨论、研报 | `https://xueqiu.com/k?q={q}` |
| **Yahoo Finance** | 全球金融市场数据、财报 | `https://finance.yahoo.com/lookup?s={q}` |
| **东方财富** | 国内公告、个股行情 | `https://so.eastmoney.com/Search/Index?keyword={q}` |

### 📱 社交媒体与趋势 (Social)
| 引擎 | 适用领域 | URL 模板 |
| :--- | :--- | :--- |
| **知乎 (Zhihu)** | 高质量中文长文、专业问答 | `https://www.zhihu.com/search?type=content&q={q}` |
| **小红书 (XHS)** | 消费决策、生活百科 (需 Playwright) | `https://www.xiaohongshu.com/search_result?keyword={q}` |
| **YouTube** | 全球视频资讯、教程 | `https://www.youtube.com/results?search_query={q}` |

---

## 🛠 2. 搜索增强技巧 (Search Dorking)

Agent 应当在 `{q}` 中加入指令以过滤噪音：
- **精准匹配**：`"{q}"` (给词加双引号)
- **站内搜索**：`site:example.com {q}`
- **文件类型**：`{q} filetype:pdf` (查找文档/研报)
- **排除干扰**：`{q} -广告 -推广`

---

## 🔄 3. Agent 标准操作流 (SOP)

### 步骤一：路径构造
根据用户问题，动态拼接 URL。
*示例：查找 DeepSeek 推理原理* -> 使用 Arxiv -> `https://arxiv.org/search/?searchtype=all&query=DeepSeek+Reasoning`

### 步骤二：调用 Super Fetch 执行抓取
使用 **`super-fetch`** 技能下的 `fetch.py`。
**注意：搜索引擎页面建议始终强制开启 Playwright 引擎。**
```bash
# 自动识别脚本路径进行调用
python ~/.openclaw/skills/super-fetch/fetch.py "<构造好的URL>" -e playwright -w 3
```

### 步骤三：提取代号与深度阅读
1. 解析 `fetch.py` 返回的 Markdown。
2. 识别条目链接代号（如 `(@ns-1)`）。
3. 调用 **`get_link.py`** 获取真实地址：
   `python ~/.openclaw/skills/super-fetch/get_link.py ns-1`
4. 再次对详情页 URL 使用 `fetch.py` 进行深度阅读。

### 步骤四：释放命名空间 (Cleanup)
分析任务结束后，及时清理该搜索任务产生的本地链接映射。
```bash
python ~/.openclaw/skills/super-fetch/get_link.py --clear ns
```

---

## 💡 4. 极端场景决策 (Edge Cases)

- **返回 "Just a moment" 或 403**：这是触发了 Cloudflare 或人机验证。**对策**：向用户请求协助，执行 `python fetch.py "<URL>" --login` 开启手动验证。
- **搜索结果太少**：检查是否关键词太长。**对策**：缩短关键词或将其翻译成英文再次尝试。
- **信息过载**：不要一次性反查所有链接。根据摘要评分，只反查排名前 3 的高相关度代号。

---
**提示**：本技能高度依赖 `super-fetch` 的安装路径 `~/.openclaw/skills/super-fetch/`。确保脚本具备执行权限。
