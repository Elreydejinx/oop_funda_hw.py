# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner.
# Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.
class Vehicle:
    def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
           
    def update_user(self):
         self.owner = input('enter the name of the new owner:')
         print(self.owner)

Honda_fit = Vehicle('1VH658567568', 'Sadan', 'James Kennedy')
Jeep_charechee = Vehicle('1H1234124124', 'SUV', 'James Kennedy')
Dogde_ram = Vehicle('1VHDDF231084', 'Pick up', 'James Kennedy')

Honda_fit.update_user()
     
# Expected Outcome: Completion of the Vehicle class with the update_owner method and 
# a demonstration script showing the creation of Vehicle objects and updating their owners.
# Task 2: Event Management System Enhancement

# Problem Statement: Use the existing Event class by adding an attribute to keep track of the number of participants. 
# Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
    
    def num_of_participants(self, num_participants):
         self.num_participants = num_participants
         
            