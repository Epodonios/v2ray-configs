import os

directory = 'main'  # نام دایرکتوری مورد نظر
search_word = 'Eliv2ray'  # کلمه‌ای که می‌خواهید جایگزین شود
replace_word = 'epod'  # کلمه‌ای که به جای کلمه قبلی قرار خواهد گرفت

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            content = file.read()
        
        new_content = content.replace(search_word, replace_word)
        
        with open(file_path, 'w') as file:
            file.write(new_content)
