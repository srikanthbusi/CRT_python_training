import csv
def file(self,S_name,S_id,S_dept)
    self.Name = S_name




f= open("Student.csv","a",newline="")
a = csv.writer(f)
a.writerow(["Student_name","Student_id","Student_dept"])
Student_name = input("Enter the Student Name: ")
Student_id = int(input("Enter the Student_id : "))
Student_dept = (input("Enter the Student_dept : "))
# Student_name = input("Enter the Student Name: ")
# Student_id = int(input("Enter the Student_id : "))
# Student_dept = (input("Enter the Student_dept : "))
a.writerow([Student_name])
print("::::The below is the Student Information::::")
with open("Student.csv","r",newline="") as file:
    read = csv.DictReader(file)
    for row in read :
        if row[Student_name] == "Srikanth" and row[Student_id] == 443 and row[Student_dept] == 'Cse_DS':
            return True
        return False



def log_reg(username,password):
    self.username = username
    self.password = password


    

# Testing the class methods
f= open("loginAndreg.csv","a",newline="")
a = csv.writer(f)
a.writerow(["username","password"])
Student_name = input("Enter the username: ")
Student_id = int(input("Enter the password : "))
a.writerow([username,password])