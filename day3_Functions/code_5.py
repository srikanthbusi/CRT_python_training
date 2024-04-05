
# write the recursive program to print
#  the digits of a number in reverse oder
def rev(n):
    if n==0:
        return
    print(n%10)
    return rev(n//10)
rev(564)
