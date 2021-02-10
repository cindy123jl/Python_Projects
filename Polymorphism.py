#Parent Class Band

class Band:
    bandName = "EXO"
    email = "members.login@gmail.com"
    password = "x023q!"
#what is displayed to user and getting values in from user
    def getLoginInfo(self):
        entry_bandName = input("Enter your band name: ")
        entry_email = input("Enter the bands email: ")
        entry_password = input("Enter the bands password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {} member!".format(entry_bandName))
        else:
            print("The password or email is incorrect.")


#Child Class Member
class Member(Band):
    base_pay = 65.00
    department = "SM Entertainment"
    pin_number = "2324"

#This is the same method in the parent class Band.
#The difference is entry_pin, we are displaying to user and retrieving their input
#and depending on their input we are printing a statement
    def getLoginInfo(self):
        entry_bandName = input("Enter your band name: ")
        entry_email = input("Enter your bands email: ")
        entry_pin = input("Enter the pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {} member!".format(entry_bandName))
        else:
            print("The pin or email is incorrect")
            
class drinks(Band):
    location = "Cafe Shoppe"
    access_number = "4442"
    
#has the same methods to the parent class except the location and access
#number is added to gain acess orders to Cafe Shoppe
    def getLoginInfo(self):
        entry_bandName = input("Enter your band name: ")
        entry_email = input("Enter you bands email: ")
        entry_access = input("Enter access number for access to drink orders: ")
        if (entry_email == self.email and entry_access == self.access_number):
            print("Welcome back, {} member!".format(entry_bandName))
        else:
            print("Try again. The email or access number is incorrect")
    

#The following code invokes the methods inside each class for the Band and Member

band = Band()
band.getLoginInfo()

member = Member()
member.getLoginInfo()

drinks = drinks()
drinks.getLoginInfo()
        

        
