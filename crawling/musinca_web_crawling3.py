import requests
from bs4 import BeautifulSoup
import pandas as pd

#특정 URL에 접속 하는 요청 (Request)객체를 생성합니다.
request = requests.get("https://display.musinsa.com/display/brands/musinsastandard?category3DepthCodes=&category2DepthCodes=&category1DepthCode=&colorCodes=&startPrice=&endPrice=&exclusiveYn=&includeSoldOut=&saleGoods=&timeSale=&includeKeywords=&sortCode=3m&tags=&page=1&size=90&listViewType=small&campaignCode=")

#접속한 이후의 웹 사이트 소스코드를 추출합니다.
html = request.text.strip()

#HTML 소스코드를 파이썬 객체로 변환합니다.
soup = BeautifulSoup(html,'html.parser')

#<span>태그 포함하는 요소를 추출합니다. (가격)
price_divs = soup.findAll('span', {"class":"txt_price_member"})

# 무신사 스탠다드 가격 담을 리스트
price = []

for link in price_divs:
    # text형식을 뽑아온다.
    links = link.get_text()
    price.append(links)

#<p>태그 포함하는 요소를 추출합니다.
divs_clothes = soup.findAll('p', {"class":"list_info"})

# 무신사 스탠다드 종목 담을 리스트
subjects = []

for link in divs_clothes:
    links = link.findAll("a")
    for lin in links:
        # title을 가져와 subjects에 담습니다.
        subject = lin.get("title")
        subjects.append(subject)

for i in range(len(price)):
    price[i] = price[i].replace(',','')
    price[i] = price[i].replace("원",'')
    price[i] = int(price[i])

total = {}
for i in range(len(subjects)):
    total[subjects[i]] = price[i]

print(total)