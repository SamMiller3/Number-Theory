#27/10/2024 Euclidian Algorithm
firstNumber=int(input("Enter first integer: "))
secondNumber=int(input("Enter second integer: "))
a,b=max(firstNumber,secondNumber),min(firstNumber,secondNumber)
c=0
while a%b!=0:
    a,b=b,a%b
print(b)