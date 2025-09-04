import requests

wiki_link = None

def set_wiki_link(link):
    global wiki_link
    wiki_link = link

if __name__ == "__main__":
    set_wiki_link(input("Enter the wiki link: "))
    print(f"The wiki link is: {wiki_link}")