import requests
from bs4 import BeautifulSoup
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# # ChromeDriver를 설치하고 경로를 변수에 저장
# driver_path = ChromeDriverManager().install()

# # 저장된 경로를 사용하여 ChromeDriver 실행
# driver = webdriver.Chrome(driver_path)

def searchWeather(kind,location):
    url = 'https://www.weather.go.kr/w/weather/forecast/' # 검색 대상 주소
    if kind == '단기 예보':
        url +='short-term.do?stnId='
    elif kind == '중기 예보':
        url +='mid-term.do?stnId1='
    location_dic = {'전국':'108', '서울/경기':'109','강원':'105','충청':'131','전라':'146','경상':'143', '제주':'184'}
    url += location_dic[location]
    #after-dfs-forecast > div:nth-child(1) > section > div.cmp-view-announce > span
    #after-dfs-forecast > div:nth-child(1) > section > div.cmp-view-content > p
    #body > div.container > section > div > div.cont-wrap.cmp-midterm > div > div > div.tab-menu-cont > div:nth-child(3) > div
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    if kind == '단기 예보':
        validate = soup.select('#after-dfs-forecast > div:nth-child(1) > section > div.cmp-view-announce > span')[0]
        content = soup.select('#after-dfs-forecast > div:nth-child(1) > section > div.cmp-view-content > p')[0]
    elif kind == '중기 예보':
        validate = soup.select("body > div.container > section > div > div.cont-wrap.cmp-midterm > div > div > div.tab-menu-cont > div.mid-tm-box.upper-box > span.txt > span")[0]
        content = soup.select('body > div.container > section > div > div.cont-wrap.cmp-midterm > div > div > div.tab-menu-cont > div:nth-child(3) > div')[0]
    
    return url, validate, content


def getNewsTitle(news_list):
    if news_list == 'ny':
        url = 'https://www.nytimes.com/'
    elif news_list == 'donga':
        url = 'https://www.donga.com/'
        
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    if news_list == 'ny':
        title = soup.find('title').text  # 실제 뉴욕타임스 구조에 맞게 수정 필요
    elif news_list == 'donga':
        title = soup.find('h2').text  # 실제 동아일보 구조에 맞게 수정 필요

    return title