class Person:
    instances = 0
    def __init__(self, name = "", id = 0):
        self.__name = name
        self.__id = id
        Person.instances += 1

    def copy(self, other_person):
        self.__id = other_person.__id
        self.__name = other_person.__name

    def output(self, arg):
        if self.__name:
            print(f"Cześć {arg}, mam na imie {self.__name}.")
        else:
            print("Brak danych")

pers1 = Person()

pers2 = Person(1, "Maciek")

pers3 = Person()
pers3.copy(pers2)

pers1.output("Adam")
pers2.output("Marek")
pers3.output("Maciek")

print(f"Liczba instancji: {Person.instances}")

    
