import requests as req
import os
import bs4

url = 'https://xkcd.com/'
if not os.path.isdir('xkcd'):
    os.makedirs('xkcd')

for i in range(100, 110):
    temp = url + str(i)
    print('Downloading image from %s...' % temp)
    res = req.get(temp)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    comicUrl = 'https:' + comicElem[0].get('src')
    res = req.get(comicUrl)
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

print('Successfully downloaded')
