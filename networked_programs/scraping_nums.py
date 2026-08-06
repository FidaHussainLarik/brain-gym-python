import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url =   input("Enter - ")
# url = 'https://py4e-data.dr-chuck.net/comments_2432573.html'
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')


# # retrive all of the anshor tags
tags = soup('span')

total = 0
count = 0
for index , tag in enumerate(tags):
    num = int(tag.text)
    total = total + num
    count = index

print(f"Count {count}")
print(f"Sum {total}...")