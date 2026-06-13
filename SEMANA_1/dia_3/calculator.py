def add (a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    if b == 0:
        return "Error"
    return(a/b)

print(add(8,9))
print(subtract(8,9))
print(multiply(8,9))
print(divide(8,9))