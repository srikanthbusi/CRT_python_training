class husband:
    def gift(self):
        print("roses")
    def trip(self):
        print("kerala")
        
class wife(husband):
    def gift(self):
        print("dress")
        
obj=wife()
obj.gift()
obj.trip()
        