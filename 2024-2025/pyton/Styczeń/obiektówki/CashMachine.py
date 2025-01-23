class CashMachine:
    def __init__(self):
        self.bills = {}

    def is_available(self):
        if not self.bills:
            print("False")
        else:
            print("True")

    def put_money(self, notes):
        for i in notes:
            if i in self.bills:
                self.bills[i] += 1
            else:
                self.bills[i] = 1

    def withdraw_money(self, amount):
        out = []
        for j in range(len(self.bills)):
            for i in sorted(self.bills.keys())[j::-1]:
                while amount >= i and self.bills.get(i) != 0:
                    amount -= i
                    self.bills[i] -= 1
                    out.append(i)
        if amount == 0:
            print(out)
        else:
            print("Brak możliwości wypłaty☻")
            
bankomat1 = CashMachine()
bankomat1.put_money([100,50,150,10])
bankomat1.is_available()
bankomat1.withdraw_money(150)
bankomat1.withdraw_money(160)
