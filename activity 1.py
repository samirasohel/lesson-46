class employee:
    #constructor
    def __init__(self,name):
        self.name=name

    #destructor
    def __del__(self):
        print("Object deleted")
        

emp1=employee("Samira")
print("Name of the employee is",emp1.name)

del emp1