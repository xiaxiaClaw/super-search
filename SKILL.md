---
name: super-search
description: 基于 super-fetch 的聚合搜索工具，支持新闻、网页、图片、视频等多种搜索。
user-invocable: true
---

# Super Search

基于 super-fetch 的聚合搜索工具，提供多种类型的搜索能力。

## 核心命令

### 基本语法
```bash
python {baseDir}/search.py <搜索类型> [关键词] [参数]
```

### 搜索类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `news` | 新闻热点 | `python {baseDir}/search.py news "今日热点"` |
| `web` | 网页搜索 | `python {baseDir}/search.py web "Python教程"` |
| `image` | 图片搜索 | `python {baseDir}/search.py image "猫咪"` |
| `video` | 视频搜索 | `python {baseDir}/search.py video "电影"` |

## 可选参数

| 参数 | 说明 |
|------|------|
| `-e, --engine` | 搜索引擎 (baidu/bing 默认: baidu) |
| `-p, --playwright` | 使用 playwright 引擎 |
| `-w, --wait` | 等待秒数 (默认: 5) |
| `-f, --full` | 获取完整内容 |

## 搜索流程 (SOP)

1. **选择搜索类型**：根据需求选择 news/web/image/video
2. **执行搜索**：调用 search.py
3. **解析结果**：分析返回的内容
4. **清理**：使用 super-fetch 的 get_link.py 清理命名空间

## 搜索引擎支持

- **百度 (baidu)**：默认搜索引擎
- **必应 (bing)**：可选

## 使用示例

```bash
# 搜索今日新闻热点
python {baseDir}/search.py news "今日热点"

# 搜索科技新闻
python {baseDir}/search.py news "科技"

# 使用 playwright 搜索
python {baseDir}/search.py web "Python教程" -p

# 使用 bing 引擎
python {baseDir}/search.py web "教程" -e bing
```

## 注意

- 搜索结果基于搜索引擎返回的 HTML 内容
- 复杂内容建议使用 playwright 引擎
- 定期清理命名空间以释放空间
