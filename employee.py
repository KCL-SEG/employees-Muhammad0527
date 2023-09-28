"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, bonus, **kwargs):
        self.name = name
        self.bonus = bonus
        self.income = 0
        self.comission = False
        self.description = ""
        if kwargs:
            self.comission = True
            self.numberOfContracts = kwargs.get("numberOfContracts")
            self.comissionPerContract = kwargs.get("comissionPerContract")


    def get_pay(self):
        if self.bonus:
            return self.income + self.bonus
        elif self.comission: 
            return self.income + (self.numberOfContracts *  self.comissionPerContract)
        else:
            return self.income

    def __str__(self):
        self.get_description()
        return self.description
    
    def get_description(self):
        if self.bonus:
            self.description = self.description + f" and receives a bonus commission of {self.bonus}"
        elif self.comission:
            self.description = self.description + f" and receives a commission for {self.numberOfContracts} contract(s) at {self.comissionPerContract}/contract"
        self.totalPay = f". Their total pay is {str(self.get_pay())}."
        self.description = self.description + self.totalPay
        return self.description

class SaleryWorker(Employee):
    def __init__(self, name, salary, bonus=0, **kwargs):
        super().__init__(name, bonus, **kwargs)
        self.income = salary
        
    def __str__(self):
        self.description = f"{self.name} works on a monthly salary of {self.income}"
        super().__str__()
        return self.description
    
class WageWorker(Employee):
    def __init__(self, name, hours, wage, bonus=0, **kwargs):
        super().__init__(name, bonus, **kwargs)
        self.wage = wage
        self.hours = hours
        self.income = self.wage * self.hours

    def __str__(self):
        self.description = f"{self.name} works on a contract of {self.hours} hours at {self.wage}/hour"
        super().__str__()
        return self.description
    
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SaleryWorker('Billie',4000)
print(billie.get_pay())
print(billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = WageWorker('Charlie', 100, 25)
print(charlie.get_pay())
print(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SaleryWorker('Renee', 3000, numberOfContracts=4, comissionPerContract=200)
print(renee.get_pay())
print(renee)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = WageWorker('Jan', 150, 25, numberOfContracts=3, comissionPerContract=220)
print(jan.get_pay())
print(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SaleryWorker('Robbie', 2000, 1500)
print(robbie.get_pay())
print(robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = WageWorker('Ariel', 120, 30, 600)
print(ariel.get_pay())
print(ariel)


