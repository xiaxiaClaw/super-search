---
name: super-search
description: 基于 super-fetch 的聚合搜索工具，支持新闻、网页、图片、视频、论文、AI、经济等多种搜索。
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
| `video` | 视频搜索 | `python {baseDir}/search.py video "教程"` |
| `paper` | 论文搜索 | `python {baseDir}/search.py paper "深度学习"` |
| `ai` | AI/科技搜索 | `python {baseDir}/search.py ai "GPT"` |
| `finance` | 财经搜索 | `python {baseDir}/search.py finance "股票"` |
| `politics` | 政治搜索 | `python {baseDir}/search.py politics "两会"` |

## 图片搜索

支持的图片类型：
- `猫咪` / `cat` - 猫咪图片
- `狗狗` / `dog` - 狗狗图片
- `风景` / `landscape` - 风景图片
- `random` - 随机图片

```bash
python {baseDir}/search.py image "猫咪"
python {baseDir}/search.py image "random"
```

## 专业搜索

### 论文搜索
```bash
python {baseDir}/search.py paper "人工智能"
python {baseDir}/search.py paper "machine learning"
```

### AI/科技搜索
```bash
python {baseDir}/search.py ai "ChatGPT"
python {baseDir}/search.py ai "大模型"
```

### 财经搜索
```bash
python {baseDir}/search.py finance "黄金价格"
python {baseDir}/search.py finance "股票行情"
```

### 政治搜索
```bash
python {baseDir}/search.py politics "两会"
python {baseDir}/search.py politics "国际关系"
```

## 可选参数

| 参数 | 说明 |
|------|------|
| `-e, --engine` | 搜索引擎 (baidu/bing 默认: baidu) |
| `-p, --playwright` | 使用 playwright 引擎 |
| `-w, --wait` | 等待秒数 (默认: 5) |
| `-f, --full` | 获取完整内容 |
