from nltk.corpus import stopwords
import nltk

# know what a web page is about.
from bs4 import BeautifulSoup
import urllib.request

# crawel
response = urllib.request.urlopen('https://en.wikipedia.org')
html = response.read()

# filter to text
soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip=True)
text = text.encode("utf-8")

# convert to tokens
tokens = [t for t in text.split()]

# count word frequancy
# (20 most frequant words)
sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):

        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)
