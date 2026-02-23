import requests
from lxml import html

url = "https://news.ycombinator.com"
response = requests.get(url)

data = html.fromstring(response.content)

title = data.find(".//title").text
print(f"Page Title: {title}\n")

links = data.xpath("//a")

for link in links[:5]:
    print(f"Text: {link.text_content()}")
    print(f"Href: {link.get('href')}")

titlelines = data.xpath("//span[@class='titleline']/a")

for title in titlelines[:5]:
    print(title.text)