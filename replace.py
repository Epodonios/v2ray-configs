file_path = "Sub7.txt"

# باز کردن فایل و خواندن محتوا
with open(file_path, "r") as file:
    content = file.read()

# جایگزینی همه کلمات ipv2ray با mmd
new_content = content.replace("ipv2ray", "mmd")

# آپدیت فایل با محتوای جدید
with open(file_path, "w") as file:
    file.write(new_content)

print("همه کلمات 'ipv2ray' در فایل جایگزین شدند.")
