import requests
import random

def get_data():
    url = "https://www.reddit.com/r/todayilearned.json?limit=100"
    response = requests.get(url,headers={"User-agent":"todayilearned"})
    r = random.randint(1, 100)
    til = response.json()["data"]["children"][r]["data"]["title"]

    if(til[:3] == 'TIL'):
        til = til[4:]
        if(til[:4] == "that"):
            til = til[5:]
            
    return til