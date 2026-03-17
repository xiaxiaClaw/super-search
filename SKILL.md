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

| 类型 | 说明 |
|------|------|
| `news` | 新闻热点 |
| `web` | 网页搜索 |
| `image` | 图片搜索 |
| `video` | 视频搜索 |
| `paper` | 论文搜索 |
| `ai` | AI/科技搜索 |
| `finance` | 财经搜索 |
| `politics` | 政治搜索 |
| `academic` | 学术搜索 |
| `shopping` | 购物搜索 |
| `map` | 地图搜索 |

## 可选参数

| 参数 | 说明 |
|------|------|
| `-e, --engine` | 搜索引擎 |
| `-p, --playwright` | 使用 playwright 引擎 |
| `-w, --wait` | 等待秒数 (默认: 5) |
| `-f, --full` | 获取完整内容 |
| `-s, --session` | 会话文件路径 |
| `--login` | 交互式登录 (自动保存会话) |

## 使用示例

### 基础搜索
```bash
# 新闻搜索
python {baseDir}/search.py news "今日热点"

# 网页搜索
python {baseDir}/search.py web "Python教程"

# 图片搜索
python {baseDir}/search.py image "猫咪"

# 论文搜索 (默认 paperswithcode)
python {baseDir}/search.py paper "deep learning"
```

### 登录会话 (绕过验证)
```bash
# 1. 登录 (打开浏览器手动验证)
python {baseDir}/search.py paper "deep learning" --login -p

# 2. 验证成功后，会话自动保存到 sessions/paper_session.json

# 3. 下次直接使用会话
python {baseDir}/search.py paper "machine learning" -s sessions/paper_session.json -p
```

### 指定搜索引擎
```bash
# 论文搜索
python {baseDir}/search.py paper "AI" -e arxiv       # arXiv
python {baseDir}/search.py paper "AI" -e paperswithcode  # Papers with Code
python {baseDir}/search.py paper "AI" -e semantic       # Semantic Scholar
```

## 搜索引擎

### 论文搜索
- `paperswithcode` - 论文+代码 (默认)
- `arxiv` - arXiv 预印本
- `semantic` - Semantic Scholar
- `connectedpapers` - 论文关联图谱

### 图片搜索
- `猫咪` / `cat` - 猫咪图片
- `狗狗` / `dog` - 狗狗图片
- `风景` / `landscape` - 风景图片
- `random` - 随机图片

## 会话管理

- 会话文件默认保存在 `./sessions/` 目录
- 文件命名规则：`{搜索类型}_session.json`，如 `paper_session.json`
- 登录后会自动保存会话，下次无需再验证
