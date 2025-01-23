class SimCard:
    def __init__(self):
        self.contacts = []
        
    def addContacts(self, name, number):
        if type(name) == str and type(number) == int and len(str(number)) == 9:
            self.person = {name : number}
            self.contacts.append(self.person)
    
    def deleteContacts(self, name):
        del int(self.contacts)[name] 
    
    def showContacts(self):
        for self.person in self.contacts:
            print(self.person)
            
person1 = SimCard()

person1.addContacts("Ola", 123456789)
person1.addContacts("Adam", 987654332)
person1.addContacts(100, 564738291)
person1.addContacts("Kasia", "numer")

person1.deleteContacts("Ola")

person1.showContacts()