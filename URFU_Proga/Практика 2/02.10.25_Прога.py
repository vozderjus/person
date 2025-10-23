# Шифр цезаря
from string import ascii_lowercase
s = input()
eng = list(ascii_lowercase)
ru = [chr(i) for i in range(ord('а'), ord('а') + 32)]
def shifr_ru(s, num, ru):
    print('Я шифрую текст')
    shifr_s = ''
    for i in s:
        if i == ' ':
            shifr_s += ' '
        else:
            shifr_s += ru[ru.index(i)+num]
    return shifr_s

def deshifr_ru(s, num, ru):
    ru = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])

    print('Я шифрую текст')
    deshifr_s = ''
    for i in s:
        if i == ' ':
            deshifr_s += ' '
        else:
            deshifr_s += ru[ru.index(i)-num]
    return deshifr_s


def shifr(s, num, eng):
    print('Я шифрую текст')
    shifr_s = ''
    for i in s:
        if i == ' ':
            shifr_s += ' '
        else:
            shifr_s += ascii_lowercase[ascii_lowercase.index(i)+num]
    return shifr_s

def deshifr(s, num, eng):
    print('Я дешифрую текст')
    deshifr_s = ''
    for i in s:
        if i == ' ':
            deshifr_s += ' '
        else:    
            deshifr_s += ascii_lowercase[ascii_lowercase.index(i)-num]
    return deshifr_s

print('Шифрование или Дешифрование? (0/1)')
n = int(input())
print('Какой шаг?')
num = int(input())


if not set(ru).isdisjoint(s.lower()):
    if n == 0:
        print('Шифрованный текст: ' + shifr_ru(s.lower(), num, ru))
    else:
        print('Дешифрованный текст: ' + deshifr_ru(s.lower(), num, ru))
else:
    if n == 0:
        print('Шифрованный текст: ' + shifr(s.lower(), num, eng))
    else:
        print('Дешифрованный текст: ' + deshifr(s.lower(), num, eng))



# олимпиада
scores = list(map(int, input().split(' ')))
student_score = int(input())
print(scores)
def check_winners(scores, student_score):
    if student_score in sorted(scores)[-3:]:
        print('Вы в тройке победителеЙ!')
    else:
        print('Вы не попали в тройку победителей')
    exit()

print(check_winners(scores, student_score))

# пироженки и коробочки
def print_pack_report(n):
    for i in range(n, 0, -1):
        if i % 15 == 0:
            print(str(i) + '- Расфасуем по три или по пять')
        elif i % 5 == 0 and i % 3 != 0:
            print(str(i) + '- Расфасуем по пять')
        elif i % 5 != 0 and i % 3 == 0:
            print(str(i) + '- Расфасуем по 3')
        else:
            print(str(i) + '- не заказываем!')
print(print_pack_report(int(input())))

# сложные пароли
import random 
from string import *
def password(a, length):
    answer = ''
    if length < len(a):
        return 'Вы ввели длину меньше, чем возможное количество различных символов!'
    n = length // len(a) #сколько символов точно влезает
    ost = length % len(a)
    for i in a:
        if ost > 0:
            answer += ''.join(random.choices(i, k=n+1))
        else:
            answer += ''.join(random.choices(i, k=n))
        ost -= 1
    answer = list(answer)
    random.shuffle(answer)
    return ''.join(answer)
    
print('Введите длину желаемого пароля: ')
length = int(input())
a = []
print('Добавить верхний регистр? (0/1)')
if int(input()) == 1:
    a.append(ascii_uppercase)
print('Добавить нижний регистр? (0/1)')
if int(input()) == 1:
    a.append(ascii_lowercase)
print('Добавить символы? (0/1)')
if int(input()) == 1:
    a.append('!@#$%^&*')
print('Добавить цифры? (0/1)')
if int(input()) == 1:
    a.append('0123456789')
print(password(a, length))

# Римский конвертер

nums = {
    '0': 0,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
def r_to_a(n):
    answer = 0
    n = '0' + n
    for i in range(len(n) - 1):
        
        if nums.get(n[i]) > nums.get(n[i + 1]):
            answer -= nums.get(n[i + 1])
        else:
            answer += nums.get(n[i + 1])
    return answer

def a_to_r(n):
    if n < 1 or n > 3999:
        return "Только числа от 1 до 3999"
    
    thousands = n // 1000
    hundreds = (n % 1000) // 100
    tens = (n % 100) // 10
    ones = n % 10
    
    result = ""
    
    result += "M" * thousands
    
    if hundreds == 9:
        result += "CM"
    elif hundreds >= 5:
        result += "D" + "C" * (hundreds - 5)
    elif hundreds == 4:
        result += "CD"
    else:
        result += "C" * hundreds
    
    if tens == 9:
        result += "XC"
    elif tens >= 5:
        result += "L" + "X" * (tens - 5)
    elif tens == 4:
        result += "XL"
    else:
        result += "X" * tens
    
    if ones == 9:
        result += "IX"
    elif ones >= 5:
        result += "V" + "I" * (ones - 5)
    elif ones == 4:
        result += "IV"
    else:
        result += "I" * ones
    
    return result


print('Программа принимает только одно число')
n = input()
if n.isdigit():
    print(reversed(a_to_r(int(n))))
else:
    print(r_to_a(n))
