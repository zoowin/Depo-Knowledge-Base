"""
Depology Trend Fetcher v3.0
===========================
Fetches skincare trends from Google Trends, Google Autocomplete, and Reddit.
Outputs to strategy/topic-pool.md with deduplication and relevance filtering.

Usage:
    python fetch_trends.py                  # Full run (all sources)
    python fetch_trends.py --google-only    # Google sources only
    python fetch_trends.py --reddit-only    # Reddit only
    python fetch_trends.py --dry-run        # Preview without writing to file
"""

import os
import sys
import time
import json
import html
import re
import argparse
import xml.etree.ElementTree as ET
from datetime import datetime

import requests

# --- Configuration ---
KEYWORDS = [
    "skincare", "anti-aging", "retinol", "k-beauty",
    "wrinkle treatment", "eye cream", "peptide serum",
    "collagen serum", "micro-needling", "niacinamide"
]

REDDIT_SUBREDDITS = [
    "SkincareAddiction",
    "30PlusSkinCare",
    "AsianBeauty",
    "antiaging",
]

# Relevance keywords — Reddit posts must match at least one to be included
RELEVANCE_KEYWORDS = [
    "anti-aging", "anti aging", "antiaging", "wrinkle", "fine line",
    "peptide", "retinol", "retinal", "retinoid", "collagen",
    "serum", "cream", "moisturizer", "eye cream", "dark circle",
    "k-beauty", "korean", "skincare routine", "skin barrier",
    "hyaluronic", "niacinamide", "vitamin c", "aha", "bha",
    "exfoliat", "microneedling", "micro-needling", "micro needle",
    "botox", "filler", "needle-free", "notox", "no-tox",
    "argireline", "matrixyl", "ceramide", "cica",
    "aging", "mature skin", "sagging", "firming", "lifting",
    "glow", "brightening", "hyperpigmentation", "dark spot",
    "spf", "sunscreen", "sun damage", "photoaging",
    "skin cycling", "slugging", "skin streaming", "glass skin",
]

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
TOPIC_POOL_PATH = os.path.join(BASE_DIR, "strategy", "topic-pool.md")


# =============================================================================
# Utility Functions
# =============================================================================

def load_existing_topics(file_path):
    """Read existing topic pool and extract all topic titles for deduplication."""
    existing = set()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                # Extract text between ** ** markers
                matches = re.findall(r'\*\*(.*?)\*\*', line)
                for m in matches:
                    # Normalize: lowercase, strip prefixes
                    clean = m.lower().strip()
                    for prefix in ["trending: ", "search suggestion: ", "reddit: ",
                                   "community question: ", "viral on r/", "reddit is talking about: "]:
                        if clean.startswith(prefix):
                            clean = clean[len(prefix):]
                    existing.add(clean)
    return existing


def is_relevant(text, min_keywords=1):
    """Check if text contains enough relevance keywords."""
    text_lower = text.lower()
    count = sum(1 for kw in RELEVANCE_KEYWORDS if kw in text_lower)
    return count >= min_keywords


def clean_reddit_title(title):
    """Remove Reddit tags like [Misc], [B&A], [Humor] etc."""
    cleaned = re.sub(r'\[.*?\]\s*', '', title).strip()
    # Remove leading/trailing punctuation
    cleaned = cleaned.strip('.,!?:;-– ')
    return cleaned


def is_duplicate(new_topic, existing_topics):
    """Check if a topic already exists (fuzzy match)."""
    clean = new_topic.lower().strip()
    # Direct match
    if clean in existing_topics:
        return True
    # Check if any existing topic contains this one or vice versa
    for existing in existing_topics:
        if len(clean) > 10 and len(existing) > 10:
            if clean in existing or existing in clean:
                return True
    return False


# =============================================================================
# Google Trends (via pytrends)
# =============================================================================

def fetch_rising_queries(keywords):
    """Fetch rising queries from Google Trends API."""
    print("🔍 Fetching trends from Google Trends...")
    rising_topics = []

    try:
        from pytrends.request import TrendReq
        pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))
    except Exception as e:
        print(f"⚠️ Google Trends initialization failed: {e}")
        return []

    # Process keywords in batches of 5 (API limit)
    for i in range(0, len(keywords), 5):
        batch = keywords[i:i+5]
        try:
            pytrends.build_payload(batch, cat=0, timeframe='today 1-m', geo='US', gprop='')
            related_queries = pytrends.related_queries()

            for kw in batch:
                if related_queries.get(kw) and related_queries[kw]['rising'] is not None:
                    top_rising = related_queries[kw]['rising'].head(3)
                    for _, row in top_rising.iterrows():
                        query = row['query']
                        value = row['value']
                        if is_relevant(query):
                            rising_topics.append({
                                'source': 'Google Trends',
                                'keyword': kw,
                                'query': query.title(),
                                'trend': value
                            })
            time.sleep(2)  # Rate limiting

        except Exception as e:
            print(f"⚠️ Google Trends batch error ({batch}): {e}")
            time.sleep(5)

    print(f"   ✅ Found {len(rising_topics)} rising queries")
    return rising_topics


