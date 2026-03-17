#!/usr/bin/env python3
"""
Super Search - 聚合搜索工具
基于 super-fetch 实现多种类型搜索
"""

import argparse
import sys
import os

# 搜索模板
SEARCH_TEMPLATES = {
    # 网页搜索
    "web": {
        "baidu": "https://www.baidu.com/s?wd={keyword}",
        "bing": "https://cn.bing.com/search?q={keyword}",
        "sogou": "https://sogou.com/web?query={keyword}",
        "360": "https://www.so.com/s?q={keyword}",
    },
    # 新闻搜索
    "news": {
        "baidu": "https://www.baidu.com/s?wd={keyword}&tn=news",
        "bing": "https://cn.bing.com/search?q={keyword}&ensearch=1",
    },
    # 图片搜索
    "image": {
        "baidu": "https://image.baidu.com/search/index?word={keyword}",
        "bing": "https://cn.bing.com/images/search?q={keyword}",
    },
    # 视频搜索
    "video": {
        "baidu": "https://video.baidu.com/v?word={keyword}",
        "bilibili": "https://search.bilibili.com/video?keyword={keyword}",
    },
}

DEFAULT_ENGINE = "baidu"
FETCH_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "super-fetch", "fetch.py")

def build_search_url(search_type, keyword, engine=None):
    """构建搜索 URL"""
    if search_type not in SEARCH_TEMPLATES:
        print(f"错误: 不支持的搜索类型 '{search_type}'")
        print(f"支持的类型: {', '.join(SEARCH_TEMPLATES.keys())}")
        sys.exit(1)
    
    engine = engine or DEFAULT_ENGINE
    if engine not in SEARCH_TEMPLATES[search_type]:
        engine = list(SEARCH_TEMPLATES[search_type].keys())[0]
    
    template = SEARCH_TEMPLATES[search_type][engine]
    url = template.replace("{keyword}", keyword)
    return url, engine

def main():
    parser = argparse.ArgumentParser(description="Super Search - 聚合搜索工具")
    parser.add_argument("search_type", help="搜索类型: web, news, image, video")
    parser.add_argument("keyword", help="搜索关键词")
    parser.add_argument("-e", "--engine", help=f"搜索引擎 (默认: {DEFAULT_ENGINE})")
    parser.add_argument("-f", "--full", action="store_true", help="获取完整内容")
    parser.add_argument("-p", "--playwright", action="store_true", help="使用 playwright 引擎")
    parser.add_argument("-w", "--wait", type=int, default=5, help="等待秒数")
    
    args = parser.parse_args()
    
    # 构建搜索 URL
    url, engine = build_search_url(args.search_type, args.keyword, args.engine)
    
    print(f"[*] 搜索类型: {args.search_type}")
    print(f"[*] 搜索引擎: {engine}")
    print(f"[*] 关键词: {args.keyword}")
    print(f"[*] URL: {url}")
    print()
    
    # 调用 super-fetch
    fetch_cmd = [
        sys.executable,
        FETCH_SCRIPT,
        url,
    ]
    
    if args.full:
        fetch_cmd.append("--full")
    if args.playwright:
        fetch_cmd.extend(["-e", "playwright", "-w", str(args.wait)])
    else:
        fetch_cmd.extend(["-e", "cffi"])
    
    os.execv(sys.executable, fetch_cmd)

if __name__ == "__main__":
    main()
