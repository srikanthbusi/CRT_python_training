# write the recursive function to count the number of digits of a number
def num(n):
    if n == 0:
        return 0
    n= n%10
    return  1 + num(n//10)
# now let's call our function with an example
print(num(345))  # it should print 3 because there are three digits in 345. 
                 # The numbers are separated by zeros