# =============================================================================
# Google Autocomplete
# =============================================================================

def fetch_google_suggestions(keywords):
    """Fetch autocomplete suggestions from Google Search."""
    print("🔍 Fetching Google Autocomplete suggestions...")
    suggestions = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    # More specific query prefixes for better results
    prefixes = ["best {kw} 2026", "{kw} for mature skin", "{kw} vs", "why {kw}"]

    for kw in keywords:
        queries = [kw] + [p.format(kw=kw) for p in prefixes]
        seen_in_kw = set()

        for query in queries:
            url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={query}"
            try:
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    if len(data) >= 2:
                        for suggestion in data[1]:
                            s_lower = suggestion.lower()
                            # Skip if too generic (same as keyword) or already seen
                            if s_lower == kw.lower() or s_lower in seen_in_kw:
                                continue
                            # Skip overly generic suggestions
                            if s_lower in ["skincare", "skincare routine", "anti-aging",
                                           "retinol", "eye cream", "k-beauty"]:
                                continue
                            if is_relevant(suggestion):
                                seen_in_kw.add(s_lower)
                                suggestions.append({
                                    'source': 'Google Search',
                                    'keyword': kw,
                                    'query': suggestion.title(),
                                    'trend': 'Popular Search'
                                })
                time.sleep(0.5)

            except Exception as e:
                print(f"   ⚠️ Autocomplete error for '{query}': {e}")

        # Limit per keyword to avoid flooding
        per_kw = [s for s in suggestions if s['keyword'] == kw]
        if len(per_kw) > 5:
            # Keep only the first 5 per keyword
            to_remove = per_kw[5:]
            suggestions = [s for s in suggestions if s not in to_remove]

    print(f"   ✅ Found {len(suggestions)} autocomplete suggestions")
    return suggestions


# =============================================================================
# Reddit
# =============================================================================

def fetch_reddit_trends(subreddits):
    """Fetch trending posts from Reddit via RSS feeds with relevance filtering.

    Note: Reddit's JSON API now requires OAuth. RSS feeds (.rss) remain publicly
    accessible and return Atom XML with post titles, links, and content previews.
    """
    print("🔍 Fetching Reddit trends (via RSS)...")
    reddit_topics = []

    headers = {
        'User-Agent': 'DepologyTrendBot/3.0 (skincare research)'
    }

    sort_modes = ['hot', 'top']  # RSS supports hot and top (not rising)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}

    for sub in subreddits:
        sub_topics = []
        for sort in sort_modes:
            # top?t=week for weekly top; hot for current trending
            t_param = "?t=week&limit=20" if sort == 'top' else "?limit=20"
            url = f"https://www.reddit.com/r/{sub}/{sort}/.rss{t_param}"

            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    root = ET.fromstring(response.text)
                    entries = root.findall('atom:entry', ns)

                    for entry in entries:
                        title_elem = entry.find('atom:title', ns)
                        content_elem = entry.find('atom:content', ns)

                        if title_elem is None:
                            continue

                        title = html.unescape(title_elem.text or '')
                        # Extract text preview from HTML content
                        content_text = ''
                        if content_elem is not None and content_elem.text:
                            # Strip HTML tags for relevance check
                            content_text = re.sub(r'<[^>]+>', ' ', html.unescape(content_elem.text))[:300]

                        # Clean the title
                        cleaned_title = clean_reddit_title(title)
                        if not cleaned_title or len(cleaned_title) < 15:
                            continue

                        # Skip stickied/meta posts
                        lower_title = title.lower()
                        if any(skip in lower_title for skip in [
                            'daily help thread', 'weekly thread', 'holy grail',
                            'mod post', 'rules reminder', 'megathread'
                        ]):
                            continue

                        # Relevance check on title + content preview
                        combined_text = f"{title} {content_text}"
                        if not is_relevant(combined_text):
                            continue

                        # Truncate display title
                        display_title = cleaned_title[:100] + "..." if len(cleaned_title) > 100 else cleaned_title

                        sub_topics.append({
                            'source': 'Reddit',
                            'keyword': sub,
                            'query': display_title,
                            'trend': f"r/{sub} · {sort}",
                        })

                elif response.status_code == 429:
                    print(f"   ⚠️ Rate limited on r/{sub}/{sort}, waiting...")
                    time.sleep(10)
                else:
                    print(f"   ⚠️ r/{sub}/{sort}: HTTP {response.status_code}")

                time.sleep(2)  # Be respectful

            except Exception as e:
                print(f"   ⚠️ Reddit RSS error r/{sub}/{sort}: {e}")

        # Deduplicate within subreddit
        seen_titles = set()
        unique_sub_topics = []
        for t in sub_topics:
            title_key = t['query'].lower()[:50]
            if title_key not in seen_titles:
                seen_titles.add(title_key)
                unique_sub_topics.append(t)

        reddit_topics.extend(unique_sub_topics[:8])  # Max 8 per subreddit

    print(f"   ✅ Found {len(reddit_topics)} relevant Reddit posts")
    return reddit_topics


