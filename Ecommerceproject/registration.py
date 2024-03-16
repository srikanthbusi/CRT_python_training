import csv
f= open("registration.csv","a",newline="")
a = csv.writer(f)
a.writerow(["username","password","phoneno","pincode","city"])


