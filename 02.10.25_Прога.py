# # Шифр цезаря
# from string import ascii_lowercase
# s = input()
# eng = list(ascii_lowercase)
# ru = [chr(i) for i in range(ord('а'), ord('а') + 32)]
# def shifr_ru(s, num, ru):
#     print('Я шифрую текст')
#     shifr_s = ''
#     for i in s:
#         if i == ' ':
#             shifr_s += ' '
#         else:
#             shifr_s += ru[ru.index(i)+num]
#     return shifr_s

# def deshifr_ru(s, num, ru):
#     ru = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])

#     print('Я шифрую текст')
#     deshifr_s = ''
#     for i in s:
#         if i == ' ':
#             deshifr_s += ' '
#         else:
#             deshifr_s += ru[ru.index(i)-num]
#     return deshifr_s


# def shifr(s, num, eng):
#     print('Я шифрую текст')
#     shifr_s = ''
#     for i in s:
#         if i == ' ':
#             shifr_s += ' '
#         else:
#             shifr_s += ascii_lowercase[ascii_lowercase.index(i)+num]
#     return shifr_s

# def deshifr(s, num, eng):
#     print('Я дешифрую текст')
#     deshifr_s = ''
#     for i in s:
#         if i == ' ':
#             deshifr_s += ' '
#         else:    
#             deshifr_s += ascii_lowercase[ascii_lowercase.index(i)-num]
#     return deshifr_s

# print('Шифрование или Дешифрование? (0/1)')
# n = int(input())
# print('Какой шаг?')
# num = int(input())


# if not set(ru).isdisjoint(s.lower()):
#     if n == 0:
#         print('Шифрованный текст: ' + shifr_ru(s.lower(), num, ru))
#     else:
#         print('Дешифрованный текст: ' + deshifr_ru(s.lower(), num, ru))
# else:
#     if n == 0:
#         print('Шифрованный текст: ' + shifr(s.lower(), num, eng))
#     else:
#         print('Дешифрованный текст: ' + deshifr(s.lower(), num, eng))



# # олимпиада
# scores = list(map(int, input().split(' ')))
# student_score = int(input())
# print(scores)
# def check_winners(scores, student_score):
#     if student_score in sorted(scores)[-3:]:
#         print('Вы в тройке победителеЙ!')
#     else:
#         print('Вы не попали в тройку победителей')
#     exit()

# print(check_winners(scores, student_score))

# # пироженки и коробочки
# def print_pack_report(n):
#     for i in range(n, 0, -1):
#         if i % 15 == 0:
#             print(str(i) + '- Расфасуем по три или по пять')
#         elif i % 5 == 0 and i % 3 != 0:
#             print(str(i) + '- Расфасуем по пять')
#         elif i % 5 != 0 and i % 3 == 0:
#             print(str(i) + '- Расфасуем по 3')
#         else:
#             print(str(i) + '- не заказываем!')
# print(print_pack_report(int(input())))

# # сложные пароли

# еще подумать надо


# # Римский конвертер

# nums = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }
# print('Программа принимает только одно число')
# n = input()
# def perevod(n):
#     answer = 0
#     for i in n:
#         answer += nums.get(i)
#     return answer
# print(perevod(n))
