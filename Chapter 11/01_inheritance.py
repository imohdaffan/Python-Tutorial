class Employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
        
        
# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print("the name is {self.name} and the salary is {self.salary}")
        
#     def showLanguage(self):
#         print("The name is {self.name} and he is good with {self.language} language")
        
 
class Progrmmer(Employee):
     company = "ITC Infotech"
     def showLanguage(self):
         print(f"The name is {self.name} and he is good with {self.language} language")
        
a = Employee()
b = Progrmmer()

print(a.company, b.company)