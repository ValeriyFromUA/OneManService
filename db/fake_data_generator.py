from typing import List, Dict, NoReturn

import requests
from random import choice, randint
from bs4 import BeautifulSoup

DEFECTS = ['не вмикається', 'перегрівається', 'іноді вимикається', 'залиття рідиною', 'повільно працює']
SHAPES = ['потертості, подряпини', 'тріщини на корпусі', 'новий', 'сліди залиття']
KIT = ['ФГТ, інструкція', 'акумулятор', 'відсутня', 'зарядний пристрій']
STATUS = ['is waiting', 'in work', 'done']
DIAGNOSIS = ['вовчанка', 'потрібна заміна ЦП', 'необхідний ремонт ланцюгів живлення', 'заміна відеочіпа',
             'необіхдно дадати SSD']
FIRST_NAMES = ['Василь', 'Петро', 'Остап', 'Аліна', 'Марія', 'Валерій']
LAST_NAMES = ['Василенко', 'Шевченко', 'Комар', 'Франко', 'Бех', 'Фесенко']
STREETS = ['Перемоги', 'Лифаря', 'Бандери', 'Шолуденка', 'Прирічна', 'Шевченка']

DEVICES = ['Ноутбук ACER Aspire 5 A515-45-R2YC Pure Silver (NX.A84EU.009)',
           'Ноутбук LENOVO IdeaPad 3 15IML05 Business Black (81WB00VFRA)',
           'Ноутбук ACER Nitro 5 AN517-54-54ZU Shale Black (NH.QF8EU.00N)',
           'Ноутбук ACER Nitro 5 AN515-57-765K Shale Black (NH.QEWEU.00P)',
           'Ноутбук ASUS Vivobook 16X M1603QA-MB195 Transparent Silver (90NB0Y82-M00BP0)',
           'Ноутбук ASUS X515EP-BQ262 Transparent Silver (90NB0TZ2-M03780)',
           'Ноутбук ASUS TUF Gaming FX506HM-HN017 Eclipse Gray (90NR0753-M01170)',
           'Ноутбук ACER Swift 3 SF314-43-R2DX Silver (NX.AB1EU.00G)',
           'Ноутбук ASUS X515EA-EJ1742 Transparent Silver (90NB0TY2-M02MT0)',
           'Ноутбук LENOVO IdeaPad 3 15ITL6 Arctic Grey (82H8020CRA)',
           'Ноутбук ACER Nitro 5 AN515-58-75T1 Obsidian Black (NH.QFLEU.008)',
           'Ноутбук Acer Nitro 5 AN517-41-R8RE Shale Black (NH.QAREU.00B)',
           'Ноутбук Nitro 5 AN517-54-50ML Shale Black (NH.QF8EU.002)',
           "Ноутбук APPLE A2337 MacBook Air 13' M1 256GB Space Grey 2020 (MGN63)",
           'Ноутбук ACER Nitro 5 AN515-55-53VH Black (NH.Q7MEU.01F)',
           'Ноутбук ASUS VivoBook X712EA-BX820 Transparent Silver (90NB0TW1-M00J20)',
           'Ноутбук LENOVO IdeaPad 5 Pro 16IAH7 Cloud Grey (82SK0084RA)',
           'Ноутбук ASUS Vivobook Pro 15 OLED M6500QC-L1088 Quiet Blue (90NB0YN1-M006V0)',
           'Ноутбук ACER Swift 3 SF314-43-R765 Pure Silver (NX.AB1EU.00D)',
           'Ноутбук ASUS PRO ExpertBook B5302CEA-L50742R Star Black (90NX03S1-M00BV0)',
           'Ноутбук ACER Nitro 5 AN515-58-55VF Obsidian Black (NH.QFMEU.00H)',
           'Ноутбук LENOVO Legion 5 15IMH05H Phantom Black (81Y600SYRA)',
           'Ноутбук ACER Aspire 3 A315-57G-36EU Black (NX.HZREU.016)',
           'Ноутбук TUF Gaming F15 ASUS FX506HE-HN008 Eclipse Gray (90NR0703-M01460)',
           "Ноутбук APPLE A2337 MacBook Air 13' M1 256GB Gold 2020 (MGND3)",
           "Ноутбук APPLE A2337 MacBook Air 13' M1 256GB Silver 2020 (MGN93)",
           'Ноутбук ASUS Vivobook Pro K6500ZC-MA301 Quiet Blue (90NB0XK1-M00JB0)',
           'Ноутбук ASUS X515EA-BQ311 Transparent Silver (90NB0TY2-M23280)',
           'Планшет LENOVO IdeaPad Duet 3 10.3" 4/128GB LTE grey (82HK005TRA)',
           'Ноутбук ASUS ROG Strix G15 G513IM-HN008 Eclipse Gray (90NR0522-M005M0)',
           'Ноутбук LENOVO IdeaPad Duet 3 10.3 Graphite Gray (82AT00LDRA)',
           'Ноутбук APPLE MacBook Air M2 256 Gb Silver (MLXY3UA/A)',
           'Ноутбук ASUS Laptop M515DA-BR903 Slate Grey (90NB0T41-M15140)',
           'Ноутбук LENOVO ThinkBook 15 Mineral Gray (20VE00G2RA)',
           'Ноутбук ASUS TUF Gaming F15 FX506HCB-HN200 Graphite Black (90NR0724-M00NK0)',
           'Ноутбук LENOVO IdeaPad 3 15ITL6 Arctic Grey (82H800ULRA)',
           'Ноутбук LENOVO IdeaPad 5 Pro 14IAP7 Cloud Grey (82SH005YRA)',
           'Ноутбук ASUS FX507ZM-HN047 (90NR09A2-M00810)',
           'Ноутбук ACER Aspire 3 A315-23-R4H7 Charcoal Black (NX.HVTEU.033)',
           'Ноутбук ASUS X515JA-EJ2804 Peacock Blue (90NB0SR3-M02R90)',
           'Ноутбук ACER Nitro 5 AN517-41-R11E Black (NH.QAQEU.008)', 'Ноутбук ASUS FX507ZM-HN044 (90NR09A2-M00770)']


def generate_order_data() -> List[Dict]:
    orders = []
    for device in DEVICES:
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


def create_fake_customers() -> List[Dict]:
    customers = []
    for _ in range(len(DEVICES)):
        data = {
            'first_name': choice(FIRST_NAMES),
            'last_names': choice(LAST_NAMES),
            'phone': f'+38011{randint(1000000, 9999999)}',
            'email': f'fake_user{randint(100, 999)}@gmail.com',
            'address': f'{choice(STREETS)}, {randint(1, 40)}'
        }
        customers.append(data)
    return customers


def add_customer_to_order_id():
    order_id = list(range(1, 43))
    customer_id = list(reversed(order_id))
    return order_id, customer_id