# =============================================================================
# Format & Write
# =============================================================================

def format_topic(item):
    """Format a single topic item as markdown checkbox."""
    query = item['query']
    source = item['source']
    context = item['keyword']
    trend = item.get('trend', '')

    if source == 'Google Trends':
        trend_label = f", trend: {trend}" if trend else ""
        return f"- [ ] **{query}** (Google Trends · `{context}`{trend_label})"

    elif source == 'Google Search':
        return f"- [ ] **{query}** (Google Autocomplete · `{context}`)"

    elif source == 'Reddit':
        return f"- [ ] **{query}** ({trend})"

    return f"- [ ] **{query}** ({source})"


def update_topic_pool(new_topics, existing_topics, dry_run=False):
    """Append new topics to topic pool with deduplication."""
    if not os.path.exists(TOPIC_POOL_PATH):
        print(f"❌ Topic Pool not found at: {TOPIC_POOL_PATH}")
        return 0

    # Filter out duplicates
    unique_new = []
    for t in new_topics:
        if not is_duplicate(t['query'], existing_topics):
            unique_new.append(t)
            # Add to existing set to prevent intra-batch duplicates
            existing_topics.add(t['query'].lower())

    if not unique_new:
        print("ℹ️  No new unique topics found (all duplicates).")
        return 0

    # Group by source
    g_trends = [t for t in unique_new if t['source'] == 'Google Trends']
    g_search = [t for t in unique_new if t['source'] == 'Google Search']
    reddit = [t for t in unique_new if t['source'] == 'Reddit']

    timestamp = datetime.now().strftime("%Y-%m-%d")
    sources = []
    if g_trends: sources.append("Google Trends")
    if g_search: sources.append("Google Autocomplete")
    if reddit: sources.append("Reddit")

    lines = []
    lines.append(f"\n\n## 🌍 Auto-Fetched Trends ({timestamp})")
    lines.append(f"*Sources: {', '.join(sources)} · {len(unique_new)} new topics*\n")

    if g_trends:
        lines.append("### Google Trends (Rising Queries)")
        for topic in g_trends:
            lines.append(format_topic(topic))
        lines.append("")

    if g_search:
        lines.append("### Google Autocomplete")
        for topic in g_search:
            lines.append(format_topic(topic))
        lines.append("")

    if reddit:
        lines.append("### Reddit Discussions")
        for topic in reddit:
            lines.append(format_topic(topic))
        lines.append("")

    output = "\n".join(lines)

    if dry_run:
        print("\n--- DRY RUN OUTPUT ---")
        print(output)
        print("--- END DRY RUN ---")
    else:
        with open(TOPIC_POOL_PATH, "a", encoding="utf-8") as f:
            f.write(output)
        print(f"📝 Appended {len(unique_new)} new topics to topic-pool.md")

    return len(unique_new)


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Depology Trend Fetcher v3.0")
    parser.add_argument('--google-only', action='store_true', help='Only fetch Google sources')
    parser.add_argument('--reddit-only', action='store_true', help='Only fetch Reddit sources')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing to file')
    args = parser.parse_args()

    print("=" * 50)
    print("  Depology Trend Fetcher v3.0")
    print(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)

    # Load existing topics for deduplication
    print(f"\n📂 Loading existing topics from: {TOPIC_POOL_PATH}")
    existing = load_existing_topics(TOPIC_POOL_PATH)
    print(f"   Found {len(existing)} existing topic entries\n")

    all_topics = []

    if not args.reddit_only:
        # 1. Google Trends
        g_trends = fetch_rising_queries(KEYWORDS)
        all_topics.extend(g_trends)

        # 2. Google Autocomplete
        g_search = fetch_google_suggestions(KEYWORDS)
        all_topics.extend(g_search)

    if not args.google_only:
        # 3. Reddit
        reddit = fetch_reddit_trends(REDDIT_SUBREDDITS)
        all_topics.extend(reddit)

    # Summary
    print(f"\n📊 Total fetched: {len(all_topics)} topics")

    if all_topics:
        added = update_topic_pool(all_topics, existing, dry_run=args.dry_run)
        print(f"\n✅ Done! Added {added} new unique topics.")
    else:
        print("\n⚠️ No topics fetched from any source.")

    print("=" * 50)


if __name__ == "__main__":
    main()
