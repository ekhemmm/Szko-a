class sort():

    def __init__(self, table = []):
        self.__table = table

    def find_max(self, start):
        max_index = start
        for i in range(start + 1, len(self.__table)):
            if self.__table[i] > self.__table[max_index]:
                max_index = i
        return max_index

    def sorting(self):
        n = len(self.__table)
        for j in range(n - 1):
            max = self.find_max(j)
            if max != j:
                self.__table[j], self.__table[max] = self.__table[max], self.__table[j]
            print(self.__table)

table = []

s1 = sort(table)

for i in range(10):
    i = int(input(f"Wprowadź element nr.{(i+1)} do tablicy: "))
    table.append(i)

print(f"Tablica przed sortowaniem: {table}")

s1.sorting()

print(f"Tablica po sortowaniu: {table}")

