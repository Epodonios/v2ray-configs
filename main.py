import os
import requests
from bs4 import BeautifulSoup

# باز کردن فایل All_Configs_Sub.txt
with open('All_Configs_Sub.txt', 'r') as file:
    data = file.read()

# اعمال تغییرات
data = data.replace('@ElliV2ray', 'apple')

# ذخیره تغییرات در فایل
with open('All_Configs_Sub.txt', 'w') as file:
    file.write(data)

print("تغییرات با موفقیت اعمال شد.")

