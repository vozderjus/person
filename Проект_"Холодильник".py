import datetime
from decimal import Decimal
  
goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
       {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':\
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None):
    if title not in items:
        if expiration_date is not None:
            items[title] = [{'amount': amount, 'expiration_date' datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()}]
        else:
            item[title] = [{'amount': amount,'expiration_date': expiration_date}]
    else:
        if expiration_date is not None:
            items[title].append({'amount': amount,'expiration_dae': datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()})
        else:
            item[title].append({'amount': amount, 'expiration_date': expiration_date})
    return items
  
def add_by_note(items, note):
    parts = note.split()
    try:
        datetime.datetime.strptime(parts[-1], DATE_FORMAT)
        expiration_date = parts[-1]
        remaining_parts = parts[:-1]
    except (ValueError, IndexError):
        expiration_date = None
        remaining_parts = parts
  
    try:
        amount = Decimal(remaining_parts[-1])
        title = ' '.join(remaining_parts[:-1])
    except:
        title = ' '.join(remaining_parts)
        amount = Decimal('1')
        print(f'Количество не указано, используем по умолчанию: 1')
  
    return add(items, title, amount, expiration_date)
print(add_by_note(goods, 'Дата+ 4 2025-12-10'))
print(add_by_note(goods, 'Дата- 4'))
print(add_by_note(goods, 'Пробелы Пробелы Дата+ 4 2025-12-10'))
print(add_by_note(goods, 'Пробелы Пробелы Дата- 4'))

  
def find(items, needle):
    result = []
    for keys in items:
        if needle.lower() in keys.lower():
            result.append(keys)
    return result
print(find(goods, 'у'))
  
def amount(items, needle):
    result = Decimal('0')
    lst = find(items, needle)
    for item in lst:
        for am in items.get(item):
            result += Decimal(str(am.get('amount')))
    return result
print(amount(goods, 'Пельмени'))
