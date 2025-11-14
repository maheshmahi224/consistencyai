a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))
print(f"before swapping the value of a={a} and b={b}")
a=a+b
b=a-b
a=a-b
print(f"after swapping a={a} and b={b}")