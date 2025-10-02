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
