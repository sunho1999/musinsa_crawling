import requests
from bs4 import BeautifulSoup

brandname = []
headers = {'User-Agent' : 'Mozilla/5.0'}

#특정 URL에 접속 하는 요청 (Request)객체를 생성합니다.
request = requests.get("https://store.musinsa.com/app/contents/brandshop",headers = headers)
#접속한 이후의 웹 사이트 소스코드를 추출합니다.
html = request.text.strip()

#HTML 소스코드를 파이썬 객체로 변환합니다.
soup = BeautifulSoup(html,'html.parser')

#<dl>태그 포함하는 요소를 추출합니다.
brand_list = soup.findAll('dl')

for brand in brand_list:
    names = brand.findAll('a')
    for name in names:
        total_name = name.get('href')
        brandname.append(total_name)
# 중복 제거
brandname = set(brandname)
brandname = list(brandname)
#정리된 브랜드 담을 리스트
total_brandname = []

for i in brandname:
    str = i.replace('/app/brand/goods_list/',"")
    total_brandname.append(str)

print(total_brandname)