import requests
from bs4 import BeautifulSoup

print("Browsing...")
result = requests.get("http://app.trimbleinsphere.com/#/portal/terraflex/forms")
c = result.content
soup = BeautifulSoup(c)
##samples = soup.find_all("a", "item-title")
print(soup)
print("Done.")
