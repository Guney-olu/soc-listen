# Reddit Data Analysis and Engagement Tool
This project is designed to fetch and analyze Reddit data, store it in a vector database, generate categorized summaries, and identify high-engagement posts for targeted posting. The workflow includes data collection, storage, querying, and reporting using advanced AI models and vector databases.

**to download model !wget "https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF/resolve/main/zephyr-7b-beta.Q4_K_M.gguf"**

ALSO GIVE PATH IMN THE INIT_LLM.py in the model intialization

```bash
pip install -r requirements.txt
```

**SET UP YOUR ENV AND RAPID API KEYS**

```bash
pip install -r requirements.txt
```

**Check the file to give the specific inputs liek subreddit**

```bash
python3 main.py
```


## Project Components

### 1. Subreddit Identification and Data Collection

**File:** `post_scrape.py`

This module fetches posts from a specified subreddit and collects top comments. It uses a proxy server to bypass potential restrictions.

## 2. Data Storage and Querying

This module handles loading JSON data and adding documents to a vector database. It uses Chroma from LangChain for vector storage

## 3. Reporting on Top Problems, Pros, and Cons, Companies

**File:** `Init_llm.py`

This module generates categorized summaries from the text data using an LLM. The generate_categorized_summary function processes text to identify problems, pros, cons, and companies mentioned.

## 4. Identifying High-Engagement Posts for Targeted Posting

**File:** `trend_scape.py`

This module identifies top engaged posts from a subreddit and formats them for targeted engagement based on various metrics

