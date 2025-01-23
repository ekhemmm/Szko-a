tl=77
n=float(input("podaj dowolna liczbe calkowita: "))

while(n!=tl):
    print("to nie ta liczba sprobuj ponownie!!!")
    if n < tl:
        print("wyzej")
    else:
        print("nizej")
    
    n=float(input("podaj dowolna liczbe calkowita: "))

print(n," to ta liczba!!!")