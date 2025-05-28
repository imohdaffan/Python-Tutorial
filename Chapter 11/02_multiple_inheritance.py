class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"the name of the Employee is {self.name} and the salary is {self.company}")
        
class coder:
    language = "python"
    def printlanguages(self):
        print(f"Out of all languages here is your language: {self.language}")
    
        
 
class Progrmmer(Employee, coder):
     company = "ITC Infotech"
     def showLanguage(self):
         print(f"The name is {self.company} and he is good with {self.language} language")
       
 
a = Employee()
b = Progrmmer()

b.show()
b.printlanguages()
b.showLanguage()