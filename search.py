#!/usr/bin/env python3
"""
Super Search - 基于 super-fetch 的聚合搜索工具
"""

import argparse
import subprocess
import sys
import os

# 搜索引擎模板
WEB_TEMPLATES = {
    "web": {
        "baidu": "https://www.baidu.com/s?wd={keyword}",
        "bing": "https://cn.bing.com/search?q={keyword}",
    },
    "news": {
        "baidu": "https://www.baidu.com/s?wd={keyword}&tn=news",
        "bing": "https://cn.bing.com/search?q={keyword}&ensearch=1",
    },
    "video": {
        "baidu": "https://v.baidu.com/v?word={keyword}",
        "bilibili": "https://search.bilibili.com/video?keyword={keyword}",
    },
    # 论文搜索 - 多来源
    "paper": {
        "arxiv": "https://arxiv.org/search/?searchtype=all&query={keyword}&start=0",
        "paperswithcode": "https://paperswithcode.com/search?q={keyword}",
        "semantic": "https://www.semanticscholar.org/search?q={keyword}&sort=relevance",
        "connectedpapers": "https://www.connectedpapers.com/search?q={keyword}",
        "researchgate": "https://www.researchgate.net/search/publication?q={keyword}",
        "pubmed": "https://pubmed.ncbi.nlm.nih.gov/?term={keyword}",
        "baidu": "https://www.baidu.com/s?wd={keyword} 论文",
    },
    # AI/科技搜索
    "ai": {
        "baidu": "https://www.baidu.com/s?wd={keyword} AI 人工智能",
        "bing": "https://cn.bing.com/search?q={keyword} AI",
    },
    # 财经搜索
    "finance": {
        "baidu": "https://www.baidu.com/s?wd={keyword} 财经 股票",
        "bing": "https://finance.bing.com/search?q={keyword}",
    },
    # 政治搜索
    "politics": {
        "baidu": "https://www.baidu.com/s?wd={keyword} 政治 时政",
        "bing": "https://cn.bing.com/search?q={keyword} politics",
    },
    # 学术搜索
    "academic": {
        "baidu": "https://www.baidu.com/s?wd={keyword} 学术 研究",
        "bing": "https://cn.bing.com/academic/search?q={keyword}",
    },
    # 购物搜索
    "shopping": {
        "baidu": "https://www.baidu.com/s?wd={keyword} 价格 购买",
        "bing": "https://cn.bing.com/shop/search?q={keyword}",
    },
    # 地图搜索
    "map": {
        "baidu": "https://map.baidu.com/?newmap=1&wd={keyword}",
        "bing": "https://www.bing.com/maps?q={keyword}",
    },
}

DEFAULT_ENGINE = "baidu"
PAPER_DEFAULT_ENGINE = "paperswithcode"
SEARCH_TYPES = ["web", "news", "image", "video", "paper", "ai", "finance", "politics", "academic", "shopping", "map"]

# Session 文件默认目录
SESSION_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sessions")
DEFAULT_SESSION = os.path.join(SESSION_DIR, "session.json")  # 统一会话文件

# 图片URL模板
IMAGE_URLS = {
    "猫": "https://cataas.com/cat?width=800&height=600&random={i}",
    "cat": "https://cataas.com/cat?width=800&height=600&random={i}",
    "狗": "https://images.dog.ceo/breeds/labrador/n02104029_{i}.jpg",
    "dog": "https://images.dog.ceo/breeds/labrador/n02104029_{i}.jpg",
    "风景": "https://picsum.photos/id/1{i:03d}/800/600",
    "landscape": "https://picsum.photos/id/1{i:03d}/800/600",
    "random": "https://picsum.photos/800/600?random={i}",
}

