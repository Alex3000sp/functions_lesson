import math
from decor import inspect
# Concatination

@inspect
def concat(*args, **kwargs):
    return ' '.join(args) if not reserved else ' '.join(args[::-1])
concat('all', 'i', 'need', 'is', 'Python', reversed=True)

# Factorial of number

def factorial(n):
    fact = 1
    if n != 0 or n != 1:
        for i in range (1, n+1):
            fact *= i
        print(fact)
    else:
        return 1
factorial(5)

def factorial(n):
    print (math.factorial(n))
factorial(5)


