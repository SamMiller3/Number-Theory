#27/10/2024 Euclidian Algorithm
first_number=int(input("Enter first integer: "))
second_number=int(input("Enter second integer: "))
a,b=max(first_number,second_number),min(first_number,second_number)
while a%b!=0:
    a,b=b,a%b
print(b)
