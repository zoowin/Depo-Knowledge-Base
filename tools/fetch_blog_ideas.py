import requests
import json
import os
import time
import random
import html
from datetime import datetime

# --- Configuration ---
# 核心种子词：基于 Depology 的产品线
SEED_KEYWORDS = [
    "matrixyl 3000", 
    "argireline solution", 
    "micro-dart patches", 
    "retinol for sensitive skin", 
    "cica redness relief",
    "peptide serum benefits"
]

# 目标 Subreddits
SUBREDDITS = ["SkincareAddiction", "30PlusSkinCare", "AsianBeauty", "DermatologyQuestions"]

# 目标文件
TARGET_FILE = r"..\Shopify SEO Blog\Blog_Topic_Pool.md"

def fetch_google_suggestions(keyword):
    """
    获取 Google 搜索下拉推荐词 (Long-tail Keywords)
    """
    print(f"🔍 [Google] Searching suggestions for '{keyword}'...")
    url = f"http://google.com/complete/search?client=chrome&q={keyword}&hl=en"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    suggestions = []
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            results = response.json()[1] # Google API returns [query, [suggestions], ...]
            # 过滤掉太短的或完全一样的
            for res in results:
                if res != keyword and len(res) > len(keyword):
                    suggestions.append(res)
    except Exception as e:
        print(f"❌ Error fetching Google suggestions: {e}")
        
    return suggestions[:5] # 只取前5个最相关的

def fetch_reddit_questions(subreddits):
    """
    获取 Reddit 上的真实用户提问 (Content Angles)
    """
    print(f"🔍 [Reddit] Hunting for questions...")
    questions = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for sub in subreddits:
        url = f"https://www.reddit.com/r/{sub}/new.json?limit=20" # 看最新帖子
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                posts = data['data']['children']
                for post in posts:
                    title = html.unescape(post['data']['title'])
                    
                    # 简单的自然语言处理：筛选像“问题”的帖子
                    triggers = ["?", "help", "advice", "routine", "vs", "compare"]
                    if any(t in title.lower() for t in triggers):
                        questions.append({
                            'subreddit': sub,
                            'title': title,
                            'url': f"https://reddit.com{post['data']['permalink']}"
                        })
            time.sleep(1) 
        except Exception as e:
            print(f"❌ Error fetching Reddit r/{sub}: {e}")
            
    # 随机打乱并只取一部分，避免每次都一样
    random.shuffle(questions)
    return questions[:8]

def format_suggestion_to_todo(keyword, source_type):
    if source_type == "Google":
        # Google 词通常是短语，适合做 H2 或文章主题
        return f"- [ ] **(Keyword)** `{keyword}` \n  - *Intent*: 🔍 Search Query\n  - *Angle*: Ultimate Guide or Comparison"
    else:
        # Reddit 是具体问题
        title = keyword['title']
        sub = keyword['subreddit']
        return f"- [ ] **(Question)** \"{title}\"\n  - *Source*: r/{sub}\n  - *Angle*: Answer this specific user pain point"

def update_blog_pool(google_data, reddit_data):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, TARGET_FILE)
    
    if not os.path.exists(file_path):
        print(f"❌ Target file not found: {file_path}")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    print(f"📝 Writing to Blog Topic Pool...")
    
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"\n\n## 🕸️ Auto-Hunted Ideas ({timestamp})\n")
        f.write("> From Google Autocomplete & Reddit Discussions\n\n")
        
        if google_data:
            f.write("### 🔍 Google Long-tail Keywords (SEO Gold)\n")
            for item in google_data:
                f.write(f"{format_suggestion_to_todo(item, 'Google')}\n")
        
        if reddit_data:
            f.write("\n### 🗣️ Reddit User Questions (Content Angles)\n")
            for item in reddit_data:
                f.write(f"{format_suggestion_to_todo(item, 'Reddit')}\n")

def main():
    print("--- Depology SEO Topic Hunter ---")
    
    # 1. Google 挖掘
    all_suggestions = []
    for seed in SEED_KEYWORDS:
        suggs = fetch_google_suggestions(seed)
        all_suggestions.extend(suggs)
        time.sleep(0.5)
    
    # 随机选一些展示，不要太多
    selected_suggestions = random.sample(all_suggestions, min(len(all_suggestions), 8))
    
    # 2. Reddit 挖掘
    reddit_questions = fetch_reddit_questions(SUBREDDITS)
    
    # 3. 写入文件
    if selected_suggestions or reddit_questions:
        update_blog_pool(selected_suggestions, reddit_questions)
        print("\n✅ Done! New topics added to 'Shopify SEO Blog/Blog_Topic_Pool.md'")
    else:
        print("\n⚠️ No new topics found.")

if __name__ == "__main__":
    main()
