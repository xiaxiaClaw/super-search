# 学术搜索

## Arxiv（AI/物理/数学论文）

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://arxiv.org/search/?searchtype=all&query=关键词" -e cffi
```

## PapersWithCode（论文+代码）

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://paperswithcode.com/search?q=关键词" -e cffi
```

## Semantic Scholar（语义搜索）

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://www.semanticscholar.org/search?q=关键词" -e playwright -w 5
```

## PubMed（医学文献）

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://pubmed.ncbi.nlm.nih.gov/?term=关键词" -e cffi
```

## CNKI 知网

```bash
python ~/.openclaw/skills/super-fetch/fetch.py "https://kns.cnki.net/kns8s/defaultresult/index?kw=关键词" -e playwright -w 5
```
