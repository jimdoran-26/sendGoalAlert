import requests
from bs4 import BeautifulSoup

URL = "https://stevensducks.com/sports/mens-soccer/stats/2021/no-23-ithaca-college/boxscore/13121"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())

a= soup.find("td", text="00:00 :").find_next_sibling("td").text
print(a)