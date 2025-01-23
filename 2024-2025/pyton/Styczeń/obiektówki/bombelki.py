from random import randint as rand
table = []

for j in range(100):
    table.append(rand(1,100))

print(table) 

for i in range(len(table)):
    for j in range(len(table)-1):
        x = 0  
        if table[j] > table[j+1]:
            x = table[j]
            table[j] = table[j+1]
            table[j+1] = x   
        print(table)