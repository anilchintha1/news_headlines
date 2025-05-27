import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = []
        # NPR headlines are inside <h2> tags with class "title"
        for h2 in soup.find_all('h2', class_='title'):
            a_tag = h2.find('a')
            if a_tag:
                title = a_tag.text.strip()
                link = a_tag['href']
                headlines.append((title, link))

        return headlines

    except Exception as e:
        print(f"Error fetching headlines: {e}")
        return []

def save_headlines(headlines, filename='headlines.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for title, link in headlines:
            f.write(f"{title}\n{link}\n\n")

def main():
    url = 'https://www.npr.org/sections/news/'
    headlines = fetch_headlines(url)
    if headlines:
        print("Latest Headlines:")
        for idx, (title, link) in enumerate(headlines[:10], start=1):
            print(f"{idx}. {title}\n   {link}\n")
        save_headlines(headlines[:10])
        print(f"Top 10 headlines saved to headlines.txt")
    else:
        print("No headlines found.")

if __name__ == "__main__":
    main()
