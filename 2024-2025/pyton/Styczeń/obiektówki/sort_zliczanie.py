from random import randint as rand

class zliczanie():
    def __init__(self, tab = [], diction = {}, sorted = []):
        self.__tab = tab
        self.__diction = diction
        self.__sorted = sorted

    def fill(self):
        for i in range(10):
            self.__tab.append(rand(1,20)) 
        return "Table: " + str(self.__tab)

    def dictionary(self):
        for i in range(max(self.__tab)):
            n = 0
            for j in self.__tab:
                if i+1 == j:
                    n += 1
            self.__diction.update({(i+1):n})
        return "Dictionary: " + str(self.__diction)
    
    def sorting(self):
        for i in range(1,21):
            if self.__diction.get(i, 0) > 0:
                for _ in range(self.__diction[i]):
                    self.__sorted.append(i)
        return "Sorted table: " + str(self.__sorted)

tab = []
table1 = zliczanie(tab)
print(table1.fill())
print(table1.dictionary())
print(table1.sorting())
