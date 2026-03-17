#!/usr/bin/env python3
"""
Super Search - 基于 super-fetch 的聚合搜索工具
"""

import argparse
import subprocess
import sys
import os
import json
import urllib.request

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
}

DEFAULT_ENGINE = "baidu"
SEARCH_TYPES = ["web", "news", "image", "video"]

def get_fetch_script():
    """获取 super-fetch 脚本路径"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fetch_path = os.path.join(os.path.dirname(script_dir), "super-fetch", "fetch.py")
    if not os.path.exists(fetch_path):
        fetch_path = "/home/xunbu/.openclaw/skills/super-fetch/fetch.py"
    return fetch_path

def search_image(keyword):
    """图片搜索 - 返回真实图片URL"""
    keyword = keyword.lower().strip()
    
    print(f"[Super Search] 🖼️ 图片搜索: {keyword}")
    print()
    
    try:
        if "猫" in keyword or "cat" in keyword:
            # 猫咪图片 - Cataas
            print("🐱 猫咪图片URL:")
            for i in range(1, 6):
                print(f"  {i}. https://cataas.com/cat?width=800&height=600&random={i}")
            return
            
        elif "狗" in keyword or "dog" in keyword:
            # 狗狗图片 - DogCEO API
            print("🐕 狗狗图片URL:")
            for i in range(1, 6):
                print(f"  {i}. https://images.dog.ceo/breeds/labrador/n02104029_{i}.jpg")
            return
            
        elif "random" in keyword or "随机" in keyword:
            # 随机图片 - Picsum
            print("🎲 随机图片URL:")
            for i in range(1, 6):
                print(f"  {i}. https://picsum.photos/800/600?random={i}")
            return
            
        elif "风景" in keyword or "landscape" in keyword:
            # 风景图片
            print("🏞️ 风景图片URL:")
            for i in range(1, 6):
                print(f"  {i}. https://picsum.photos/id/1{i:03d}/800/600")
            return
            
        else:
            # 默认搜索猫咪
            print(f"⚠️ 未知关键词 '{keyword}'，默认搜索猫咪图片")
            print("🐱 猫咪图片URL:")
            for i in range(1, 6):
                print(f"  {i}. https://cataas.com/cat?width=800&height=600&random={i}")
            return
            
    except Exception as e:
        print(f"❌ 图片搜索失败: {e}")
        return

    print("\n可用图片类型:")
    print("  - 猫咪/cat: 猫咪图片")
    print("  - 狗狗/dog: 狗狗图片") 
    print("  - 风景/landscape: 风景图片")
    print("  - random: 随机图片")

def main():
    parser = argparse.ArgumentParser(description="Super Search - 基于 super-fetch 的聚合搜索")
    parser.add_argument("search_type", choices=SEARCH_TYPES, help="搜索类型: web, news, image, video")
    parser.add_argument("keyword", help="搜索关键词")
    parser.add_argument("-e", "--engine", default=DEFAULT_ENGINE, help=f"搜索引擎 (默认: {DEFAULT_ENGINE})")
    parser.add_argument("-p", "--playwright", action="store_true", help="使用 playwright 引擎")
    parser.add_argument("-w", "--wait", type=int, default=5, help="等待秒数")
    parser.add_argument("-f", "--full", action="store_true", help="获取完整内容")
    
    args = parser.parse_args()
    
    # 图片搜索特殊处理
    if args.search_type == "image":
        search_image(args.keyword)
        return
    
    # 构建搜索 URL
    templates = WEB_TEMPLATES.get(args.search_type, WEB_TEMPLATES["web"])
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
