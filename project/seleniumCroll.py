from selenium import webdriver
from selenium.webdriver.common.by import By 
import io


import time
#options = webdriver.ChromeOptions()
#options.add_argument("headless")
driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from urllib.request import urlopen
import re


subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie"')
url = "https://www.hffinfo.com/search/product"


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get(url)





time.sleep(5)

item_list = driver.find_elements(By.CSS_SELECTOR,'#__next > div:nth-child(4) > div.BoardList__Container-sc-yasezg-0.eEDNnM.font-notosans > div.items > a')
# 총 요소 개수
print("item_list_len : ",len(item_list))
item_list_len = len(item_list)

# 요소의 값 (상품 이름,기능성 내용,회사)
print("item_list : ",item_list[0].text.split('\n'))
item_list_text = item_list[0].text.split('\n')

# 요소의 이미지 링크
img_href = item_list[0].find_element(By.CLASS_NAME,"row").find_element(By.CLASS_NAME,'thumbnail').get_attribute("style")
print("img_href : ",img_href)

# 요소의 링크(상세 페이지 이동을 위한)
print("item_src : ",item_list[0].get_attribute('href'))
item_list_src = item_list[0].get_attribute('href')
start = item_list_src.rfind("/") + 1
end = item_list_src.find("?", start)
item_list_src = item_list_src[start:end]

time.sleep(3)

#상세 페이지 값 가져오기
url = 'https://www.hffinfo.com/api/foods/'+item_list_src
httpResponse = urlopen(url)
jsondata = json.load(httpResponse)
print(jsondata['domestic'])
domestic = jsondata['domestic']
PRDT_SHAP_CD_NM = domestic['PRDT_SHAP_CD_NM']
LCNS_NO = domestic['LCNS_NO']
PRDLST_NM = domestic['PRDLST_NM']
IFTKN_ATNT_MATR_CN = domestic['IFTKN_ATNT_MATR_CN']
BSSH_NM = domestic['BSSH_NM']
POG_DAYCNT = domestic['POG_DAYCNT']
NTK_MTHD = domestic['NTK_MTHD']
RAWMTRL_NM = domestic['RAWMTRL_NM']

### 상세 페이지별 데이터 정보
"""

"PRDT_SHAP_CD_NM"    : "캡슐"                                               제형
"LCNS_NO"            : "20040015083"                                        상품번호
"PRDLST_NM"          : "루테인오메가플러스D&E"                               상품 이름
"IFTKN_ATNT_MATR_CN" : "과다 섭취 시 일시적으로 ..."                          섭취 시 주의사항
"BSSH_NM"            : "주식회사한미양행"                                    제조사명
"STDR_STND"          : "(1) 성상 : 이미, 이취가..."                          기준 및 규격
"DISPOS"             : "이미, 이취가 없고 고유의 향미가 있는..."               성상만
"PRIMARY_FNCLTY"     : "①혈중 중성지질 개선·혈행 개선..."                     기능성 내용
"FRMLC_MTRQLT"       : "폴리에틸렌(PE), ..."                                 포장재질(방법)
"POG_DAYCNT"         : "제조일로부터 24개월"                                  유통기한
"NTK_MTHD"           : "1일 1회, 1회 1캡슐을..."                             섭취량/섭취 방법
"RAWMTRL_NM"         :  "EPA 및 DHA 함유 유지..."                            기능성 원료


데이터 프레임  컬럼(예상) 

NO , 상품번호 , 상품 이름 , 제조사명 , 유통기한 , 섭취량/섭취 방법  , 제형 , 기능성 원료 , 기능성 내용 , 이미지 링크 , [조회수,성상,포장재질,...]


"""


# CSV 데이터
data = [
    ["NO" , "상품번호" , "상품 이름" , "제조사명" , "유통기한" , "섭취량 및 섭취 방법"  , "제형" , "기능성 원료" , "기능성 내용" , "이미지 링크"]
]
row_one = list([1,LCNS_NO,PRDLST_NM,BSSH_NM,POG_DAYCNT,NTK_MTHD.replace(',','$'),PRDT_SHAP_CD_NM,RAWMTRL_NM.replace(',','$'),item_list_text[1].replace(',','$'),img_href])

data.append(row_one)
print(data)

filename = "seleniumCroll.csv"

# CSV 문자열 작성
csv_string = ""
for row in data:
    csv_string += ",".join(map(str, row)) + "\n"

# CSV 파일 작성
with open(filename, "w") as file:
    file.write(csv_string)

print("CSV 파일이 작성되었습니다.")







# 파일 닫기

# 드라이버 닫기
driver.close()