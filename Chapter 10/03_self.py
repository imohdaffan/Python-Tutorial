class Employee:
    language = "python" # This is a class attribute
    salary = 1200000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary {self.salary}")
        
    @staticmethod
    def greet():
        print("Good morning")
    

harry = Employee()
# harry.language = "JavaScript" # This is a instance attribute
harry.getInfo()
harry.greet()
# Employee.getInfo("harry")