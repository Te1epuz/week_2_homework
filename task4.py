import csv

user_list = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

print(user_list)

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user) # почему в итоговом файле пустые строки есть ???


# А этим читать csv файл
with open('export.csv', 'r', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    reader = csv.DictReader(f, fields, delimiter=';')
    new_user_list = []
    for row in reader:
        new_user_list.append(dict(row)) # без дикт сохраняло ерунду какую-то
        print(dict(row))

print(new_user_list)