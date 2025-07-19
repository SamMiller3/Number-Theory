#27/10/2024 Checker for relatively prime numbers

def highest_common_divisor(a,b):
    while a%b!=0:
        a,b=b,a%b
    return(b)

first_number=int(input("Enter first integer: "))
second_number=int(input("Enter second integer: "))

if highest_common_divisor(max(first_number,second_number),min(first_number,second_number))==1:
    print(True)
else:
    print(False)
