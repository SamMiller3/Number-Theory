#27/10/2024 Implementation of Eulers totient function

def highestCommonDivisor(a,b):
    while a%b!=0:
        a,b=b,a%b
    return(b)

def isCoprime(a,b):
    return(highestCommonDivisor(a,b)==1)

def totient(n):
    value=0
    for i in range(1,n):
        if isCoprime(i,n):
            value+=1
    return(value)

n=int(input("Enter value to find totient of: "))
print(totient(n))