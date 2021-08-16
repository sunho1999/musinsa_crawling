import requests
from bs4 import BeautifulSoup

#특정 URL에 접속 하는 요청 (Request)객체를 생성합니다.
request = requests.get("https://display.musinsa.com/display/brands/musinsastandard?category3DepthCodes=&category2DepthCodes=&category1DepthCode=&colorCodes=&startPrice=&endPrice=&exclusiveYn=&includeSoldOut=&saleGoods=&timeSale=&includeKeywords=&sortCode=3m&tags=&page=1&size=90&listViewType=small&campaignCode=")

#접속한 이후의 웹 사이트 소스코드를 추출합니다.
html = request.text.strip()

#HTML 소스코드를 파이썬 객체로 변환합니다.
soup = BeautifulSoup(html,'html.parser')

#<div>태그 포함하는 요소를 추출합니다. (이미지 링크)
image_divs = soup.findAll('div', {"class":"list_img"})
image_list= []
for img in image_divs:
    # img형식을 뽑아온다.
    images = img.findAll("img")
    for image in images:
        # data-original속성을 확인합니다.
        img_link = image.get("data-original")
        image_list.append(img_link)

for i in image_list:
    i = "https:" + i
    print(i)

