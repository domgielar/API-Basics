import requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com/"

response = requests.get(url)
print(response)

html_content=response.text

soup = BeautifulSoup(html_content, 'html.parser')

print(html_content[:500])

links = soup.find_all("a")

for link in links:
    print(link.text)