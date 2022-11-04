#for maths calculation

# example 1
# simple adding
x=lambda a:a+10
print(x(5))
# x s value move to a

# example 2
# simple multiplying
x=lambda a:a*10
print(x(5))

# ecxample 2.1
x=lambda a,b:a*b
print(x(5,6))

# lambda function in another function

# example 1
def my(n):
    return lambda a:a*n
sa= my(2)
print(sa(11))

# example 2
def my(n):
    return lambda a:a*n
print(x(11,3))


