import json
import re
from datetime import datetime

with open("../operations.json", "r", encoding="utf-8") as file:
    readed_json = file.read()
    operations = json.loads(readed_json)

c = []
for i in operations:
    '''Сортируем файл json по дате, котору мы переводим в формат datetime и добавляем в новый список'''
    if "state" in i and i["state"] == "EXECUTED":
        i["date"] = datetime.strptime(i["date"],'%Y-%m-%dT%H:%M:%S.%f')
        c.append(i)
c = sorted(c,key=lambda x:x["date"])[::-1]

def lust_op():
    '''Спрашиваем сколько операций нужно вывести'''
    # x = int(input("Сколько последних операций вы хотите вывести?  "))
    # d = c[0:x]
    d = c[0:5]
    return d
# print(lust_op())
# d = c[0:5]
# print(d)

def output(f):
    '''Выводим последние и подкоректированные операции'''
    for x in f:
        c = x['to']
        to_number = re.sub('[\D]', '', c)
        to_words = re.sub('[\d]', '', c)
        if "from" in x:
            n = x['from']
            number = re.sub('[\D]', '', n)
            cards = re.sub('[\d]', '', n)
            print(f"{x['date'].date()} {x['description']}\n{cards}{number[:4]} {number[4:6]}** **** {number[-4:]} --> {to_words}**{to_number[-4:]}\n{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}")
        else:
            print(f"{x['date'].date()} {x['description']}\n{to_words}**{to_number[-4:]}\n{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}")

output(lust_op())


