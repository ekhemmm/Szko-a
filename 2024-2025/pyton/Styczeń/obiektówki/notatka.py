class notatka():
    counter = 0
    def __init__(self, id = 0, name = "", content = ""):
        self.__name = name
        self.__id = id
        self.__content = content

    def input(self, namein, contentin):
        notatka.counter += 1
        self.__id = notatka.counter
        self.__name = namein
        self.__content = contentin
    
    def show(self):
        print("\n" + "Tytuł notatki: " + self.__name)
        print(self.__content + "\n")

    

n1 = notatka()
n2 = notatka()
n3 = notatka()

n1.input("takajaka", "Lubie jesc placki")
n1.show()

n2.input("xd", ":))))")
n2.show()

n3.input("lol", "śigma")
n3.show()


