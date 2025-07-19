#27/10/2024 Implementation of Eulers totient function

def highest_common_divisor(a,b):
    while a%b!=0:
        a,b=b,a%b
    return(b)

def id_coprime(a,b):
    return(highest_common_divisor(a,b)==1)

def totient(n):
    value=0
    for i in range(1,n):
        if is_coprime(i,n):
            value+=1
    return(value)

n=int(input("Enter value to find totient of: "))
print(totient(n))
