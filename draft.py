from bs4 import BeautifulSoup
import pandas as pd
import datetime 
from decimal import Decimal

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Tạo bảng
columns = ['MMYYYY',
            'Bank_name',
            'Bank_code', 
            'Peer_No',
            'Volume_type',
            'Segment',
            'Off_1M', 'Off_2M', 'Off_3M', 'Off_6M','Off_12M', 'Off_13M', 'Off_18M', 'Off_24M', 'Off_36M',
            'Onl_1M', 'Onl_2M', 'Onl_3M', 'Onl_6M','Onl_12M', 'Onl_13M', 'Onl_18M','Onl_24M','Onl_36M'
            ]


Update_inst = pd.DataFrame(columns=columns)

url_chrome = r"D:\Chromedriver\chromedriver.exe"


def convert_to_float(value):
    return round(Decimal(float(value.replace('.', '.').replace(',', '.').replace('%', '').replace('*', ''))),3)
chrome_options = Options()
driver = webdriver.Chrome(service=Service(executable_path=url_chrome), options=chrome_options)
driver.maximize_window()

try:
    driver.set_page_load_timeout(10)
    TPB = driver.get('https://tpb.vn/cong-cu-tinh-toan/lai-suat')
    TPB_soup = BeautifulSoup(driver.page_source, 'html').find('div', class_= "tab-table tabside-bar")
    TPB_table = TPB_soup.find_all('table')[0]
except:    
    TPB_html = driver.page_source
    TPB_soup = BeautifulSoup(TPB_html, 'html')
    TPB_div = TPB_soup.find('div', class_= "tab-table tabside-bar")
    TPB_table = TPB_soup.find_all('table')[0]


value_offline_truong_an = [(TPB_table.find_all("tbody")[0]\
                                  .find_all("tr")[y]\
                                  .find_all("td")[1]\
                                  .text.strip()) for y in [0,0,1,2,3,3,4,5,6]]

value_online = [(TPB_table.find_all("tbody")[0]\
                                  .find_all("tr")[y]\
                                  .find_all("td")[2]\
                                  .text.strip()) for y in [0,0,1,2,3,3,4,5,6]]

value_offline_cuoi_ky  = [(TPB_table.find_all("tbody")[0]\
                                  .find_all("tr")[y]\
                                  .find_all("td")[3]\
                                  .text.strip()) for y in [0,0,1,2,3,3,4,5,6]]

Update_inst.loc[1, ['MMYYYY',
                    'Bank_code', 
                    'Volume_type',
                    "Off_1M","Off_2M","Off_3M", "Off_6M", "Off_12M","Off_13M","Off_18M", "Off_24M", "Off_36M",
                    "Onl_1M","Onl_2M","Onl_3M","Onl_6M", "Onl_12M","Onl_13M","Onl_18M", "Onl_24M", "Onl_36M"]]\
                 = [datetime.datetime.now().strftime("%d/%m/%Y"),
                    'TPB',
                    'All',
                    *value_offline_cuoi_ky if x is not None else *value_offline_truong_an for x in value_offline_cuoi_ky
                    *value_online
                    ]

driver.quit()
