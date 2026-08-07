import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (common on some systems for this assignment)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    # position is 1-based, so subtract 1 for the list index
    href = tags[position - 1].get("href")
    # Resolve in case the href is relative instead of a full URL
    url = urllib.parse.urljoin(url, href)

print("Retrieving:", url)

# Extract just the name from the final URL, e.g. known_by_Sitor.html -> Sitor
last_part = url.rstrip("/").split("/")[-1]
name = last_part.replace("known_by_", "").replace(".html", "")
print("Last name retrieved:", name)