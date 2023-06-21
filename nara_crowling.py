# Step 1. 필요한 모듈과 라이브러리를 로딩하고 검색어를 입력 받습니다
from bs4 import BeautifulSoup     
from selenium.webdriver.common.by import By
import time
import sys

query_txt = input('크롤링할 키워드는 무엇입니까?: ')
start_date = input('조회 시작일자 입력: ')
end_date = input('조회 종료일자 입력: ')
ft_name = input('검색 결과를 저장할 txt 파일경로와 이름을 지정하세요: ')
fx_name = input('검색 결과를 저장할 xls 파일경로와 이름을 지정하세요: ')

#Step 2. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "c:/temp/chromedriver_240/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.g2b.go.kr/index.jsp")
time.sleep(2)

#Step 3. 검색창의 이름을 찾아서 검색어를 입력 후 검색을 진행합니다
#driver.find_element(By.NAME, 'bidNm').click()
element = driver.find_element(By.NAME, 'bidNm')
element.send_keys(query_txt)
element = driver.find_element(By.NAME, 'fromBidDt')
#element.clear()
element.send_keys(start_date)
element = driver.find_element(By.NAME, 'toBidDt')
#element.clear()
element.send_keys(end_date)
driver.find_element(By.CLASS_NAME, "btn_dark").click()

# Step 4. 현재 페이지에 있는 내용을 화면에 출력하기
time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content_list = soup.find('div',class_='results')
print(html)
