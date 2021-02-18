#Cindy Lara
#Python 
#encapsulation assignment
#I will be creating a class that uses 
#encapsulation

#This assignment should include the following

#1. The class should make use of a private attribute or function.

#2. The class should make use of a protected attribute or function.

#3. Create an object that makes use of protected and private.

#4. Add comments throughout your Python explaining your code.

class Private:# my class called Private
    def __init__(self):#built in init function in python, it is used to assign values to operations
        self.__privateVar = "DOGS"# self is the word chosen to name as my parameter the name of the variable is privateVar
                                  #the double underscores denotes private
    
    def getPrivate(self):
        print(self.__privateVar)#how we print our value, in this instance "DOGS"

    def setPrivate(self, private): #accessing instances from our class
        self.__privateVar = private #this is our private attribute

obj = Private() # obj is defined
obj.getPrivate()
obj.setPrivate("CATS") #can give the private variable a new value without altering the original
obj.getPrivate() #new value retrieved

#a protected class where we are assinging a value then changin it under obj 
class protected: #class name
    def __init__(self):
        self._protectedVar = 23 #our initial value

obj = protected()
obj._protectedVar = 231 # our changed value
print(obj._protectedVar) #our changed value is printed out
