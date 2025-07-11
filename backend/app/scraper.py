import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(topic: str) -> str:
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url)
    
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    return "\n".join([p.get_text() for p in paragraphs [:5]])


