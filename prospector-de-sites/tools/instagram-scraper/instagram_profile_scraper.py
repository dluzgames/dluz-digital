"""
Instagram Profile Scraper
Extract full profile data from any public Instagram profile using the
Crawlbase 'instagram-profile' scraper — followers, bio, posts, stories, IGTV.

Blog reference: https://crawlbase.com/blog/how-to-scrape-instagram-data-using-python/
"""

from crawlbase import CrawlingAPI
import json

# Set your Crawlbase token
crawlbase_token = 'YOUR_CRAWLBASE_TOKEN'

# URL of the Instagram profile to scrape
instagram_profile_url = 'https://www.instagram.com/apple/'

# Options for Crawling API — use the instagram-profile scraper
options = {
    'scraper': 'instagram-profile',
}

# Create a Crawlbase API instance with your token
api = CrawlingAPI({'token': crawlbase_token})

try:
    # Send a GET request to crawl the URL with options
    response = api.get(instagram_profile_url, options=options)

    # Check if the response status code is 200 (OK)
    if response.get('statusCode', 0) == 200:
        # Parse the JSON response
        response_body_json = response.get('body', {})
        data = json.loads(response_body_json) if isinstance(response_body_json, str) else response_body_json

        # Display profile information
        print("=" * 45)
        print("         INSTAGRAM PROFILE DATA")
        print("=" * 45)

        print(f"\nUsername    : @{data.get('username', 'N/A')}")
        print(f"Name        : {data.get('name', 'N/A')}")
        print(f"Verified    : {'✓ Yes' if data.get('verified') else 'No'}")

        followers = data.get('followersCount', {})
        following = data.get('followingCount', {})
        posts = data.get('postsCount', {})

        print(f"\nFollowers   : {followers.get('text', 'N/A')} ({followers.get('value', 'N/A')})")
        print(f"Following   : {following.get('text', 'N/A')}")
        print(f"Posts       : {posts.get('text', 'N/A')}")

        bio = data.get('bio', {})
        if bio:
            print(f"\nBio         : {bio.get('text', 'N/A')}")
            bio_tags = bio.get('tags', [])
            if bio_tags:
                hashtags = [t.get('hashtag') for t in bio_tags if t.get('hashtag')]
                print(f"Bio Tags    : {', '.join(hashtags)}")

        # Open Stories
        stories = data.get('openStories', [])
        if stories:
            print(f"\nOpen Stories: {len(stories)} available")

        # Recent Posts
        recent_posts = data.get('posts', [])
        if recent_posts:
            print(f"\n=== Recent Posts ({len(recent_posts)} found) ===")
            for i, post in enumerate(recent_posts[:5], 1):
                print(f"  {i}. {post.get('link', 'N/A')}")
                if post.get('imageData'):
                    print(f"     {post['imageData'][:80]}...")

        # IGTV
        igtvs = data.get('igtvs', [])
        if igtvs:
            print(f"\n=== IGTV Videos ({len(igtvs)} found) ===")
            for igtv in igtvs:
                print(f"  • {igtv.get('caption', 'N/A')} ({igtv.get('duration', 'N/A')})")
                print(f"    {igtv.get('link', '')}")

        # Save full data to JSON file
        with open('profile_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("\n✓ Full profile data saved to profile_data.json")

    else:
        print(f"Request failed with status code: {response.get('statusCode', 0)}")

except Exception as e:
    print(f"API request error: {str(e)}")
