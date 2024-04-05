# write an function to calculate sum of first n large digits of a number
def sod(n):
    l = n % 10
    while n >= 10:
        
        n = n // 10
        f = n  # f is now assigned before the while loop
    return n + f  # return the sum

print(sod(786))



def sod(n):
    total = 0
#     # Finding the first n large digits of the number
    while n > 0 and n < 10:
        n = n // 10
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total

result = sod(786)
print("The sum of the digits is:", result)
