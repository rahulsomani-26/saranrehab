import requests 
from bs4 import BeautifulSoup 
url = 'https://www.accuweather.com/en/in/musahri/3228013/weather-forecast/3228013'

def get_weather(url):
    result = requests.get(url)
    if result.status_code:
        print("Fetching Data")
        data = result.text 
        soup = BeautifulSoup(data,'html.parser')
        print(soup.prettify())

    else:
        print("Error in Fetching data")

get_weather(url=url)