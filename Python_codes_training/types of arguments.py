def ex(s,n):
    print("name:",s)
    print("surname:",n)
ex("sat","na")

def ex(s,n):
    print("name:",s)
    print("surname:",n)
ex(n="sat",s="na")

def ex(s,n="ash"):
    print("name:",s)
    print("surname:",n)
ex("ash")


def ex(**na):

    print("surname:",na["n"])
ex(n="sat")



