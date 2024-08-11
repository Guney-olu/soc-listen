"""
We are using social miner reddit api to get the post id's
and then using https://rapidapi.com/SeasonedCode/api/reddapi to get the comments
"""
import requests
from dotenv import load_dotenv
import os

load_dotenv()

X_RapidAPI_Key = os.getenv("X_RapidAPI_Key")

# Function to fetch post IDs
def fetch_post_ids(subreddit):
    url = "https://reddapi.p.rapidapi.com/api/getTopPostsBySubreddit"
    
    querystring = {
        "subreddit": subreddit,
        "time": "year"
    }
    
    headers = {
        "X-RapidAPI-Key": X_RapidAPI_Key,
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        post_ids = [post['id'] for post in data['data']['posts']]
        return post_ids
    else:
        print(f"Failed to fetch post IDs: {response.status_code}")
        return []

# Function to get top comments for a post
def get_top_comments(post_url, proxy, comments_num=2):
    url = "https://reddapi.p.rapidapi.com/api/scrape_post_comments"
    
    querystring = {
        "proxy": proxy,
        "post_url": post_url,
        "comments_num": str(comments_num)
    }
    
    headers = {
        "X-RapidAPI-Key": X_RapidAPI_Key,
        "X-RapidAPI-Host": "reddapi.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get comments for {post_url}: {response.status_code}")
        return None

def fetch(subreddit, proxy, num_posts=100, comments_num=2):
    """
    Fetch top comments from Reddit posts in a specific subreddit.
    
    :param subreddit: Name of the subreddit.
    :param proxy: Proxy server to use for fetching data.
    :param num_posts: Number of posts to fetch comments from.
    :param comments_num: Number of top comments to fetch per post.
    :return: A dictionary where keys are post URLs and values are lists of comments.
    """
    post_ids = fetch_post_ids(subreddit)
    
    comments_dict = {}

    for post_id in post_ids[:num_posts]:  
        post_url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}"
        comments = get_top_comments(post_url, proxy, comments_num)
        if comments:
            comments_dict[post_url] = comments

    return comments_dict
