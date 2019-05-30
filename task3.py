with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()

print('длинна строки - ', len(content))
print('количество слов - ', len(content.split()))
content = content.replace('.','!')
    
with open('referat2.txt', 'w', encoding='utf-8') as f:
    f.write(content)