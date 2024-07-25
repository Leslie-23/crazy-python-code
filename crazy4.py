from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import choice

url = 'https://www.wunderground.com/'

city = input('Type a city: ')
driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
driver.get(url)

driver.find_element_by_name('query').send_keys(city)

time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
possible_cities = soup.find_all('span', {'class':'ui-autocomplete-term'})

choose_city = [ x.parent.text for x in possible_cities ]
city = choice.Menu(choose_city).ask()

driver.find_element_by_name('query').send_keys(Keys.CONTROL + "a")
driver.find_element_by_name('query').send_keys(Keys.DELETE)

driver.find_element_by_name('query').send_keys(city)
driver.find_element_by_name('query').send_keys(Keys.ENTER)

soup = BeautifulSoup(driver.page_source, 'html.parser')
temp = soup.find('div', {'class':'condition-data'})
wind = soup.find('div', {'class':'condition-wind'})

deg = temp.find('span',{'class':'ng-star-inserted'}).text.split()[-1]
hi = temp.find('span',{'class':'hi'}).text
low = temp.find('span',{'class':'lo'}).text
current = temp.find('span',{'class':'wu-value wu-value-to'}).text

wdesc = wind.find('p',{'class':'ng-star-inserted'}).text.strip()

print ('%s\nHi: %s%s Low: %s%s Current: %s%s\n%s' %(city, hi,deg, low,deg, current,deg, wdesc))


driver.close()
