# باز کردن فایل برای خواندن
with open('All_Configs_Sub.txt', 'r') as file:
    file_content = file.read()

# جایگزینی همه وقوع‌های 'Outline_vpn@' با 'epodonios'
file_content = file_content.replace('Outline_vpn', 'epodonios')

# باز کردن فایل برای نوشتن و ذخیره محتوای تغییر یافته
with open('All_Configs_Sub.txt', 'w') as file:
    file.write(file_content)

print("جایگزینی انجام شد و فایل با موفقیت ذخیره شد.")
