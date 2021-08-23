# musinsa_crawling
- - -
<img width="600" alt="스크린샷 2021-08-22 오후 8 26 51" src="https://user-images.githubusercontent.com/80037682/130353346-645863d7-8e1e-4f50-bc42-4fa906240844.png">

무신사의 각 브랜드 상품 데이터 크롤링 후 시각화하기
- - -
## 프로젝트 목적
    
 무신사는 다양한 브랜드들을 모아놓은 편집샾인데 원하고자 하는 브랜드의 가격과 상품,이미지 등을  
 가져와 각 브랜드들의 평균가를 비교하여 보다 가격이 저렴한 브랜드를 찾고자 시작했습니다.
- - -
## 단계별 접근
**1. 웹 크롤링 하기**  
* BeautifulSoup 와 requests 라이브러리를 사용합니다.

**2. 웹 크롤링 한 데이터 입출력하기**
*  excel 파일로 데이터를 저장합니다.
    
**3. 데이터들을 데이터 프레임화 시킨 후 시각화 하기**
* matplotlib 라이브러리를 사용하여 시각화 합니다.   
  이때 시각화를 할 때 비교하기 편한 가로형 막대그래프를 이용합니다.
  
- - -

<img width="1352" alt="스크린샷 2021-08-22 오후 8 20 45" src="https://user-images.githubusercontent.com/80037682/130353186-17f14bf3-dd4e-4f3a-862e-791db387f3cf.png">

~~~
현재 무신사스토어는 main_category로 상의,아우터,바지,원피스 등 품목 별로 분류를 해놓았고 약 3500여개의 브랜드가 입점되어있습니다.
이 중에서 내가 원하고자 하는 브랜드들의 html주소를 parsing하여 각 브랜드의 품목별 평균가를 excel파일로 저장합니다.
~~~

### 웹 크롤링한 브랜드 사이트
<center>

[thisisneverthat](https://display.musinsa.com/display/brands/thisisneverthat?category3DepthCodes=&category2DepthCodes=&category1DepthCode=&colorCodes=&startPrice=&endPrice=&exclusiveYn=&includeSoldOut=&saleGoods=&timeSale=&includeKeywords=&sortCode=3m&tags=&page=1&size=90&listViewType=small&campaignCode= "디스이즈네버뎃")    
[covernat](https://display.musinsa.com/display/brands/covernat?category3DepthCodes=&category2DepthCodes=&category1DepthCode=&colorCodes=&startPrice=&endPrice=&exclusiveYn=&includeSoldOut=&saleGoods=&timeSale=&includeKeywords=&sortCode=3m&tags=&page=1&size=90&listViewType=small&campaignCode= "커버낫")  
[musinsastanddard](https://display.musinsa.com/display/brands/musinsastandard?category3DepthCodes=&category2DepthCodes=&category1DepthCode=&colorCodes=&startPrice=&endPrice=&exclusiveYn=&includeSoldOut=&saleGoods=&timeSale=&includeKeywords=&sortCode=3m&tags=&page=1&size=90&listViewType=small&campaignCode= "무신사스탠다드")
</center>

## 각 브랜드의 상의,아우터,하의 평균값을 데이터프레임화하기

<img width="337" alt="스크린샷 2021-08-23 오후 8 52 58" src="https://user-images.githubusercontent.com/80037682/130444779-01dba56c-c065-4843-8a5d-7fbe1b27b8f5.png">

## 데이터프레임 시각화하기
<img width="1193" alt="스크린샷 2021-08-23 오후 8 52 42" src="https://user-images.githubusercontent.com/80037682/130442864-53952f14-278d-4773-a1f2-cc25fc76ecc4.png">

## 데이터 시각화 후 분석
* 전체적으로 상의,하의,아우터 중 아우터 > 하의 > 상의 순으로 가격이 측정되었다.
* 특정 3가지 브랜드를 따져봤을 때 'musinsastandard' 라는 브랜드의 평균가가 제일 낮았다.

