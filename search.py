#!/usr/bin/env python3
"""
Super Search - 基于 super-fetch 的聚合搜索工具
"""

import argparse
import subprocess
import sys
import os

# 搜索模板
SEARCH_TEMPLATES = {
    "web": {
        "baidu": "https://www.baidu.com/s?wd={keyword}",
        "bing": "https://cn.bing.com/search?q={keyword}",
    },
    "news": {
        "baidu": "https://www.baidu.com/s?wd={keyword}&tn=news",
        "bing": "https://cn.bing.com/search?q={keyword}&ensearch=1",
    },
}

DEFAULT_ENGINE = "baidu"
SEARCH_TYPES = ["web", "news"]

def get_fetch_script():
    """获取 super-fetch 脚本路径"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fetch_path = os.path.join(os.path.dirname(script_dir), "super-fetch", "fetch.py")
    if not os.path.exists(fetch_path):
        fetch_path = "/home/xunbu/.openclaw/skills/super-fetch/fetch.py"
    return fetch_path

def main():
    parser = argparse.ArgumentParser(description="Super Search - 基于 super-fetch 的聚合搜索")
    parser.add_argument("search_type", choices=SEARCH_TYPES, help="搜索类型: web, news")
    parser.add_argument("keyword", help="搜索关键词")
    parser.add_argument("-e", "--engine", default=DEFAULT_ENGINE, help=f"搜索引擎 (默认: {DEFAULT_ENGINE})")
    parser.add_argument("-p", "--playwright", action="store_true", help="使用 playwright 引擎")
    parser.add_argument("-w", "--wait", type=int, default=5, help="等待秒数")
    parser.add_argument("-f", "--full", action="store_true", help="获取完整内容")
    
    args = parser.parse_args()
    
    # 构建搜索 URL
    templates = SEARCH_TEMPLATES.get(args.search_type, SEARCH_TEMPLATES["web"])
    engine = args.engine if args.engine in templates else DEFAULT_ENGINE
    url = templates[engine].replace("{keyword}", args.keyword)
    
    print(f"[Super Search] 类型: {args.search_type} | 引擎: {engine} | 关键词: {args.keyword}")
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
