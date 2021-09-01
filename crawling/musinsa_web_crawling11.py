
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
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

brandname = []
while True:

    a = input("원하고자 하는 브랜드를 입력하세요: ")
    print("0을 입력하면 브랜드 검색을 종료합니다.")
    if a in total_brandname:
        brandname.append(a)
    elif a == "0":
        break
    elif a not in total_brandname:
        print("해당 브랜드는 없는 브랜드입니다. 다시 입력하세요.")


#특정 URL에 접속 하는 요청 (Request)객체를 생성합니다.
main_category = ["상의","하의","아우터",]

"""
data-category1depth-code="003" # 바지
data-category1depth-code="002" # 아우터
data-category1depth-code="001" # 상의
"""

# 각 브랜드 html 담을 리스트
list_url= []
ave_sum_list = []
for i in brandname:
    # 특정 URL에 접속 하는 요청 (Request)객체를 생성합니다.
    html = "https://display.musinsa.com/display/brands/"
    category_html = "?category3DepthCodes=&category2DepthCodes=&category1DepthCode="
    another_html = "&colorCodes=&startPrice=&endPrice=&exclusiveYn=&includeSoldOut=&saleGoods=&timeSale=&includeKeywords=&sortCode=3m&tags=&page=1&size=90&listViewType=small&campaignCode="
    full_html = ""
    category_code = "" # 품목별 코드 넣을 문자열
    print(i,"의 브랜드 카테고리를 찾습니다")
    for j in range(3):
        category = input("원하고자 하는 분류를 입력하세요: (ex 상의,아우터,하의)")
        if category == "상의":
            category_code = "001"
            full_html = html + i + category_html + category_code + another_html
        elif category == "아우터":
            category_code = "002"
            full_html = html + i + category_html + category_code + another_html
        elif category == "하의":
            category_code = "003"
            full_html = html + i + category_html + category_code + another_html

        list_url.append(full_html)

for url in list_url:
    cnt = 0

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

    # 브랜드제품 이름 담을 리스트
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

    sum = 0

    for i in price:
        sum = sum + i
        ave_sum = sum//len(price)
    ave_sum_list.append(ave_sum)


# 데이터 프레임 저장할 리스트
brand_ave = {}

# 한 리스트에 몇개씩 담을지 결정
n = len(main_category)
result = [ave_sum_list[i * n:(i + 1) * n] for i in range((len(ave_sum_list) + n - 1) // n )]

# 데이터 프레임화
for i in range(len(brandname)):
    brand_ave[brandname[i]] = result[i]


df = pd.DataFrame(brand_ave)
# 행열 바
df = df.T
# 데이터 프레임 열 바꾸기
df.columns = main_category
print(df)

# 해당 경로에 엑셀파일로 저장하기
df.to_excel(excel_writer='/Users/sunho99/PycharmProjects/python_Project/musinsa/crawling/brand_product_ave_price.xlsx')

# Excel 데이터를 데이터프레임 변환
df = pd.read_excel('brand_product_ave_price.xlsx', engine= 'openpyxl',index_col= 0)

df = df.loc[brandname,main_category ]
# 스타일 서식 지정
plt.style.use('ggplot')

# 수평 막대 그래프 그리기
df.plot( kind='barh',
         figsize=(12, 5),
         color = ['skyblue','orange','yellow'])

plt.title('각 브랜드 평균가 추출')
plt.ylabel('브랜드 이름')
plt.xlabel('가격')

plt.show()