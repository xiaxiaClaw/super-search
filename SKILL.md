---
name: super-search
description: 基于 super-fetch 的聚合搜索工具，支持新闻、网页、图片、视频等多种搜索。
user-invocable: true
---

# Super Search

基于 super-fetch 的聚合搜索工具，提供多种搜索能力。

## 搜索类型

### 1. 网页搜索
使用百度/Bing/Google 搜索网页内容。
```bash
python {baseDir}/search.py web "关键词"
```

### 2. 新闻搜索
搜索实时新闻热点。
```bash
python {baseDir}/search.py news "关键词"
```

### 3. 图片搜索
搜索图片。
```bash
python {baseDir}/search.py image "关键词"
```

### 4. 视频搜索
搜索视频。
```bash
python {baseDir}/search.py video "关键词"
```

## 使用示例

```bash
# 搜索今日新闻
python {baseDir}/search.py news "今日热点"

# 搜索网页
python {baseDir}/search.py web "Python教程"

# 搜索科技新闻
python {baseDir}/search.py news "科技"
```

## 搜索引擎

- **网页/新闻**：百度、Bing
- **图片**：百度图片
- **视频**：百度视频

## 注意

- 所有搜索调用 super-fetch 执行
- 搜索结果为原始 HTML，需进一步解析
- 复杂搜索建议使用 playwright 引擎
