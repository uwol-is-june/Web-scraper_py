from requests import get

#get을 통해 받은 200은 정상적으로 연결했다는 뜻 - HTTP 상태 코드 참고
#Crawling 할 때 000/robots.txt 로 크롤링 가능한 범위 체크 필수

a = get('https://www.naver.com')
print(a)