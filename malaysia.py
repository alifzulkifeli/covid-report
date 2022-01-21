import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/country/malaysia/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.find_all('script')

myarr = []

for i in  range(len(result)):
  myarr.append([i,result[i]])
    

with open('output.txt', 'w') as f:
    f.write(str(myarr))


