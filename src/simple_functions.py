# simple math opetation function
# addtion
def add(x, y):
    return (x + y)

# product
def prod(x, y):
    return (y*x)

# power 
def power(x, y):
    return (x**y)

# factorial in a recusive way
def factorial(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n*factorial(n-1)
        
