class samochoelektryczny:
    def __init__(self, max_zasieg):
        self.max_zasieg = max_zasieg
        self.zasieg_chwilowy = max_zasieg
        
    def laduj(self):
        self.zasieg_chwilowy = self.max_zasieg
    
    def jedz(self, kilometry):
        self.kilometry = kilometry
        if kilometry < self.zasieg_chwilowy:
            print(kilometry)
            self.zasieg_chwilowy -= kilometry
        else:
            print(self.zasieg_chwilowy)
            self.zasieg_chwilowy = 0
    
    def waga(self, kilogramy):
        self.kilogramy = kilogramy
        if kilogramy >= 1300:
            if self.max_zasieg > 600:
                print("Samochod nie wyruszy w tak dluga trase")
            else:
                print("Samochod ledwo pojedzie ale da rade")
        elif kilogramy < 1300:
            if self.max_zasieg < 600:
                print("Samochod na spokojnie pojedzie w taka droge")
            else:
                print("Nie wyruszy w tak dluga droge")
    
    def kolor(self, kolorek):
        self.kolor = kolorek
        print("Twoj samochod ma kolor "+ kolorek)
           

    def stats(self):
        print("Waga: " + str(self.kilogramy) + " kg")
        print("Droga: " + str(self.kilometry) + " km")
        print("Kolor samochodu: " + self.kolor)
    
    
s1 = samochoelektryczny(160)

s1.kolor('niebieski')

s1.waga(1200)

s1.jedz(50)
s1.jedz(60)
s1.jedz(200)    

s1.stats()