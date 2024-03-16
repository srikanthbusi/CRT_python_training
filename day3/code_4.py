def fact(n):
 if n==0:
    return 1
 else:
   return n*fact(n-1)

print(fact(30))

# fibanocci series
def fib(num):
  if num==1:
    return 0
  elif num==2:
    return 1
  else:
    return fib(num-1) + fib(num-2)

print(fib(5))

def fib_iterative(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, num):
        a, b = b, a + b
    return b
fib_iterative(5)


