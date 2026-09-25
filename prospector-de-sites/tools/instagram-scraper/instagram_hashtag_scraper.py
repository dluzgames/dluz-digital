"""
Instagram Hashtag Scraper
Extract posts, engagement data, and trending content from any public Instagram
hashtag page using the Crawlbase 'instagram-hashtag' scraper.

Blog reference: https://crawlbase.com/blog/how-to-scrape-instagram-data-using-python/
"""

from crawlbase import CrawlingAPI
import json

# Set your Crawlbase token
crawlbase_token = 'YOUR_CRAWLBASE_TOKEN'

# URL of the Instagram hashtag page to scrape
instagram_hashtag_url = 'https://www.instagram.com/explore/tags/love/'

# Options for Crawling API — use the instagram-hashtag scraper
options = {
    'scraper': 'instagram-hashtag',
}

# Create a Crawlbase API instance with your token
api = CrawlingAPI({'token': crawlbase_token})

try:
    # Send a GET request to crawl the URL with options
    response = api.get(instagram_hashtag_url, options=options)

    # Check if the response status code is 200 (OK)
    if response.get('statusCode', 0) == 200:
        # Parse the JSON response
        response_body_json = response.get('body', {})
        data = json.loads(response_body_json) if isinstance(response_body_json, str) else response_body_json

        # Display hashtag overview
        print("=" * 45)
        print("         INSTAGRAM HASHTAG DATA")
        print("=" * 45)

        print(f"\nHashtag     : {data.get('hashtag', 'N/A')}")
        posts_count = data.get('postsCount', 0)
        print(f"Total Posts : {posts_count:,}")

        # Open Stories under hashtag
        stories = data.get('openStories', [])
        if stories:
            print(f"Stories     : {len(stories)} active")

        # Posts
        posts = data.get('posts', [])
        if posts:
            print(f"\n=== Posts Found: {len(posts)} ===")

            # Engagement stats
            total_likes = sum(p.get('likeCount', 0) for p in posts)
            total_comments = sum(p.get('commentCount', 0) for p in posts)
            avg_likes = total_likes // len(posts) if posts else 0
            avg_comments = total_comments // len(posts) if posts else 0

            print(f"\nEngagement Summary:")
            print(f"  Avg Likes    : {avg_likes:,}")
            print(f"  Avg Comments : {avg_comments:,}")
            print(f"  Total Likes  : {total_likes:,}")

            # Top posts by likes
            top_posts = sorted(posts, key=lambda x: x.get('likeCount', 0), reverse=True)[:5]
            print(f"\n=== Top 5 Posts by Likes ===")
            for i, post in enumerate(top_posts, 1):
                print(f"\n  {i}. {post.get('link', 'N/A')}")
                print(f"     Likes    : {post.get('likeCount', 0):,}")
                print(f"     Comments : {post.get('commentCount', 0):,}")
                print(f"     Posted   : {post.get('takenAt', 'N/A')}")
                caption = post.get('caption', '')
                if caption:
                    print(f"     Caption  : {caption[:80]}...")

            # Video vs photo breakdown
            videos = [p for p in posts if p.get('isVideo')]
            photos = [p for p in posts if not p.get('isVideo')]
            print(f"\nContent Breakdown:")
            print(f"  Photos : {len(photos)}")
            print(f"  Videos : {len(videos)}")

        # Save full data to JSON file
        with open('hashtag_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("\n✓ Full hashtag data saved to hashtag_data.json")

    else:
        print(f"Request failed with status code: {response.get('statusCode', 0)}")

except Exception as e:
    print(f"API request error: {str(e)}")
