from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
chrome_options = Options()
chrome_options.add_argument('--headless')

# 啟動webdrive
driver = webdriver.Chrome(
    'C:\\Users\\JK251\\Desktop\\NLP_homework\\HW2\\chromedriver.exe')
# get義大醫院網頁
driver.get('https://www5.edah.org.tw/MainDept.aspx?Hospital=EDAH')
# 各科的連結網址 這裡是皮膚科
url = "RegisterChooseOption.aspx?Hospital=EDAH&deptCode=63&deptDesc=%e7%9a%ae%e8%86%9a%e7%a7%91&stockCode=O_CE&eng_deptDesc=Division+of+Dermatology"
# 點擊皮膚科
driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
# 使用bf4 得到網頁資料
soup = BeautifulSoup(driver.page_source, 'html5lib')
# 搜尋table
table = soup.find('table', id='AutoNumber1')
# 關閉webdrive
driver.close()
# print(table.prettify())
while True:
    print("你想知道義大醫院 哪位皮膚科醫生的看診時間？ 如要結束請輸入 q")
    search_name = input(" 請直接輸入醫生姓名 或是 輸入q來結束：  ")
    if search_name == "q":
        break

    # 搜尋列表
    rows = [x for x in table.findAll('tr') if x.find("td") != None]

    data_list = []
    for i in range(0, len(rows)-1):
        for j in range(1, 4):
            if re.search(search_name, rows[i].findAll('td')[j].text) != None and re.search("已額滿", rows[i].findAll('td')[j].text) == None:
                data_list.append({
                    '醫師姓名': search_name,
                    '日期': rows[i].findAll('td')[0].text,
                    '時段': rows[0].findAll('td')[j].text,
                })

    # 判斷和打印時間
    if data_list:
        for i in data_list:
            print(i)
    else:
        print("你所輸入的醫生進一個月都沒有門診")
