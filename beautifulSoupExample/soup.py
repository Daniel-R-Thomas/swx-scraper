import requests
from bs4 import BeautifulSoup

import requests

url = raw_input("Enter a website to extract the URL's from: ")

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})


headers = {'User-Agent': 'Mozilla/5.0'}

r  = requests.get("http://" +url, headers=headers)

data = r.text

soup = BeautifulSoup(data, "lxml")

print "Pulling data from: " + url
print "\n"

print soup.title.string


print "\n"

postCount = 0
trumpCount = 0
trumpList = []
trumpWordList = ["russia", "trump", "ivanka", "china", "mueller"]
for heading in soup.find_all(["h2"]):
    text = heading.text.strip()
    print(" - " + text)
    postCount += 1

    for word in trumpWordList:
        if word in text.lower():
            trumpCount += 1
            trumpList.append(text)
            break

print "\nRelated possible Trump posts pulled: " + str(trumpCount) + " out of " + str(postCount) + " posts"
for x in range(len(trumpList)):
    print " ~ " + trumpList[x]
