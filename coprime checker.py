#27/10/2024 Checker for relatively prime numbers

def highestCommonDivisor(a,b):
    while a%b!=0:
        a,b=b,a%b
    return(b)

firstNumber=int(input("Enter first integer: "))
secondNumber=int(input("Enter second integer: "))

if highestCommonDivisor(max(firstNumber,secondNumber),min(firstNumber,secondNumber))==1:
    print(True)
else:
    print(False)