# Open the file Sub1.txt in read mode
with open('All_Configs_Sub.txt', 'r') as file:
    data = file.read()

# Replace all occurrences of 'Eliv2ray' with 'Hello'
data = data.replace('Eliv2ray', 'Hello')

# Open the file Sub1.txt in write mode and write the modified data
with open('All_Configs_Sub.txt', 'w') as file:
    file.write(data)
