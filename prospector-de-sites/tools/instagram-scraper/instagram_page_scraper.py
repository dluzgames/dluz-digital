"""
Instagram Page Scraper
Scrape raw HTML from any public Instagram page using Crawlbase Crawling API.

Blog reference: https://crawlbase.com/blog/how-to-scrape-instagram-data-using-python/
"""

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
            # Print the response body (raw HTML)
            print(response['body'])
        else:
            print(f"Request failed with status code: {response['status_code']}")
    else:
        print("Response does not contain a status code.")

except Exception as e:
    # Handle any exceptions or errors
    print(f"An error occurred: {str(e)}")