def get_fetch_script():
    """获取 super-fetch 脚本路径"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fetch_path = os.path.join(os.path.dirname(script_dir), "super-fetch", "fetch.py")
    if not os.path.exists(fetch_path):
        fetch_path = "/home/xunbu/.openclaw/skills/super-fetch/fetch.py"
    return fetch_path

def search_image(keyword):
    """图片搜索 - 返回真实图片URL"""
    keyword_lower = keyword.lower().strip()
    
    print(f"[Super Search] 🖼️ 图片搜索: {keyword}")
    print()
    
    # 匹配图片类型
    img_type = None
    for key in IMAGE_URLS:
        if key in keyword_lower:
            img_type = key
            break
    
    if img_type is None:
        # 默认猫咪
        img_type = "猫"
    
    urls = IMAGE_URLS[img_type]
    print(f"📷 图片 ({img_type}):")
    for i in range(1, 6):
        print(f"  {i}. {urls.format(i=i)}")

def main():
    parser = argparse.ArgumentParser(description="Super Search - 基于 super-fetch 的聚合搜索")
    parser.add_argument("search_type", choices=SEARCH_TYPES, help="搜索类型")
    parser.add_argument("keyword", help="搜索关键词")
    parser.add_argument("-e", "--engine", default=DEFAULT_ENGINE, help=f"搜索引擎 (默认: {DEFAULT_ENGINE})")
    parser.add_argument("-p", "--playwright", action="store_true", help="使用 playwright 引擎")
    parser.add_argument("-w", "--wait", type=int, default=5, help="等待秒数")
    parser.add_argument("-f", "--full", action="store_true", help="获取完整内容")
    parser.add_argument("-s", "--session", help="会话文件路径 (默认: ./sessions/{类型}_session.json)")
    parser.add_argument("--login", action="store_true", help="交互式登录 (会自动保存会话)")
    
    args = parser.parse_args()
    
    # 图片搜索特殊处理
    if args.search_type == "image":
        search_image(args.keyword)
        return
    
    # 构建搜索 URL
    templates = WEB_TEMPLATES.get(args.search_type, WEB_TEMPLATES["web"])
    # 论文搜索默认用 arxiv
    if args.search_type == "paper" and args.engine == DEFAULT_ENGINE:
        engine = PAPER_DEFAULT_ENGINE
    else:
        engine = args.engine if args.engine in templates else DEFAULT_ENGINE
    url = templates[engine].replace("{keyword}", args.keyword)
    
    # 显示搜索类型图标
    icons = {
        "web": "🌐", "news": "📰", "video": "🎬", 
        "paper": "📚", "ai": "🤖", "finance": "💰",
        "politics": "🏛️", "academic": "🎓", "shopping": "🛒", "map": "🗺️"
    }
    icon = icons.get(args.search_type, "🔍")
    
    print(f"[Super Search] {icon} {args.search_type} | 引擎: {engine} | 关键词: {args.keyword}")
    print(f"[Super Search] URL: {url}")
    print()
    
    # 获取 fetch 脚本路径
    fetch_script = get_fetch_script()
    
    if not os.path.exists(fetch_script):
        print(f"错误: 找不到 super-fetch 脚本: {fetch_script}")
        sys.exit(1)
    
    # 构建 fetch 命令
    cmd = [sys.executable, fetch_script, url]
    
    if args.full:
        cmd.append("--full")
    
    if args.login:
        cmd.append("--login")
        # 自动保存会话（统一使用 session.json）
        os.makedirs(SESSION_DIR, exist_ok=True)
        if args.session:
            session_file = args.session
        else:
            session_file = DEFAULT_SESSION
        cmd.extend(["-s", session_file])
        print(f"[Super Search] 💾 会话将保存至: {session_file}")
    elif args.session:
        cmd.extend(["-s", args.session])
    
    if args.playwright:
        cmd.extend(["-e", "playwright", "-w", str(args.wait)])
    else:
        cmd.append("-e")
        cmd.append("cffi")
    
    # 执行搜索
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[Super Search] 已取消")
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()
