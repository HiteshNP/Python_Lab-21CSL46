"""Write a python program to download the all XKCD comics"""

import requests as req
import os, bs4

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)

for i in range(1, 8):
    print('Downloading image from %s...' % url)
    res = req.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    comicUrl = 'http:' + comicElem[0].get('src')

res = req.get(comicUrl)

imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
for chunk in res.iter_content(1):
    imageFile.write(chunk)
imageFile.close()
print('Successfully downloaded')
