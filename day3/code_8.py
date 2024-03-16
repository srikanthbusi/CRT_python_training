# armstrong number using recursion
def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
x = count(n)
def arm(n):
    if n == 0:
        return 0
    return(n%10)**x + arm(n//10)
count(153)