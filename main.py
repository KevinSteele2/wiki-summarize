import requests
from bs4 import BeautifulSoup
from transformers import pipeline

wiki_link = None

def set_wiki_link(link):
    global wiki_link
    wiki_link = link

def fetch_wiki_content():

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyWikipediaBot/1.0; +https://example.com/bot)"
    }

    if wiki_link is None:
        raise ValueError("Wiki link is not set.")

    r = requests.get(wiki_link, headers=headers)
    if r.status_code == 200:
        return r.text
    else:
        raise Exception(f"Failed to fetch content from {wiki_link}, status code: {r.status_code}")
    
def parse_wiki_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(['p'])
    text = "\n".join([el.get_text() for el in elements])
    return text

def summarize_text(text, max_length=130, min_length=30):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    text = text[:1024]
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary

if __name__ == "__main__":
    set_wiki_link(input("Enter the wiki link: "))
    print(f"The wiki link is: {wiki_link}")
    text = fetch_wiki_content()
    text = parse_wiki_content(text)
    summary = summarize_text(text, 130, 30)
    print(summary)
