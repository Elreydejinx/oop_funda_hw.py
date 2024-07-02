# Object Oriented Principles
# Guidelines for wrinting OOP well


# Encapsulation - Data Bundling or Data Hiding within our Classes
# allows to have more control over who adn what is accessing out class attributes and methods
# packages attributes and methids managing their accessibility

# public Attribute -most accessible - accessible within the class and outside the class their defined in
# self.name

# Protected Attribute - mildly accessibly - only accessibly within the class and subclasses(classes that inherit)
# self._settings --- underscore to denote a protect attribute

# private Attribute - least accessible - only accessible within the class they're defined in.
# self.__id
# Python does the best job at actually guarding with the naming convention
# __ python mangles the attribute so we cant access it by the name

#^^ PYTHON NAMING CONVENTIONS FOR THE ATTRIBUTES ^^

class Smartphone:
    def __init__(self, model, serial_number, operating_system):
        self.model = model # Public Attribute
        self._operating_system = operating_system # protected attribute
        self.__serial_number = serial_number

    def show_info(self):
        print(f'Model: {self.model}')
        print(f'Operating System: {self._operating_system}')
        # we only want to acces private attributes through getters and setters
        #use those getters or setters in other methods
        #check out getters and getters below
        print(f'Serial Number: private for security reasons... psss {self.__serial_number}')

# creating an instance of our smartphone
my_phone = Smartphone('Iphone 13', 'IOS', 'v37b45')

# accessing a public attribute
print(my_phone.model)

# accssing a protected attribute - this is possible - BUT is not recommended
print(my_phone._operating_system) # BUT YOU SHOULDN'T ... PLEASE
# numbers =[1,2,3,4,5,6,7,8,9,]
# def sum_list():
#     return sum(numbers) 
# trying to access a private attribute will give you an  error
# print(my_phone.__serial_number) # AttributeError
print(my_phone._Smartphone__serial_number) # accessing the mangled private attribute

# calling the show_info method
my_phone.show_info()

# Implementing Getters and Setters

# getter is a blass method that is used to read or access private attributes
# setters is a method that allows us to change the values of a private attribute

# provide controlled ways to interact wiht our class attributes, weather its viewing or modifying
class Smartphone:
    def __init__(self, model, serial_number, operating_system):
        self.model = model # Public Attribute
        self._operating_system = operating_system # protected attribute
        self.__serial_number = serial_number

    def show_info(self):
        print(f'Model: {self.model}')
        print(f'Operating System: {self._operating_system}')
        # we only want to acces private attributes through getters and setters
        #use those getters or setters in other methods
        #check out getters and getters below
        print(f'Serial Number: private for security reasons...') # psss {self.__serial_number}')
    
    # getter for the __serial_number
    def get_serial_number(self):
        #only thing a getter needs to do is return the specified attribute
        return self.__serial_number

    # setter for the __serial_number
    def set_serial_number(self, new_number):
        self.__serial_number = new_number

my_phone = Smartphone('IPhone 13', 'IOS', 'x2bn64')
# using the getter
serial_number = my_phone.get_serial_number()
print(serial_number, 'before calling the setter')
# using the setter
my_phone.set_serial_number('g23n769')
print(my_phone.get_serial_number(), 'after calling the setter')

# getters and setters within a bankaccount
class BankAccount():
    #                                 default perameter of 0
    def __init__(self, account_holder, initial_balance=0):
        #private attribute
        self.__balance = initial_balance
        # public attribute
        self.account_holder = account_holder

    # getter for balance
    def get_balance(self):
        return self.__balance
    # setter for balance
    def set_balance(self, new_balance):
        self.__balance = new_balance

    #getter for account_holder
    def get_account_holder(self):
        return self.account_holder
    
    # setter for account_holder
    def set_acount_holder(self, new_holder):
        self.account_holder = new_holder

    # deposit - use our setter to change the balance
    def deposit(self, amount):
        if amount > 0:
            #                    using the getter to access the curent balance and add it to the pass argument
            self.set_balance(self.get_balance() + amount)
            print(f'Deposited: {amount}')
        else:
            print('Invalid Deposit Amount')

    # withdraw
    def withdraw(self, amount):
        if 0 < amount < self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print(f'Withdrawn: ${amount}')
        else:
            print('Invalid withdrawal amount of insufficient balance')
# using our bank account
account = BankAccount('Ryan ,1000')
print(f'Account Holder: {account.get_account_holder()}')
print(f'initail Balance: ${account.get_balance()}')
        
# depositing and withdrawing from our account
account.deposit(700)
account.withdraw(200)
print(f'Updated Balance: ${account.get_balance()}')

# changing the account holder
account.set_acount_holder('Selena')
print(f'New Account Holder: {account.get_account_holder()}')

new_holder = input('who is the new person?')
account.set_acount_holder(new_holder)
# account.account_holder = new_holder


#inheritance - Classes can inherit funtionaly and attributes from other classes
# while also haveing their own unique funtionality
class SmartPhone:
    def __init__(self, model):
        self.model = model

    def make_call(self, number):
        print(f'Making a call to {number}')
    
    def send_message(self, number, message):
        print(f'Sending a message to {number}: {message}')

# child class - sub Class
#       call you inheriting form going in parentheses
                            #\/
class SmartCameraPhone(SmartPhone):
    def __init__(self, model, camera_resolution):
        # super.init() - calls the init of the perent class and initializes any of those attributes
        super().__init__(model)
        self.camera_resolution = camera_resolution
        

# Polymorphism - the ablility of objects of different classes to respond to the same method call in theie
# own unique ways - method overloading - repurposing methods  from an inherited class

# Abstraction - The Layer between the functionality of the code and the code itself.
# creating cli applications


# class Character:

#     #class attribute - shared across all instances of the class
#     gold = 0

#     def __init__(self, name, class_type):
#         self.name = name
#         self.class_type = class_type
    
#     def collect_gold(self, amount):
#         Character.gold += amount # (self.gold) would override the class but the class would be s
#         # shared accross a class

# archer = Character('Legolas', 'Archer')
# fighter = Character('Aragorn', 'Fighter')
# barbarian = Character('Gimli', 'Barbarian')

# archer.collect_gold(20)
# print(archer.gold)
# fighter.collect_gold(50)
# print(fighter.gold)
# barbarian.collect_gold(70)
# print(barbarian.gold)
