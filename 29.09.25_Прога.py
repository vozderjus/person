#1
# n = int(input())
# print(str(n) + 'C = ' + str((n*9.5) + 32) + 'F') 
# print(str(n) + 'C = ' + str(n + 273.15) + 'K')

#2
# n = int(input())

# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# if n > 0:
#     print('Положительное')
# elif n < 0:
#     print('Отрицательное')
# else:
#     print('Ноль')

# if 10 <= n <= 50:
#     print('Принадлежит диапоазону [10;50]')
# else:
#     print('Не принадлежит диапазону [10;50]')

#3
# import random
# from string import * 
# letters = (random.choices(ascii_uppercase, k=3))
# numbers = random.choices('0123456789',  k=3)
# symbols = random.choices('!@#$%^&*', k=2)
# random.shuffle(letters+numbers+symbols)
# print(''.join(p))

#4
# s = input().lower()

# counts = dict()
# for i in s:
#     counts[i] = counts.get(i, 0) + 1

# print('\n'.join(f'{i[0]}: {i[1]}' for i in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]))
