class faculty:
    def __init__(self,fname,dept,id):
        self.fname=fname
        self.dept=dept
        self.id=id
    def print_info(self):
        print("faculty info:",self.fname,self.dept,self.id)
obj = faculty("sat","cse",101)
obj.print_info()
class cse(faculty):
    pass
obj=cse("nav","cse",102)
obj.print_info()

        