import requests

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

if __name__ == "__main__":
    set_wiki_link(input("Enter the wiki link: "))
    print(f"The wiki link is: {wiki_link}")
    text = fetch_wiki_content()
    print(text)
