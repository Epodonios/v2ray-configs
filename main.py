import os
import requests
from bs4 import BeautifulSoup




    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            content = file.read()
        
        new_content = content.replace('Eliv2ray', 'abding')
        
        with open(file_path, 'w') as file:
            file.write(new_content)

