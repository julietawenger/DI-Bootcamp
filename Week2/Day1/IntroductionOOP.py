"""OOD: object oriented programmig. Day 1"""

class Dog():
    def __init__(self, color, breed, floppy_ears, name):
        self.color = color              # It doesn't belong to Dog, it belongs to peanut, the Dog
        self.breed = breed
        self.floppy_ears = floppy_ears
        self.name = name
        print("A new dog has been initialized.")

    def __str__(self):
        return f"{self.color, self.breed, self.floppy_ears, self.name}"

    def bark(self):
        return f"{self.name} goes WOOF!"
    
    def walk(self, number_of_meters):
        return f"{self.name} walked {number_of_meters} meters."
    
    def sit(self): 
        print(f"{self.name} sits down.")   
        
    def eat(self, food):
        print(f"{self.name} ate {food}.")

    def rename(self, new_name):
        self.name = new_name

peanut = Dog("brown", "beagle", True, "Peanut")
dingo = Dog("white", "cnaani", False, "Dingo")

print(peanut.breed)
print(dingo)
print(dingo.bark())
print(peanut.sit())

#%%
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

## create an instance for the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)
#%%

# Exercise 
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print("Hello my name is " + self.name)

  def change_name(self, new_name):
      self.name = new_name
first_person = Person("John", 36)
first_person.show_details()

## Hello my name is John.

#%%
class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)
dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")

#%%

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

aaron = BankAccount(99845, 200)
aaron.deposit(50)
aaron.deposit(150)
aaron.view_balance()
aaron.withdraw(500)
aaron.view_transactions()


#%%
"""Create a book class where each book has a title, author and a year.""""
class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def check_out(self): 
        self.check_out = True
    def check_in(self):
        self.checked_out = False