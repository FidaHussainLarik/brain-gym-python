import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# url =   input("Enter - ")
url = 'https://dr-chuck.com/'
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')


# retrive all of the anshor tags
tags = soup('a')
for tag in tags:
    print(tag)
    print(tag.get('href',None))


