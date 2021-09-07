import requests
from bs4 import BeautifulSoup

URL = "https://stevensducks.com/sports/mens-soccer/stats/2021/no-23-ithaca-college/boxscore/13121"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())


# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text)

list_of_events = text.split('\n')
#for row in list_of_events:
#    print(row)

cut=0
for i in range(len(list_of_events)):
    if list_of_events[i] == '00:00':
        cut=i

print(len(list_of_events))
print(cut)
print(list_of_events[cut:])

goals = []
for i in range(len(list_of_events)):
    if list_of_events[i].__contains__('GOAL'):
        goals+=[i]
print(goals)

print(list_of_events[907],list_of_events[912],list_of_events[1064],list_of_events[1069])