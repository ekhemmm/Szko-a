
h=float(input("ile masz wzrostu w cm: "))
w=float(input("ile wazysz w kg: "))

h=h/100

bmi=w//h**2

print("twoje bmi wynosi: ",bmi)

if(bmi<16):
    print("wyglodzenie")
    
elif(bmi>=16 and bmi<=16.9):
    print("wychodzenie")
    
elif(bmi>=17 and bmi<=18.4):
    print("niedowaga")
    
elif(bmi>=18.5 and bmi<=24.9):
    print("waga prawidlowa")

elif(bmi>=25 and bmi<=29.9):
    print("nadwaga")

elif(bmi>=30 and bmi<=34.9):
    print("otylosc 1 stopnia")

elif(bmi>=35 and bmi<=39.9):
    print("otylosc 2 stopnia")

elif(bmi>=40):
    print("otylosc 3 stopnia")
    


