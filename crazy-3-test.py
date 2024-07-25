import requests
from bs4 import BeautifulSoup

url = 'https://www.example-weather-website.com/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Assuming the temperature data is within a tag with class 'temperature'
temperature = soup.find('span', class_='temperature').get_text()
print(f"Current temperature: {temperature}")
