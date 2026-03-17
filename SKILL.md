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

## 图片搜索说明

图片搜索返回**真实图片URL**，可直接用于发送：

```bash
# 搜索猫咪图片
python {baseDir}/search.py image "猫咪"

# 搜索狗狗图片  
python {baseDir}/search.py image "dog"

# 随机图片
python {baseDir}/search.py image "random"
```

支持的图片类型：
- `猫咪` - 调用 TheCatAPI
- `狗狗/dog` - 调用 DogCEO API
- `random` - 调用 Picsum 随机图

## 视频搜索

```bash
# 搜索视频
python {baseDir}/search.py video "教程"
```

## 可选参数

| 参数 | 说明 |
|------|------|
| `-e, --engine` | 搜索引擎 (baidu/bing 默认: baidu) |
| `-p, --playwright` | 使用 playwright 引擎 |
| `-w, --wait` | 等待秒数 (默认: 5) |
| `-f, --full` | 获取完整内容 |

## 使用示例

```bash
# 今日新闻
python {baseDir}/search.py news "今日热点"

# 网页搜索
python {baseDir}/search.py web "Python教程"

# 搜索图片
python {baseDir}/search.py image "猫咪"

# 搜索视频
python {baseDir}/search.py video "科普"
```

## 搜索引擎

- **百度 (baidu)** - 默认
- **必应 (bing)** - 可选
