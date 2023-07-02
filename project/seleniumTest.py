from selenium import webdriver
from selenium.webdriver.common.by import By 
import io


import time
#options = webdriver.ChromeOptions()
#options.add_argument("headless")
driver = webdriver.Chrome()

url = "https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/searchHomeHF.do?menu_grp=MENU_NEW04&menu_no=2823"
f = open('../crollingTest.txt', 'w')

driver.get(url)

time.sleep(5)

mobile_table = driver.find_element(By.CSS_SELECTOR, ".mobile_table")
table_txt = mobile_table.find_elements(By.CSS_SELECTOR, ".table_txt")

def parse_product_page(driver):
    time.sleep(5)
    print("test")
    mb_tabl = driver.find_element(By.CSS_SELECTOR, "table.mb-table.mb-view.left-txt")
    tbody = mb_tabl.find_element(By.CSS_SELECTOR, "tbody")
    tr = tbody.find_elements(By.CSS_SELECTOR, "tr")
    for t in tr:
        th = t.find_element(By.CSS_SELECTOR, "th")
        td = t.find_element(By.CSS_SELECTOR, "td")
        print(th.text, td.text)
        f.write(th.text+'\\n')
        f.write(td.text+'\\n')
        print()

for i in range(1, len(table_txt), 5):
    print(table_txt[i].text)
    table_txt[i].click()
    parse_product_page(driver)
    driver.back()
    time.sleep(5)

# 파일 닫기
f.close()
# 드라이버 닫기
driver.close()