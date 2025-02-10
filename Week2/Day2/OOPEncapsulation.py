class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
c.sell()

# change the price
c.__max_price = 1000
c.sell()
# >> The private attribute __max_price cannot be changed
# >> Selling Price: 900

# using setter function
c.set_max_price(1000)
c.sell()
# >> Selling Price: 1000