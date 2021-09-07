import requests
from bs4 import BeautifulSoup

def get_data(url):
    STARTING_POINT='00:00'
    URL = url

    response = requests.get(URL)
    if response.status_code != 200: #check that the url is valid
        print("Error in the HTTP request")
        return None

    soup = BeautifulSoup(response.content, 'html5lib')

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    list_of_events = text.split('\n')

    start_index = 0 #eliminate the preceeding to the box score information
    for i in range(len(list_of_events)):
        if list_of_events[i] == STARTING_POINT:
            start_index = i

    #print(list_of_events[start_index:])
    return list_of_events[start_index:]