1
n = int(input())
print(str(n) + 'C = ' + str((n*9.5) + 32) + 'F') 
print(str(n) + 'C = ' + str(n + 273.15) + 'K')

2
n = int(input())

if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

if n > 0:
    print('Положительное')
elif n < 0:
    print('Отрицательное')
else:
    print('Ноль')

if 10 <= n <= 50:
    print('Принадлежит диапоазону [10;50]')
else:
    print('Не принадлежит диапазону [10;50]')

3
import random
from string import * 
letters = (random.choices(ascii_uppercase, k=3))
numbers = random.choices('0123456789',  k=3)
symbols = random.choices('!@#$%^&*', k=2)
random.shuffle(letters+numbers+symbols)
print(''.join(p))

4
from collections import Counter

s = input().lower()
count = Counter(s)

print(count)
print(count.most_common(3))

5
n = int(input())
p = []
check = [True] * (n + 1)
for i in range(2, n + 1):
    if check[i]:
        p.append(i)
        for j in range(i * 2, n + 1, i):
            check[j] = False
print(p)

6
n = int(input())
s = ''
for i in range(1,n + 1):
    s = s + str(i)
print(s[n-1])
