from random import randint as rand
from math import *
table = []
n = 101

for i in range(2,n):
    table.append(i)

i = 2
j = 0
while i <= sqrt(n-1):
    for j in range(len(table)-1):
        if table[j] % i == 0 and table[j] != i:
            table.pop(j)
    i += 1

print(table)

