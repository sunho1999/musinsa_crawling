import requests
from bs4 import BeautifulSoup
import pandas as pd

brandname = ["thisisneverthat","musinsastandard","covernat"]

#특정 URL에 접속 하는 요청 (Request)객체를 생성합니다.
html = "https://display.musinsa.com/display/brands/"
another_html = "?category3DepthCodes=&category2DepthCodes=&category1DepthCode=&colorCodes=&startPrice=&endPrice=&exclusiveYn=&includeSoldOut=&saleGoods=&timeSale=&includeKeywords=&sortCode=3m&tags=&page=1&size=90&listViewType=small&campaignCode="
list_url= []
# 데이터 프레임 저장할 리스트
brand_ave = {}

for i in brandname:
    full_html = ""
    full_html = html + i + another_html
    list_url.append(full_html)
    cnt = 0
for url in list_url:
    request = requests.get(url)
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
    sum = 0
    for i in price:
        sum = sum + i
        ave_sum = sum//len(price)

    # bradn_ave에 각 브랜드 평균가 저장하기
    brand_ave[brandname[cnt]] = [ave_sum]
    cnt += 1


df = pd.DataFrame(brand_ave)
df.index = ['평균가']
print(df)
# 해당 경로에 엑셀파일로 저장하기
df.to_excel(excel_writer='/Users/sunho99/PycharmProjects/python_Project/musinsa/crawling/sample.xlsx')

