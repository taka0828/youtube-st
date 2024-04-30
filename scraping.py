!pip3 install BeautifulSoup4
from bs4 import BeautifulSoup
import requests
url = 'https://scraping-for-beginner.herokuapp.com/udemy'
res = requests.get(url)
res.text
soup = BeautifulSoup(res.text,'html.parser')
soup
n_subscriber = soup.find('p',{'class':'subscribers'}).text
n_subscriber
n_subscriver = int(n_subscriber.split('：')[1])
n_subscriber
n_review = soup.find('p',{'class':'reviews'}).text
n_review
n_review = int(n_review.split('：')[1])
n_review
url_ec = 'https://scraping.official.ec/'
res = requests.get(url_ec)
soup = BeautifulSoup(res.text,'html.parser')
item_list = soup.find('ul',{'id': 'itemList'})
item_list
len(item_list.find_all('li'))
items = item_list.find_all('li')
items
item = items[0]
item
item_find('p',{'class':'items-grid_itemTitleText_5c97110f'}).text