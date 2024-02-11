# باز کردن فایل All_Configs_Sub.txt
with open('All_Configs_Sub.txt', 'r') as file:
    data = file.read()

# اعمال تغییرات
data = data.replace('eliv2ray', 'apple')

# ذخیره تغییرات در فایل
with open('All_Configs_Sub.txt', 'w') as file:
    file.write(data)

print("تغییرات با موفقیت اعمال شد.")
