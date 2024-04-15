from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
from collections import OrderedDict
import csv

result_title = []
result_price = []

def crawl_page(soup):
    before_title = []
    before_price = []

    # class로 검색 시 class_ 로 해야함
    scripts = soup.find("div", id="container_w20240101a09346a42bfca").find_all("div", class_="item-pay")
    for script in scripts:
        before_title.append(script.find('h2').text.strip())
        before_price.append(script.find('p', class_='pay inline-blocked').text.strip().replace(',','').replace('원', ''))
    # OrderedDictionary로 저장하면 순서대로 생성되는데, 다시 list로 변환하면 key만 남게 되어 정상적으로 작동
    result_title.append(list(OrderedDict.fromkeys(before_title))) 
    # 가격의 경우 중복 값이 가능하기 때문에 짝수 번째 항 슬라이스
    result_price.append(before_price[::2])
    print(result_price)
    print(result_title)


p = sync_playwright().start()

# headless True면 브라우저 안보이고 프로세스만 실행
browser = p.chromium.launch(headless=False)
page = browser.new_page()

# 페이지 이동
page.goto("https://storycloud.kr/705")
time.sleep(3)

# 최하단 이동
while(True):
  page.keyboard.down("End")
  time.sleep(3)
  button_exists = page.locator('.btn._more_btn.more_btn').first.is_visible()

  if button_exists:
      page.click('.btn._more_btn.more_btn')
      time.sleep(3)
  else:
      time.sleep(3)
      break


content = page.content()
p.stop()
soup = BeautifulSoup(content, "html.parser")
crawl_page(soup)

# csv 저장
file = open("name_price.csv", mode="w", encoding="utf-8")
writter = csv.writer(file)
writter.writerow(["작품 명", "가격"])
for title, price in zip(result_title[0], result_price[0]):
    writter.writerow([title, price])
