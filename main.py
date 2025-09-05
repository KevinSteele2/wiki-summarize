import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt_tab')

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
    elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])
    text = "\n".join([el.get_text() for el in elements])
    return text

def summarize_text(text, num_sentences=3): 
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LuhnSummarizer(Stemmer("english"))
    summarizer.stop_words = get_stop_words("english")

    summary = summarizer(parser.document, num_sentences)
    return summary

if __name__ == "__main__":
    set_wiki_link(input("Enter the wiki link: "))
    print(f"The wiki link is: {wiki_link}")
    text = fetch_wiki_content()
    text = parse_wiki_content(text)
    summary = summarize_text(text, 3)
    print(summary)
