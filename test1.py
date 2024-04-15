import requests
from bs4 import BeautifulSoup
from collections import OrderedDict

# get을 통해 받은 200은 정상적으로 연결했다는 뜻 - HTTP 상태 코드 참고
# Crawling 할 때 000/robots.txt 로 크롤링 가능한 범위 체크 필수

result_title = []
result_price = []

def crawl_page(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser",)
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

url = "https://storycloud.kr/705"
crawl_page(url)


