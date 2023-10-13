import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import datetime 

x = requests.get("https://www.vietcombank.com.vn/vi-VN/KHCN/Cong-cu-Tien-ich/KHCN---Lai-suat")
html = x.text

start = html.find("currentDataInterestRate")
end = html.find("}]}")
html_2= html[start:end]

matches = re.findall(r'&quot;rates&quot;:([\d.]+)', html_2)
df = [m[:5] for m in matches]

columns = ['MMYYYY','Bank_name', 'CASA_int', 'Off_1M', 'Off_3M', 'Off_6M', 'Off_1Y', 'Off_2Y', 'Onl_1M', 'Onl_3M', 'Onl_6M','Onl_1Y','Onl_2Y']

Update_inst = pd.DataFrame(columns=columns)

Update_inst.loc[0, 'MMYYYY'] = datetime.datetime.now().strftime("%d/%m/%Y")
Update_inst.loc[0, 'Bank_name'] = 'ACB'
Update_inst.loc[0, 'CASA_int'] = df[0]
Update_inst.loc[0, 'Off_1M'] = df[9]
Update_inst.loc[0, 'Off_3M'] = df[15]
Update_inst.loc[0, 'Off_6M'] = df[18]
Update_inst.loc[0, 'Off_1Y'] = df[24]
Update_inst.loc[0, 'Off_2Y'] = df[27]
Update_inst.loc[0, 'Onl_1M'] = df[70]
Update_inst.loc[0, 'Onl_3M'] = df[71]
Update_inst.loc[0, 'Onl_6M'] = df[72]
Update_inst.loc[0, 'Onl_1Y'] = df[76]
Update_inst.loc[0, 'Onl_2Y'] = df[79]

Update_inst
