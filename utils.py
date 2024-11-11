import json


def load_file():
    """Загружаем исходные данные из файла operations.json"""
    with open('operations.json', 'r', encoding='utf-8') as file:
        json_load = json.load(file)
    return json_load

load_file()

def sort_info():
    """Сортируем наш список по статусу EXECUTED
    и самым последним операциям по дате"""
    operations = []
    data = load_file()
    for i in data:
        if i.get("state") == "EXECUTED":
            operations.append(i)
    return sorted(operations, key=lambda x: x["date"], reverse=True)[:5]

print(sort_info()



def get_number(number):
    """Преобразуем номер карты и номер счета в необходимый формат
    Maestro 1913883747791351 -> 1913 88** **** 1351
    Счет 72645194281643232984 -> **2984 """
    pass


def get_date(date):
    """Преобразуем дату в необходимый формат
    2019-02-12T00:08:07.524972 -> 12.02.2019"""
    pass


def get_message():
    """Принимаем дату, от, кому и преобразуем в формате
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб"""
    pass
