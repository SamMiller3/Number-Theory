# Find modular multiplicative inverse given 
# a modulo m
# 21/07/2025

def extended_gcd(a,b): # extended euclidean algorithm
    if a % b == 0:
        return (b, 0, 1) 
    quotient = a//b 
    remainder = a - quotient * b 
    gcd, old_x , old_y = extended_gcd(b, remainder)
    x = old_y
    y = old_x - old_y * quotient
    return gcd, x, y

print("Input format: a (mod m) give integers a and m")
a = int(input("enter a: "))
m = int(input("enter m: "))
d,p,q = extended_gcd(a,m) # use extended euclidean algorithm to solve Bezout's identity
if d == 1: # verify they are coprime
    print(f"Modular multiplicative inverse is: {p}.")
else: 
    print("Modular multiplicative inverse does not exist.")
