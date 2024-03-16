class addition:
    def add(self,a):#won't executed
        print(a)
    def add(self,a,b):#won't executed
        print(a+b)
    def add(self,a,b,c):#executed
        print(a+b+c)
        
obj=addition()
#obj.add(10)
#obj.add(10,20)
obj.add(10,20,30)

#python doesn't support method overloading so it passes errors
'''add fucntion can be work if u only call that last one coz 
add function assigned to last one'''
