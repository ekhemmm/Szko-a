class pizza:
    def __init__(self):
        self.ingredients = []
        self.price = 0
        
    def addIngredient(self, ingredient):
        if type(ingredient) == str:
            self.ingredients.append(ingredient)
            print("Dodano skladnik: " + ingredient)
        else:
            print("Wprowadzono zly skladnik")
            
    def showIngredients(self):
        print(self.ingredients)
        
    def pizzaSize(self, size):
        if(size == 'L'):
            print("Pizza jest duza")
            self.price += 40
        elif(size == 'M'):
            print("Pizza jest srednia")
            self.price += 30
        elif(size == 'S'):
            print("Pizza jest mala")    
            self.price += 20
        else:
            print("Wprowadzono zly rozmiar pizzy")
    
    def pizzaPrice(self):
        self.price += len(self.ingredients) * 5        
        print("Pizza kosztuje: " + str(self.price) + "zl")
        
pizza1 = pizza()

pizza1.addIngredient('Ser')
pizza1.addIngredient('Pomidor')

pizza1.addIngredient(123)

pizza1.showIngredients()

pizza1.pizzaSize("S")
pizza1.pizzaPrice()