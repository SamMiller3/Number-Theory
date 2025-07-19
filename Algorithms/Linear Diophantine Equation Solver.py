# linear Diophantine Equation solver 
# can verify equations such as ax+by=c have a solution and find it
# given that a,b,c are integers
# implemented using the extended euclidean algorithm
# 19/07/2025

def gcd(a,b): # standard euclidean
    if a % b == 0:
        return b 
    quotient = a//b 
    remainder = a - quotient * b 
    return(gcd(b, remainder))

def extended_gcd(a,b): 
    if a % b == 0:
        return (b, 0, 1) # returning d,x1,y1
        # b would be the previous remainder hence gcd=b and y=1,x=0
    quotient = a//b 
    remainder = a - quotient * b # rearrange divison algorithm
    gcd, old_x , old_y = extended_gcd(b, remainder)
    x = old_y
    y = old_x - old_y * quotient
    return gcd, x, y

print("you will enter an equation of the form ax+by=c for example 1071x+462y=21.")
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
print(f"Equation is {a}x+{b}y={c}")
gcd = gcd(a,b)
if c%gcd!=0: # a solution exists iff gcd(a,b)|c
    print("A solution does not exist for the given equation.")
else:
    a_reduced,b_reduced = a//gcd,b//gcd # a and b are now coprime hence will find principal solution
    d,x0,y0 = extended_gcd(a,b)
    scale = c // gcd
    x, y = scale * x0, scale * y0
    print(f"Genral solution: x = {x} + {b_reduced}k and y = {y} - {a_reduced}k for some integer k.")