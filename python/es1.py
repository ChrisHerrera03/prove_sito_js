def is_even(num):
    return num % 2 == 0

class Product:
    def __init__(self,name,price):
        self.price = price
        self.name = name
    
    def __str__(self):
        return f"{self.name}: {self.price}$"
    
    def apply_discount(self,percent):
        valore = (self.price * percent) / 100
        self.price -= valore
        return self.price

prod1 = Product("mela",10)
prod2 = Product("pizza",5)
prod2.apply_discount(10)

def safe_divide(a,b):
    try:
        return a / b
    except ArithmeticError:
        return "Impossibile fare divisione per 0"

def opendata(data):
    total = 0
    try:
        with open(data) as f:
            for line in f:
                total += int(line)
            return total
    except FileNotFoundError:
        return "File inesistente"
    except ValueError: 
        return "Non si può"

print(opendata("data.txt"))