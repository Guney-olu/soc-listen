"""
It fetches and displays the top posts from a specified subreddit 
based on their upvote ratio
Using the upvote ratio is better than counting upvotes and downvotes
"""

import requests
from datetime import datetime
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

X_RapidAPI_Key = os.getenv("X_RapidAPI_Key")

def fetch_engaged_posts(subreddit, top_n=5, time_filter='month'):
    url = "https://reddit34.p.rapidapi.com/getTopPostsBySubreddit"
    querystring = {
        "subreddit": subreddit,
        "time": time_filter
    }

    headers = {
        "x-rapidapi-key": X_RapidAPI_Key,
        "x-rapidapi-host": "reddit34.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('posts', [])
        sorted_posts = sorted(data, key=lambda x: (x['created'], x['upvoteRatio'], x['numComments']), reverse=True)
        return sorted_posts[:top_n]
    else:
        print(f"Failed to fetch posts: {response.status_code}")
        return []



def generate_llm_prompt(posts):
    prompt_template_str = """For each of the following posts, provide a rationale for why it is suitable for targeted engagement based on the title, upvote ratio, number of comments, and the subreddit:

{posts}

Format:
Post: "{title}" ({subreddit})
Rationale : 
"""

    post_details = []
    for post in posts:
        try:
            title = post.get("title", "No Title")
            subreddit = post.get("belongsTo", {}).get("id", "Unknown Subreddit")
            upvote_ratio = post.get("upvoteRatio", "Unknown")
            num_comments = post.get("numComments", "Unknown")
            created_timestamp = post.get("created", 0)
            created_date = datetime.fromtimestamp(created_timestamp / 1000).strftime("%Y-%m-%d %H:%M:%S")
            
            # Format each post detail string
            detail = f'Post: "{title}" (r/{subreddit})\nUpvote Ratio: {upvote_ratio}, Number of Comments: {num_comments}, Created: {created_date}'
            post_details.append(detail)
        except Exception as e:
            print(f"Skipping post due to unexpected error: {e}")

    post_details_str = "\n\n".join(post_details)

    return f"For each of the following posts, provide a rationale for why it is suitable for targeted engagement based on the title, upvote ratio, number of comments, and the subreddit:\n\n{post_details_str}\n\nFormat:\nPost: \"{title}\" ({subreddit})\nRationale: "


def identify_top_engaged_posts(subreddit, top_n=5, time_filter='year'):
    posts = fetch_engaged_posts(subreddit, top_n, time_filter)
    llm_prompt = generate_llm_prompt(posts)
    return llm_prompt


#SAMPLE USAGE
# subreddit = "technology"
# llm_prompt = identify_top_engaged_posts(subreddit)
# print(llm_prompt)
