# 金融搜索

## 雪球（A股/美股讨论）

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://xueqiu.com/k?q=关键词" -e cffi
```

## 东方财富（公告/财报）

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://so.eastmoney.com/Search/Index?keyword=关键词" -e cffi
```

## Yahoo Finance（全球金融）

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://finance.yahoo.com/lookup?s=关键词" -e playwright -w 5
```
