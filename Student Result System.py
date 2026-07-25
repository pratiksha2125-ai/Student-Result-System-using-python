
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    
    def Result(self):

        if self.marks>=90:
            return "A"
        elif self.marks>=75:
            return "B" 
        elif self.marks >= 40:
            return "C"
        else:
            return "FAIL"
        
    def display(self):
        print("=================STUDENT DETAILS================")

        print(f"Student Name is :{self.name} \n Age is :{self.age}")
        print("Result",self.Result())

s1=student("Pratiksha",18,91.53)
s1.display()

