from random import randint as rand
table = []

for j in range(10):
    table.append(rand(1,20))

class sortowanie():
    def __init__(self, tab = []):
        self.tab = tab
    
    def sortuj(self):
        for i in range(1, len(self.tab)):
            for j in range(0,i):
                if(self.tab[i] < self.tab[j]):
                    self.tab.insert(j, self.tab[i])
                    self.tab.pop(i+1)
                    print(self.tab)
                    break
        return self.tab

s1 = sortowanie(table)
print(table)
print(s1.sortuj())