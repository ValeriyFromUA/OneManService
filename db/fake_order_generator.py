from typing import List, Dict

import requests
from random import choice, randint
from bs4 import BeautifulSoup

DEFECTS = ['не вмикається', 'перегрівається', 'іноді вимикається', 'залиття рідиною', 'повільно працює']
SHAPES = ['потертості, подряпини', 'тріщини на корпусі', 'новий', 'сліди залиття']
KIT = ['ФГТ, інструкція', 'акумулятор', 'відсутня', 'зарядний пристрій']
STATUS = ['is wating', 'in work', 'done']
DIAGNOSIS = ['вовчанка', 'потрібна заміна ЦП', 'необхідний ремонт ланцюгів живлення', 'заміна відеочіпа',
             'необіхдно дадати SSD']


def get_device_names() -> List[str]:
    url = 'https://www.foxtrot.com.ua/ru/shop/noutbuki.html?page=2'
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'lxml')
    device_list = []
    devices = soup.find_all("a", class_='card__title')
    for device in devices:
        device = device.text
        device_list.append(device)

    return device_list


def generate_order_data(device_list: List[str]) -> List[Dict]:
    orders = []
    for device in device_list:
        data = {
            'device': device,
            'serial_number': randint(1000, 9999),
            'defect': choice(DEFECTS),
            'shape': choice(SHAPES),
            'kit': choice(KIT),
            'diagnosis': choice(DIAGNOSIS),
            'status': choice(STATUS)
        }
        orders.append(data)
    return orders
