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

#The following code invokes the methods inside each class for the Band and Member

band = Band()
band.getLoginInfo()

member = Member()
member.getLoginInfo()
        

        
