# The extended Euclidean algorithm finds the greatest common divisor of a and b 
# as well as well as solving berzout's identity ax+by=gcd(a+b)
# using the divison algorithm  (a = b * quotient + remainder)
# to track the linear combinations of d = x1 * b + y1 * remainder

# 19/07/2025

def extended_gcd(a,b): 
    if a % b == 0:
        return (b, 0, 1) # return - d,x1,y1. b would be the previous remainder hence gcd and b has coefficient of 1
    quotient = a//b 
    remainder = a - quotient * b # rearrange divison algorithm
    gcd, old_x , old_y = extended_gcd(b, remainder)
    x = old_y
    y = old_x - old_y * quotient
    return gcd, x, y


a = int(input("enter a: "))
b = int(input("enter b: "))
gcd, x, y = extended_gcd(a,b)
print(f"gcd({a}, {b}) = {gcd}")
print(f"gcd({a}, {b}) = {a}x + {b}y for x and y are integers")
print(f"principal solution of equation is x = {x}, y = {y}")