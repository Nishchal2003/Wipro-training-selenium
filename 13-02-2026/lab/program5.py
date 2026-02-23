'''Write a simple program to parse a small HTML string.
Given this HTML:
Extract the title text.
Extract the <h1> text.
Extract the paragraph text.
Write a program to:
Find the first <a> tag.
Print its href attribute.
'''

from bs4 import BeautifulSoup

html = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click Here</a>
  </body>
</html>
"""

soup = BeautifulSoup(html,"html.parser")

print(soup.title.text)
print(soup.h1.text)
print(soup.p.text)
print(soup.body.text)
print(soup.a.text)
link = soup.find("a")
print(link["href"])
print(soup.prettify())