# lambda arguments: expressions   :::::::Syntax

"""Example 1 – Multiplying a number to an argument with Python Lambda"""
# n  = int(input("Enter an number:"))
# var = lambda i : i*n
# print("The result is:",var(n))

"""Example 2 – Display a string with Python Lambda Functions"""
# n = input("Enter your String: ")
# # displaying using lambda functions 
# (lambda str : print(str))(n)
# (lambda str1: print(str1))(n)

"""Example 3 – Lambda Functions with more than arguments"""
# i,j,k = map(int,input("Enter the Threee elements:").split())
# value = lambda i,j,k:i*j*k
# print("The mltiplication of values are:",value(i,j,k))

"""Example 4 – Find the maximum of two numbers with Lambda Functions"""
# i,j = map(int,input("Enter two numbers:").split())
# values = lambda i,j: print(i) if i>j else print(j)
# values(i,j)

"""Example 5 – Find the square of a number with Python Lambda Functions"""
# num = int(input("Enter an number:"))
# valuess = lambda num:print(num*num)
# valuess(num)