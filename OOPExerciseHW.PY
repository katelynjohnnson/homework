class RetailItem:

    def __init__(self,description,units,price):
        self.__ItemDescript = description
        self.__Units = units
        self.__Price = price

    def get_description(self):
        print('Description: ',self.__ItemDescript)

    def get_units(self):
        print('Units in Inventory: ',self.__Units)
    
    def get_price(self):
        print('Price: $',self.__Price)

item1 = RetailItem('Jacket',12,59.95)
item2 = RetailItem('Designer Jeans',40,34.95)
item3 = RetailItem('Shirt',20,24.95)

print('\nRetail Item 1: ')
item1.get_description(),
item1.get_units(),
item1.get_price()

print('\nRetail Item 2: ')
item2.get_description(),
item2.get_units(),
item2.get_price()

print('\nRetail Item 3: ')
item3.get_description(),
item3.get_units(),
item3.get_price()