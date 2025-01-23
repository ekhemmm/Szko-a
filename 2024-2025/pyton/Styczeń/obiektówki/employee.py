class Employee:
    def __init__(self, name, lastname, hourly_rate):
        self.name = name
        self.lastname = lastname
        self.salary = 0
        self.hourly_rate = hourly_rate
    
    def register_time(self, hours):
        self.hours = hours
        if(hours<=8):
            self.salary =+ hours * self.hourly_rate
        elif(hours>8):
            self.salary =+ self.hourly_rate * 8 + (self.hourly_rate * 2) * (hours-8)          
    
    def pay_salary(self):
        print("Employees salary: " + str(self.salary))
        self.salary = 0
        
employee1 = Employee('Jan', 'Kowalski', 100.0)
employee1.register_time(5)
employee1.pay_salary()
employee1.pay_salary()
employee1.register_time(10)
employee1.pay_salary()