class Father:
    def bike(self):
        print("Harley Davidson")
    def laptop(self):
        print("laptop with lower specifications")
class Children(Father):
    def laptop(self):
        print("laptop with Higher specifications w")

obj = Children()
obj.laptop()  #over riding