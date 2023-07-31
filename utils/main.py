# import json
#
# with open("operations.json", "r", encoding="utf-8") as file:
#     readed_json = file.read()
#     operations = json.loads(readed_json)
#
#
# print(operations[0]["id"])

class Hero:

   def __init__(self, name):
     self.name = name
     print("Я", self.name)

hero_1 = Hero("Печений")
hero_2 = Hero("Нечений")
hero_3 = Hero("Имбирний первый")

print(hero_1.name)
print(hero_2.name)
print(hero_3.name)
