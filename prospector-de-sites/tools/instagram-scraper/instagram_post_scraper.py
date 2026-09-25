"""
Instagram Post Scraper
Extract structured JSON data from any public Instagram post using the
Crawlbase 'instagram-post' scraper — likes, comments, captions, media, and more.

Blog reference: https://crawlbase.com/blog/how-to-scrape-instagram-data-using-python/
"""

from crawlbase import CrawlingAPI
import json

# Set your Crawlbase token
crawlbase_token = 'YOUR_CRAWLBASE_TOKEN'

# URL of the Instagram post to scrape
instagram_post_url = 'https://www.instagram.com/p/B5LQhLiFFCX'

# Options for Crawling API — use the instagram-post scraper
options = {
    'scraper': 'instagram-post',
}

# Create a Crawlbase API instance with your token
api = CrawlingAPI({'token': crawlbase_token})

try:
    # Send a GET request to crawl the URL with options
    response = api.get(instagram_post_url, options=options)

    # Check if the response status code is 200 (OK)
    if response.get('statusCode', 0) == 200:
        # Parse the JSON response
        response_body_json = response.get('body', {})
        data = json.loads(response_body_json) if isinstance(response_body_json, str) else response_body_json

        # Display key post information
        print("=== Post Details ===")
        posted_by = data.get('postedBy', {})
        print(f"Posted by : @{posted_by.get('accountUserName', 'N/A')}")
        print(f"Profile   : {posted_by.get('accountLink', 'N/A')}")

        location = data.get('postLocation', {})
        if location:
            print(f"Location  : {location.get('locationName', 'N/A')}")

        caption = data.get('caption', {})
        print(f"\nCaption   : {caption.get('text', 'N/A')}")

        tags = caption.get('tags', [])
        if tags:
            hashtags = [t.get('hashtag') for t in tags if t.get('hashtag')]
            print(f"Hashtags  : {', '.join(hashtags)}")

        print(f"\nLikes     : {data.get('likesCount', 0):,}")
        print(f"Comments  : {data.get('repliesCount', 0):,}")
        print(f"Date      : {data.get('dateTime', 'N/A')}")

        media = data.get('media', {})
        print(f"\nImages    : {len(media.get('images', []))}")
        print(f"Videos    : {len(media.get('videos', []))}")

        replies = data.get('replies', [])
        if replies:
            print(f"\n=== Top Comments ({len(replies)} total) ===")
            for reply in replies[:3]:
                print(f"  @{reply.get('accountUserName')}: {reply.get('text', '')[:80]}")

        # Save full data to JSON file
        with open('post_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("\n✓ Full post data saved to post_data.json")

    else:
        print(f"Request failed with status code: {response.get('statusCode', 0)}")

except Exception as e:
    print(f"API request error: {str(e)}")
