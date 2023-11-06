from bs4 import BeautifulSoup
import pandas as pd
import datetime 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Tạo bảng
columns = ['MMYYYY','Bank_name', 'Bank_code', 'Peer_No', 'Volume_type', 'CASA_int', \
           'Off_1M', 'Off_2M', 'Off_3M', 'Off_6M', \
            'Off_12M', 'Off_13M', 'Off_18M', 'Off_24M', 'Off_36M',\
            'Onl_1M', 'Onl_2M', 'Onl_3M', 'Onl_6M',\
            'Onl_12M', 'Onl_13M', 'Onl_18M','Onl_24M','Onl_36M']


Update_inst = pd.DataFrame(columns=columns)

url_chrome = r"D:\Chromedriver\chromedriver.exe"

def convert_to_float(value):
    return float(value.replace(',', '.').replace('%', '').replace('*', ''))

url_ACB = 'https://www.acb.com.vn/lai-suat-tien-gui' # Done

# Send an HTTP GET request to the URL and retrieve the content
chrome_options = Options()
driver = webdriver.Chrome(service=Service(executable_path=url_chrome), options=chrome_options)
driver.maximize_window()
acb = driver.get(url_ACB)

# Set the common values for 'MMYYYY' and 'Bank_name'
Update_inst.loc[6, 'MMYYYY'] = datetime.datetime.now().strftime("%d/%m/%Y")
Update_inst.loc[6, 'Bank_name'] = 'ACB'


# Check if the request was successful (status code 200)
#if acb.status_code == 200:
#driver timeout to stop forever loading
driver.implicitly_wait(30)

#get page html content
ACB_html_content = driver.page_source
    
    # Parse the HTML content using BeautifulSoup
ACB_soup = BeautifulSoup(ACB_html_content, 'html.parser')
    
    # Find the CASA_int value and convert it to float
casa = ACB_soup.find_all('span', class_='font6')[0].text

    # Find and convert offline and online values to float using list comprehension
offline_values_1M = [convert_to_float(ACB_soup.find_all("tbody")[1]\
                                      .find_all("tr")[5]\
                                        .find_all("td", class_="xl68")[0]\
                                            .text.strip())]
offline_values = [convert_to_float(ACB_soup.find_all("tbody")[1]\
                                   .find_all("tr")[x]\
                                   .find_all("td")[1]\
                                    .text.strip()) for x in [6, 7, 10, 12,13,15,16,17]]
online_values = [convert_to_float(ACB_soup.find_all("tbody")[3]\
                                  .find_all("tr")[2]\
                                  .find_all("td")[y]\
                                    .text.strip()) for y in [2, 4, 5, 6, 6]]
surplus_values = [convert_to_float(ACB_soup.find_all("tbody")[2]\
                                  .find_all("tr")[1]\
                                  .find_all("td")[x]\
                                    .text.strip()) for x in [1,2,3]]

# Update the DataFrame with the converted values
Update_inst.loc[1, ["Volume_type"]] = 'U300M'
Update_inst.loc[1, ["Off_1M"]] = offline_values_1M + surplus_values[0]
Update_inst.loc[1, ["Off_2M","Off_3M", "Off_6M", "Off_12M","Off_13M","Off_18M", "Off_24M", "Off_36M"]] = offline_values+ surplus_values[0]
Update_inst.loc[1, ["Onl_1M","Onl_3M", "Onl_6M", "Onl_12M","Onl_13M","Onl_18M", "Onl_24M", "Onl_36M"]] = online_values+ surplus_values[0]

Update_inst.loc[2, ["Volume_type"]] = 'U10B'
Update_inst.loc[2, ["Off_1M"]] = offline_values_1M+ surplus_values[1]
Update_inst.loc[2, ["Off_2M","Off_3M", "Off_6M", "Off_12M","Off_13M","Off_18M", "Off_24M", "Off_36M"]] = offline_values+ surplus_values[1]
Update_inst.loc[2, ["Onl_1M","Onl_3M", "Onl_6M", "Onl_12M","Onl_13M","Onl_18M", "Onl_24M", "Onl_36M"]] = online_values+ surplus_values[1]

Update_inst.loc[3, ["Volume_type"]] = '10B'
Update_inst.loc[3, ["Off_1M"]] = offline_values_1M+ surplus_values[2]
Update_inst.loc[3, ["Off_2M","Off_3M", "Off_6M", "Off_12M","Off_13M","Off_18M", "Off_24M", "Off_36M"]] = offline_values+ surplus_values[2]
Update_inst.loc[3, ["Onl_1M","Onl_3M", "Onl_6M", "Onl_12M","Onl_13M","Onl_18M", "Onl_24M", "Onl_36M"]] = online_values+ surplus_values[2]

#close driver
driver.close()

# print(type(surplus_values))
