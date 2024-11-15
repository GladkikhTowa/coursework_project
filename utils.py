import json
import datetime


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


sort_info()


def get_number():
    """Преобразуем номер карты и номер счета в необходимый формат
    Maestro 1913883747791351 -> 1913 88** **** 1351
    Счет 72645194281643232984 -> **2984 """
    number = sort_info()
    for num in number:
        if 'from' in num:
            if num['from'].startswith('Visa Classic'):
                print(f"{num['from'][:19]}** ****{num['from'][25:]} ---> **{num['to'][21:]}")
            elif num['from'].startswith('Maestro'):
                print(f"{num['from'][:17]}** ****{num['from'][20:]} ---> **{num['to'][21:]}")
            elif num['from'].startswith('Счет'):
                print(f"{num['from'][:5]} ****{num['from'][21:]} ---> **{num['to'][21:]}")
        else:
            print(f"---> **{num['to'][21:]}")


get_number()


def get_date():
    """Преобразуем дату в необходимый формат
    2019-02-12T00:08:07.524972 -> 12.02.2019"""
    date_form = sort_info()
    date_list = []
    for date in date_form:
        date_str = datetime.datetime.strptime(date['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%S:%M:%H %d-%m-%Y')
        date_list.append((date_str[9:].replace('-', '.')))
    date_s = '\n'.join(date_list)
    return date_s


get_date()


def get_message():
    """Принимаем дату, от, кому и преобразуем в формате
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб"""
    pass
