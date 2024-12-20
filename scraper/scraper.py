import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape title and description for Amazon product pages
        if "amazon" in url:
            title = soup.find("span", {"id": "productTitle"}).get_text(strip=True)
            description = soup.find("div", {"id": "feature-bullets"}).get_text(strip=True)
            return f"{title}. {description}"

        # Default scraping logic for other pages
        content = ' '.join(p.text for p in soup.find_all('p') if p.text.strip())
        return content

    except Exception as e:
        print(f"Error while scraping URL: {e}")
        return None

