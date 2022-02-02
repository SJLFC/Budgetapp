class Budget():
    def __init__(self, balance):
        self.balance = balance

    def __repr__(self):
        return f"The remaining balance of this budget is £{self.balance}."

    def withdraw(self, amount):
        self.balance -= amount
        return amount

    def deposit(self, amount):
        self.balance += amount
        return amount

food = Budget(200)
with open("food.txt", "w") as foodvar:
    foodvar.write(str(food.balance))

clothing = Budget(200)
with open("clothing.txt", "w") as clothingvar:
    clothingvar.write(str(clothing.balance))

entertainment = Budget(200)
with open("entertainment.txt", "w") as entertainmentvar:
    entertainmentvar.write(str(entertainment.balance))

print(food)
print(clothing)
print(entertainment)

food.withdraw(50)

print()
print(food)

entertainment.withdraw(food.deposit(50))

    
print()
print(food)
print(entertainment)