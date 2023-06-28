# Python 크롤링 필요 라이브러리 임포트

import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time

# 건강기능 식품 검색 - 리스트 페이지
# Post 데이터 폼
list_page_data = {'menu_no' : '2823',
        'menu_grp' : 'MENU_NEW04',
        'menuNm' : '건강기능식품 검색',
        'copyUrl' : 'https://www.foodsafetykorea.go.kr:443/portal/healthyfoodlife/searchHomeHFProc.do?menu_grp=MENU_NEW05&menu_no=2827',
        'mberId' : '',
        'mberNo' : '',
        'favorListCnt' : '0',
        'search_code' : '01',
        'search_word' : '',
        'show_cnt' : '50',
        'start_idx' : '1'}

# 헤더 데이터 정보
list_page_header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Content-Length': '262',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'elevisor_for_j2ee_uid=fwu78dtpd7a2r; JSESSIONID=AbNlBr6zNhVxPXuNIa2SYNxm2L1ufRgJrUQbO2POskcyO2NNxza8VQLAuUhPKI5i.amV1c19kb21haW4veGNvd2FzMDNfSVBPMDE=; _ga=GA1.3.1906239005.1686975824; _gid=GA1.3.1285248620.1686975824; cookieTerm=%uAC74%uAC15%uAE30%uB2A5%uC2DD%uD488; menu_grp=MENU_NEW01; _gat=1',
'Host': 'www.foodsafetykorea.go.kr',
'Origin': 'https://www.foodsafetykorea.go.kr',
'Referer': 'https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/searchHomeHF.do?menu_grp=MENU_NEW04&menu_no=2823', # 요청을 보낸 이전 주소(이부분만 넣어서 해봄)
'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "macOS",
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


detail_page_data = {
    "prdlstReportLedgNo": "2023021000259351",
    "search_word": "",
    "search_code": "01",
    "start_idx": "1",
    "show_cnt": "10",
    "menu_no": "2823",
    "menu_grp": "MENU_NEW04"
}

detail_page_header = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '120',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'elevisor_for_j2ee_uid=bn5rcdtstbzp3; JSESSIONID=Y8LUngXcwio8O66vKRZ6Lea09CnuBZRqHO8wN6SOP9CGERFmxUPI5UZ2VdvlnTON.amV1c19kb21haW4veGNvd2FzMDNfSVBPMDE=; _ga=GA1.3.863865110.1687078695; _gid=GA1.3.1669119883.1687078695; _gat=1',
'Host': 'www.foodsafetykorea.go.kr',
'Origin': 'https://www.foodsafetykorea.go.kr',
'Referer': 'https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/searchHomeHF.do?menu_grp=MENU_NEW04&menu_no=2823',
'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "macOS",
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}


# 헤더는 리스트페이지헤더를 그대로 사용



df = pd.DataFrame();

page_index = 1
while(True):
  if page_index > 2:
    break

  list_page_data['start_idx'] = page_index
    # 요청 전송
  list_page_response = requests.post(
    'https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/searchHomeHFProc.do',
    data= list_page_data , headers= list_page_header
  )
  time.sleep(3)
  list_page_soup= BeautifulSoup(list_page_response.text,'html.parser')
  # json데이터 파싱
  list_page_json_data = json.loads(str(list_page_soup))

  for i in range(0,len(list_page_json_data),1):
    print(list_page_json_data[i]['prdlst_report_ledg_no']) # 상품 코드 모두 출력 이 코드를 이용해 코드별 접속이 가능
    item_no = list_page_json_data[i]['prdlst_report_ledg_no'] # 상품 코드 모두 출력 이 코드를 이용해 코드별 접속이 가능
    detail_page_data['prdlstReportLedgNo'] = item_no
    detail_page_response = requests.post('https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/searchHomeHFDetail.do',data= detail_page_data , headers= detail_page_header) # 상세정보 페이지 요청
    print(detail_page_response.status_code) # 상태 코드 출력
    time.sleep(3)
    detail_page_soup = BeautifulSoup(detail_page_response.text,'html.parser')
    container = detail_page_soup.select("#contents > main > div.page-container")
    table = detail_page_soup.select('.mb-table')
    rows = detail_page_soup.find_all('tr')
    th_text = ""
    td_text = ""
    for row in rows:
      th = row.find('th')
      td = row.find('td')
      if th:
        th_text += th.get_text()+'$'
      else:
        th_text +='$'
      if td:
        td_text += td.get_text()+'$'
      else:
        td_text +='$'
    print(td_text)
    
    #print(td_text)
    df2 = pd.DataFrame(columns=th_text.split('$'),data=[td_text.split('$')])
    df = pd.concat([df, df2]) # row bind : axis = 0, default
    print('len(df)',len(df))
  page_index+=1

import pandas as pd

# CSV파일로 저장하기
df.to_csv("test.csv")
# 엑셀로 저장하기
df.to_excel("test.xlsx")


# // 정규식 패턴을 사용하여 URL을 추출
# const urlPattern = /url\("([^"]+)"\)/g;
# const matches = cssValue.matchAll(urlPattern);

# // 추출된 URL 출력
# for (const match of matches) {
#   const url = match[1];
#   console.log(url);
# }