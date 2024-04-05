# write the recursive function to calculate the sum of digits of a number
def count(n):
    if n==0:  #basecase
     return 0
    return n%10 +count(n//10)
print(count(456))      #test case
    