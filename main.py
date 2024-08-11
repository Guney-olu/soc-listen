"""
We are not using subreddit directly it require a diff llm or try test method or paid api's which is waste of time
but can be added anytime
"""



#1. Subreddit Identification and Data Collection
from post_scrape import fetch

subreddit = input("Enter the subreddit: ")
proxy = "157.230.188.193:3128"  # Get it from https://free-proxy-list.net
output  =  fetch(subreddit, proxy)


#2. Data Storage and Querying

from vdb_save import load_json_file,add_documents_to_vector_store

json_file_path = '/Users/aryanrajpurohit/stream/soc-listen/data.json' 
json_data = load_json_file(json_file_path)

add_documents_to_vector_store(json_data, vector_store)


#3. Reporting on Top Problems, Pros, and Cons, Companies 

from Init_llm import generate_categorized_summary
from vdb_save import vector_store

results = vector_store.similarity_search(
    "the toothbrush is verybad",
    k=2,
    filter={"metatag": "feedback"},
)
for res in results:
    input_text = f"Page Content: {res.page_content} | Metadata: {res.metadata}"


# IT WILL LOOK LIKE BELOW -||-

# input_text = """
# Just in case you’re concerned you won’t be able to get a $200+ smart toothbrush, you will soon to be able to get a $400 AI powered toothbrush.
# Meanwhile, Oral-B is pushing its latest toothbrush to capitalize on the latest AI tech trend. Without real detail, Oral-B claims its new $400 toothbrush has "A.I. position detection that tracks where you brush across all 3 surfaces of your teeth.” Like many, I'm skeptical about the toothbrush’s incorporation of actual AI; notably, P&G declined to comment to The Washington Post on what, exactly, makes the toothbrush "AI."
# This is the future we dreamed about as children manifesting before our very own eyes!
# What, exactly, makes the toothbrush "AI." The brush is so sharp and hard, you'll scream "AÏ!" when you use it.
# OMG this is like the days when manufactures wanted to say their machines they produced like toasters and refrigerators were internet connected as a marketing point rather than a truly practical use.
# Yeah I never thought “I wish my toothbrush had an app, imagine all the cool stuff my toothbrush could do if I could control it via app using WiFi!” Imagine being an app developer and your job was to build out a platform for a toothbrush. I would quiet quit so hard on that shit lol.
# I have a toothbrush with built-in WiFi. It connects to an app supposedly, but WTF would I need to track, much less let the world track, how and when I brush my teeth?
# 2026: Mr Observe. I'm afraid your dental insurance will not cover your claim for dentures since you only brushed below average frequency and were inconsistent.
# """

summary = generate_categorized_summary(input_text)
print("Summary:", summary)


#4. Identifying High-Engagement Posts for Targeted Posting

from trend_scape import identify_top_engaged_posts
from Init_llm import model
subreddit = "technology" #name of the subreddit
llm_prompt = identify_top_engaged_posts(subreddit)
result = model(llm_prompt)
