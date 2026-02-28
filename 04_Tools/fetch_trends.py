import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime
import os
import time
import random
import requests
import html
import json

# --- Configuration ---
KEYWORDS = ["skincare", "anti-aging", "retinol", "k-beauty", "wrinkle treatment", "eye cream", "peptide serum"]
REDDIT_SUBREDDITS = ["SkincareAddiction", "30PlusSkinCare", "AsianBeauty"]
# TARGET_FILE = r"..\Operations\Topic Pool.md"  # Relative path to Topic Pool

# --- Google Trends Setup ---
try:
    # 尝试初始化 Google Trends
    pytrends = TrendReq(
        hl='en-US', 
        tz=360, 
        timeout=(10, 25)
    )
except:
    pytrends = None

# --- Google Trends Method ---
def fetch_rising_queries(keywords):
    print("🔍 Fetching trends from Google Trends (Official API)...")
    rising_topics = []
    
    if not pytrends:
        print("⚠️ Google Trends API initialization failed.")
        return []

    try:
        # Build payload
        pytrends.build_payload(keywords, cat=0, timeframe='today 1-m', geo='US', gprop='')
        related_queries = pytrends.related_queries()
        
        for kw in keywords:
            if related_queries.get(kw) and related_queries[kw]['rising'] is not None:
                # Get top 3 rising queries per keyword
                top_rising = related_queries[kw]['rising'].head(3)
                for index, row in top_rising.iterrows():
                    query = row['query']
                    value = row['value'] # Can be 'Breakout' or a percentage increase
                    rising_topics.append({'source': 'Google Trends', 'keyword': kw, 'query': query, 'trend': value})
            time.sleep(1) # Be nice to Google API
            
    except Exception as e:
        print(f"❌ Error fetching Google trends: {e}")
        
    return rising_topics

# --- Google Autocomplete Method ---
def fetch_google_suggestions(keywords):
    print("🔍 Fetching autocomplete suggestions from Google Search...")
    suggestions_topics = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for kw in keywords:
        # Using Google's public autocomplete API
        url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={kw}"
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if len(data) >= 2:
                    suggestions = data[1]
                    count = 0
                    for suggestion in suggestions:
                        if suggestion.lower() != kw.lower() and count < 3:
                            suggestions_topics.append({
                                'source': 'Google Search',
                                'keyword': kw,
                                'query': suggestion,
                                'trend': 'Popular Search'
                            })
                            count += 1
            time.sleep(1) # Be polite
            
        except Exception as e:
            print(f"❌ Error fetching suggestions for {kw}: {e}")

    return suggestions_topics

# --- Reddit Method ---
def fetch_reddit_trends(subreddits):
    print("🔍 Fetching trends from Reddit...")
    reddit_topics = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for sub in subreddits:
        url = f"https://www.reddit.com/r/{sub}/top.json?t=week&limit=5"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                posts = data['data']['children']
                for post in posts:
                    title = html.unescape(post['data']['title'])
                    score = post['data']['score']
                    if score > 50: 
                        reddit_topics.append({
                            'source': 'Reddit',
                            'keyword': sub,
                            'query': title,
                            'trend': f"{score} upvotes"
                        })
            else:
                print(f"⚠️ Failed to fetch r/{sub}: Status {response.status_code}")
            time.sleep(1) 

        except Exception as e:
            print(f"❌ Error fetching Reddit r/{sub}: {e}")
            
    if not reddit_topics:
        # Sample fallback
        reddit_topics.append({
            'source': 'Reddit',
            'keyword': 'SkincareAddiction',
            'query': '[B&A] Sample Reddit Topic',
            'trend': 'N/A'
        })

    return reddit_topics

def format_for_depology(trend_item):
    query = trend_item['query']
    source = trend_item['source']
    context = trend_item['keyword']
    
    if source == 'Google Trends':
        query = query.title()
        return f"- [ ] **Trending: {query}** (Source: Google Trends '{context}')"
    
    elif source == 'Google Search':
        query = query.title()
        return f"- [ ] **Search Suggestion: {query}** (Source: Google Autocomplete '{context}')"
    
    elif source == 'Reddit':
        if len(query) > 80: query = query[:77] + "..."
        return f"- [ ] **Reddit: {query}** (Source: Reddit r/{context})"

    return f"- [ ] **{query}** (Source: {source})"

def update_topic_pool(new_topics):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level from 'tools' to 'Depo EDM Knowledge Base'
    base_dir = os.path.dirname(script_dir)
    # Modified path to match actual structure
    file_path = os.path.join(base_dir, "01_Strategy_and_Planning", "Topic_Pool.md")
    
    if not os.path.exists(file_path):
        print(f"❌ Topic Pool file not found at: {file_path}")
        # Try fallback to absolute path just in case
        fallback_path = r"c:\Users\曾泽南\Desktop\DEP\Depo-Knowledge-Base\01_Strategy_and_Planning\Topic_Pool.md"
        if os.path.exists(fallback_path):
             file_path = fallback_path
        else:
             return

    print(f"📝 Appending {len(new_topics)} new topics to Topic Pool...")
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"\n\n## 🌍 Auto-Fetched Trends ({timestamp})\n")
        f.write("*Sources: Google Trends, Google Autocomplete, Reddit*\n\n")
        
        # Grouping
        g_trends = [t for t in new_topics if t['source'] == 'Google Trends']
        g_search = [t for t in new_topics if t['source'] == 'Google Search']
        reddit = [t for t in new_topics if t['source'] == 'Reddit']
        
        if g_trends:
            f.write("### Google Trends (Rising Queries)\n")
            for topic in g_trends:
                f.write(f"{format_for_depology(topic)}\n")
            f.write("\n")

        if g_search:
            f.write("### Google Search Suggestions\n")
            for topic in g_search:
                f.write(f"{format_for_depology(topic)}\n")
            f.write("\n")
            
        if reddit:
            f.write("### Reddit Discussions\n")
            for topic in reddit[:5]:
                f.write(f"{format_for_depology(topic)}\n")

def main():
    print("--- Depology Trend Fetcher v2.2 (All Sources) ---")
    
    # 1. Google Trends (API)
    g_trends = fetch_rising_queries(KEYWORDS)
    
    # 2. Google Autocomplete
    g_search = fetch_google_suggestions(KEYWORDS)
    
    # 3. Reddit
    reddit = fetch_reddit_trends(REDDIT_SUBREDDITS)
    
    all_topics = g_trends + g_search + reddit
    
    if all_topics:
        unique_topics = {t['query']: t for t in all_topics}.values()
        print("--- FETCHED TOPICS ---")
        for t in unique_topics:
            print(t)
        print("----------------------")
        update_topic_pool(unique_topics)
        print("\n✅ Done! Check 'Operations/Topic Pool.md'")
    else:
        print("\n⚠️ No trending topics found.")

if __name__ == "__main__":
    main()
