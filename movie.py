import requests
from bs4 import BeautifulSoup
url = "http://www.atmovies.com.tw/movie/next/"
Data = requests.get(url)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".filmListAllX li")
info = ""
for item in result:
  info += item.text + "\n\n"
print(info)
