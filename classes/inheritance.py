

class Parent:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
        
    def printProps(self):
        print(self.fname, self.lName)
        

class Child(Parent):
    def __init__(self, fName, lName, worth):
        super().__init__(fName, lName)
        self.worth = worth
        
    def printProps(self):
        print(self.fName, self.lName, self.worth)
        
entry1 = Child("Gift", "Mwaiseghe", 800000000000)
entry1.printProps()