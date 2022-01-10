n1=int(input("Enter a number1: "))
n2=int(input("Enter a number2: "))
n3=int(input("Enter a number3: "))
if n1>n2 and n1>n3:
    print("biggest number is:",n1)
elif n2>n3:
    print("biggest number is:",n2)
else:
    print("biggest number is:",n3)