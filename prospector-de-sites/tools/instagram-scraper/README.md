<a href="https://crawlbase.com/signup?utm_source=github&utm_medium=readme&utm_campaign=instagram_scraper" target="_blank">
  <img src="https://github.com/user-attachments/assets/afa4f6e7-25fb-442c-af2f-b4ddcfd62ab2"
       alt="Crawlbase - Scrape Instagram Without Getting Blocked"
       style="max-width: 100%; border: 0;">
</a>

# How to Scrape Instagram Data Using Python

A complete guide and working code to scrape Instagram profiles, posts, and hashtags using the [Crawlbase Crawling API](https://crawlbase.com/docs/crawling-api/). Extract public Instagram data at scale without getting blocked.

[![Language](https://img.shields.io/badge/language-Python-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Crawlbase](https://img.shields.io/badge/powered%20by-Crawlbase-orange)](https://crawlbase.com)

## 📖 Table of Contents

- [Why Scrape Instagram Data?](#-why-scrape-instagram-data)
- [Getting Started](#-getting-started)
- [Basic Scraping with Crawlbase](#-basic-scraping-with-crawlbase)
- [instagram-post Scraper](#-instagram-post-scraper)
- [instagram-profile Scraper](#-instagram-profile-scraper)
- [instagram-hashtag Scraper](#-instagram-hashtag-scraper)
- [Overcoming Anti-Scraping Challenges](#-overcoming-anti-scraping-challenges)
- [Project Structure](#-project-structure)
- [FAQ](#-frequently-asked-questions)

---

## 💡 Why Scrape Instagram Data?

Instagram, with over **2 billion active accounts**, is a goldmine of public data. Here's what you can do with it:

1. **Market Research** — Understand audience preferences, behaviors, and trends from profiles, posts, and comments
2. **Competitor Analysis** — Study competitors' content strategies, post frequency, and engagement
3. **Influencer Marketing** — Evaluate influencer profiles for engagement rates and audience relevance before hiring
4. **Content Strategy** — Discover what content performs best in your niche
5. **Social Media Analytics** — Track follower growth, post reach, and engagement over time
6. **Lead Generation** — Identify ideal customers based on interests and activity
7. **Trend Analysis** — Monitor viral content and emerging hashtags
8. **Academic Research** — Gather social data for research and experiments

---

## 🚦 Getting Started

### Prerequisites

- Python 3.7+
- A free Crawlbase account — [Sign up here](https://crawlbase.com/signup) (first 1,000 requests free, no credit card needed)

### Step 1 — Install the Crawlbase Library

```bash
pip install crawlbase
```

### Step 2 — Get Your API Token

After signing up, get your token from the [Crawlbase dashboard](https://crawlbase.com/dashboard/account/docs).

### Step 3 — Create Your Scraper File

```bash
touch instagram_scraper.py
```

---

## 🔰 Basic Scraping with Crawlbase

The simplest usage — fetch the raw HTML of any Instagram page:

```python
from crawlbase import CrawlingAPI

# Set your Crawlbase token
crawlbase_token = 'YOUR_CRAWLBASE_TOKEN'

# URL of the Instagram page to scrape
instagram_page_url = 'https://www.instagram.com/apple/'

# Create a Crawlbase API instance with your token
api = CrawlingAPI({'token': crawlbase_token})

try:
    # Send a GET request to crawl the URL
    response = api.get(instagram_page_url)

    # Check if the response status code is 200 (OK)
    if 'status_code' in response:
        if response['status_code'] == 200:
            # Print the response body
            print(response['body'])
        else:
            print(f"Request failed with status code: {response['status_code']}")
    else:
        print("Response does not contain a status code.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
```

This returns the raw HTML of the Instagram page. For structured JSON data, use the dedicated scrapers below.

---

## 📸 `instagram-post` Scraper

Extract structured data from any Instagram post — likes, comments, captions, media, tags, and more.

```python
from crawlbase import CrawlingAPI

crawlbase_token = 'YOUR_CRAWLBASE_TOKEN'
instagram_post_url = 'https://www.instagram.com/p/B5LQhLiFFCX'

options = {
    'scraper': 'instagram-post',
}

api = CrawlingAPI({'token': crawlbase_token})

try:
    response = api.get(instagram_post_url, options=options)

    if response.get('statusCode', 0) == 200:
        response_body_json = response.get('body', {})
        print(response_body_json)
    else:
        print(f"Request failed with status code: {response.get('statusCode', 0)}")

except Exception as e:
    print(f"API request error: {str(e)}")
```

### Example JSON Response

```json
{
  "postedBy": {
    "accountName": "apple",
    "accountUserName": "apple",
    "accountLink": "https://www.instagram.com/apple/"
  },
  "postLocation": {
    "locationName": "Cheonan, Korea",
    "link": "https://www.instagram.com/explore/locations/236722267/cheonan-korea/"
  },
  "caption": {
    "text": "\"Nature can be a designer.\" #landscapephotography #ShotoniPhone by Chang D.",
    "tags": [
      {
        "hashtag": "#landscapephotography",
        "link": "https://www.instagram.com/explore/tags/landscapephotography/"
      },
      {
        "hashtag": "#ShotoniPhone",
        "link": "https://www.instagram.com/explore/tags/shotoniphone/"
      }
    ]
  },
  "media": {
    "images": [
      "https://instagram.fccu1-1.fna.fbcdn.net/..."
    ],
    "videos": []
  },
  "likesCount": 373174,
  "viewsCount": 0,
  "dateTime": "2019-11-22T17:21:42.000Z",
  "repliesCount": 12,
  "replies": [
    {
      "accountUserName": "user123",
      "accountLink": "https://www.instagram.com/user123/",
      "text": "Beautiful shot!",
      "likesCount": 0,
      "dateTime": "2020-03-26T05:48:15.000Z"
    }
  ]
}
```

---

## 👤 `instagram-profile` Scraper

Extract full profile data — follower counts, bio, posts, stories, and IGTV content.

```python
from crawlbase import CrawlingAPI

crawlbase_token = 'YOUR_CRAWLBASE_TOKEN'
instagram_profile_url = 'https://www.instagram.com/apple/'

options = {
    'scraper': 'instagram-profile',
}

api = CrawlingAPI({'token': crawlbase_token})

try:
    response = api.get(instagram_profile_url, options=options)

    if response.get('statusCode', 0) == 200:
        response_body_json = response.get('body', {})
        print(response_body_json)
    else:
        print(f"Request failed with status code: {response.get('statusCode', 0)}")

except Exception as e:
    print(f"API request error: {str(e)}")
```

### Example JSON Response

```json
{
  "username": "apple",
  "verified": true,
  "postsCount": {
    "value": "645",
    "text": "645"
  },
  "followersCount": {
    "value": "23,226,349",
    "text": "23.2m"
  },
  "followingCount": {
    "value": "6",
    "text": "6"
  },
  "name": "apple",
  "bio": {
    "text": "Everyone has a story to tell. Tag #ShotoniPhone to take part.",
    "tags": [
      {
        "hashtag": "#ShotoniPhone",
        "link": "https://www.instagram.com/explore/tags/shotoniphone/"
      }
    ]
  },
  "posts": [
    {
      "link": "https://www.instagram.com/p/B_XxvQvlsGe/",
      "image": "https://scontent-ams4-1.cdninstagram.com/...",
      "imageData": "Photo by apple on April 24, 2020."
    }
  ],
  "igtvs": [
    {
      "link": "https://www.instagram.com/tv/B9ex0TSlMCg/",
      "caption": "Shifting Perspectives",
      "duration": "1:44"
    }
  ]
}
```

---

## #️⃣ `instagram-hashtag` Scraper

Extract posts, engagement metrics, and trending content from any public Instagram hashtag page.

```python
from crawlbase import CrawlingAPI

crawlbase_token = 'YOUR_CRAWLBASE_TOKEN'
instagram_hashtag_url = 'https://www.instagram.com/explore/tags/love/'

options = {
    'scraper': 'instagram-hashtag',
}

api = CrawlingAPI({'token': crawlbase_token})

try:
    response = api.get(instagram_hashtag_url, options=options)

    if response.get('statusCode', 0) == 200:
        response_body_json = response.get('body', {})
        print(response_body_json)
    else:
        print(f"Request failed with status code: {response.get('statusCode', 0)}")

except Exception as e:
    print(f"API request error: {str(e)}")
```

### Example JSON Response

```json
{
  "hashtag": "#love",
  "postsCount": 1922533116,
  "posts": [
    {
      "link": "https://www.instagram.com/p/CFr2LTkDGAL",
      "shortcode": "CFr2LTkDGAL",
      "caption": "Serious.\n#fitness #gym #love #lifestyle...",
      "commentCount": 20,
      "likeCount": 633,
      "takenAt": "2020-09-28T15:23:11.000+00:00",
      "isVideo": false
    }
  ]
}
```

---

## 🛡️ Overcoming Anti-Scraping Challenges

### Instagram's Anti-Scraping Mechanisms

Instagram employs several layers of protection:

- **Rate Limiting** — Restricts the number of requests per time window; exceeding limits results in temporary or permanent blocks
- **CAPTCHA** — Triggers during login or suspicious browsing activity
- **Dynamic Content** — Pages are frequently updated, breaking selector-based scrapers
- **Session Cookies** — Tracks user behavior and flags sudden pattern changes
- **User-Agent Checks** — Suspicious UA strings trigger detection

### Strategies to Avoid Detection

| Strategy | Description |
|----------|-------------|
| **Use Rotating Proxies** | Distribute requests across multiple IPs to avoid rate limits |
| **Randomize User Agents** | Rotate UA strings to mimic different browsers and devices |
| **Session Management** | Maintain consistent sessions rather than creating new ones repeatedly |
| **Limit Request Frequency** | Add random delays between requests to mimic human behavior |
| **Simulate Human Behavior** | Scroll, click, and interact naturally rather than hammering endpoints |
| **Scrape Off-Peak Hours** | Less server load means fewer CAPTCHAs and rate limit triggers |
| **Respect robots.txt** | Check Instagram's scraping guidelines and adhere to them |
| **Use Headless Browsers** | Tools like Selenium render JavaScript for a more authentic experience |

> **Tip:** Crawlbase handles all of these automatically — proxies, CAPTCHAs, rate limiting, and JS rendering are built in, so you can focus on the data.

---

## 📁 Project Structure

```
instagram-scraper/
├── README.md
├── LICENSE
├── .gitignore
├── .gitattributes
├── requirements.txt
└── examples/
    ├── instagram_page_scraper.py     # Raw HTML scraping
    ├── instagram_post_scraper.py     # Structured post data
    ├── instagram_profile_scraper.py  # Full profile extraction
    └── instagram_hashtag_scraper.py  # Hashtag page scraping
```

---

## ❓ Frequently Asked Questions

### What is an Instagram Scraper?
An Instagram scraper is a tool that automates collecting public data from Instagram — including profiles, posts, comments, hashtags, and engagement metrics — without manual browsing.

### Is it legal to scrape Instagram?
Scraping is legal when limited to publicly accessible data (images, captions, likes, follower counts). Avoid scraping private information or violating copyright. Always comply with Instagram's terms of service and applicable data protection laws like GDPR.

### What types of data can be scraped from Instagram?
- **User Profiles** — username, bio, follower/following counts, post count
- **Posts** — captions, images, videos, hashtags, likes, comments
- **Comments** — text, timestamps, usernames
- **Hashtags** — post count, trending posts under a tag
- **Stories** — public story content
- **IGTV** — video titles and durations
- **Location Data** — geotags on public posts

### What are the ethical considerations?
Respect user privacy, obtain consent where required, avoid collecting personal contact details, and use scraped data responsibly. Responsible scraping means not using data for spam, harassment, or re-selling personal information.

### What are practical use cases for scraped Instagram data?
- Social media marketing optimization
- Influencer discovery and vetting
- Competitor content analysis
- Brand sentiment monitoring
- Trend identification and reporting
- Market research and academic studies

---

## 📚 Resources

- [Crawlbase Crawling API Docs](https://crawlbase.com/docs/crawling-api/)
- [Instagram Scraper Reference](https://crawlbase.com/docs/crawling-api/scrapers/#instagram)
- [Full Blog Post: How to Scrape Instagram Data Using Python](https://crawlbase.com/blog/how-to-scrape-instagram-data-using-python/)
- [Crawlbase Pricing](https://crawlbase.com/pricing)

## 🤝 Support

- **Email**: support@crawlbase.com
- **Docs**: [crawlbase.com/docs](https://crawlbase.com/docs)
- **Status**: [status.crawlbase.com](https://status.crawlbase.com)

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Start scraping today!** [Create a free Crawlbase account](https://crawlbase.com/signup) — no credit card required, first 1,000 requests are on us.
