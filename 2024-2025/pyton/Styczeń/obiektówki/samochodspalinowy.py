class samochod_spalinowy:
    def __init__(self, max_zasieg):
        self.max_zasieg = max_zasieg
        self.zasieg_chwilowy = max_zasieg
        self.max_bagu = 56
        self.stan_akt = 0
        
    def tankuj(self):
        self.zasieg_chwilowy = self.max_zasieg
    
    def zatankuj(self, benzyna):
        if(self.stan_akt < self.max_bagu):
            if(self.stan_akt + benzyna > self.max_bagu):
                self.stan_akt += benzyna
                while self.stan_akt > self.max_bagu:
                    self.stan_akt -= 1;
                print("Osiagnieto maksymalna pojemnosc bagu")
                print("Ilosc paliwa " + str(self.stan_akt) + " l")
            else:
                self.stan_akt += benzyna
                print("Ilosc paliwa " + str(self.stan_akt) + " l")
    
    def jedz(self, kilometry):
        self.kilometry = kilometry
        if kilometry < self.zasieg_chwilowy:
            print(kilometry)
            self.zasieg_chwilowy -= kilometry
        else:
            print(self.zasieg_chwilowy)
            self.zasieg_chwilowy = 0
    
    def kolor(self, kolorek):
        self.kolor = kolorek
        print("Twoj samochod ma kolor "+ kolorek)
           

    def stats(self):
        print("Waga: " + str(self.kilogramy) + " kg")
        print("Droga: " + str(self.kilometry) + " km")
        print("Kolor samochodu: " + self.kolor)
    
    
s1 = samochod_spalinowy(160)

s1.zatankuj(42)