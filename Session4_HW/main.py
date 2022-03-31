from urllib.error import URLError
import requests
from bs4 import BeautifulSoup
from webtoon import extracting
import csv

results = []
f = open('webtoon.csv', mode='w', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(['title', 'who', 'point'])
URL = f'https://comic.naver.com/webtoon/weekdayList?week=fri'
wt_html = requests.get(URL)
wt_soup = BeautifulSoup(wt_html.text, "html.parser")

wt_list_list = wt_soup.select_one("ul.img_list")
wt_list = wt_list_list.select("li")

crawlings = extracting(wt_list)

for crawling in crawlings:
    info_row=[]
    info_row.append(crawling['title'])
    info_row.append(crawling['who'])
    info_row.append(crawling['point'])
    writer.writerow(info_row)
print(crawlings)