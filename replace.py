with open('All_Configs_Sub.txt', 'r') as file:
    content = file.read()

content = content.replace('Eliv2ray', 'Hello')
content = content.replace('ipv2ray', 'Hello')

with open('All_Configs_Sub.txt', 'w') as file:
    file.write(content)
