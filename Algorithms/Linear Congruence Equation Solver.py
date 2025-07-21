# solve linear congruence equations of the form ax=b(mod m)
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

print("Input format: ax = b (mod m) give integers a, b and m.")
print("For example for 75x = 12 (mod 237) x = 76, 155, 234 (mod 237).")
a = int(input("enter a: "))
b = int(input("enter b: "))
m = int(input("enter m: "))
print(f"Only solutions in the set of least residues of modulo {m} will be returned.") 
gcd,p,q = extended_gcd(a,m) # use extended euclidean algorithm to solve Bezout's identity
if b % gcd != 0: # solutions exist if and only if d divides m
    print("No solutions exist to the given equation.")
elif gcd == 1: # if a and m are coprime find multiplicative inverse
    inverse = p
    x = (b * inverse) % m
    print(f"x = {x} (mod {m}).")
else: # otherwise there are d solutions modulo m
    k = p * (b//gcd)
    increment = m//gcd
    solutions=[]
    for i in range(gcd):
        solutions.append(str(k))
        k += increment
    print(f"x = {', '.join(solutions)} (mod {m}).")
