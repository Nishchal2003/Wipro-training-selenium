from bs4 import BeautifulSoup

html = '''
 <html> 
    <head>
        <title>My Page</title
    </head>
    <body> 
        <h1>Welcome</h1>
        <p>This is a paragraph.</p> 
        <a href="https://example.com">Click Here</a>
        <h2>Hi</h2>
        <h2>Hiiii</h2>
        <b>How are you</b>
        <table>
            <tr><th>Name</th><th>Age</th></tr>
            <tr><td>Nishchal</td><td> 22</td></tr>
            <tr><td>Manjunath</td><td> 22</td></tr>
        </table>
    </body> 
</html> 
'''
soup = BeautifulSoup(html, "html.parser")

print(soup.title.text,soup.h1.text)

print(soup.p.text)

paragraphs = soup.find_all("p")
for paragaraph in paragraphs:
    print(paragaraph.text)

#print(soup.)
links = soup.find_all("a")
print(len(links))

for link in links:
    print(link.text)

print(soup.h2.text)
print(soup.b.text)

links = soup.find_all("a")

for link in links:
    print(link["href"])

for i in range(1,7):
    headings = soup.find_all(f"h{i}")
    for tag in headings:
        print(f"h{i}",tag.text)

tables = soup.find_all("table")
for table in tables:
    print(table.text)

images = soup.find_all("img")
for image in images:
    print(image.get("src"))