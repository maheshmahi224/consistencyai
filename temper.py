select=input("select the temperature type (k or oc or f) : ")
temp=float(input("enter the temperature value :"))

if select=="c":
    print(f"celcius :{temp}")
    F=temp*(9/5)+32
    K=temp+273
    print(f"farenhiet :{F}")
    print(f"Kelvin :{K}")


elif select=="f":
    print(f"farenhiet :{temp}")
    C=(temp-32)*(5/9)
    K=C+273
    print(f"celcius :{C}")
    print(f"Kelvin :{K}")

elif select=="k":
    print(f"Kelvin :{temp}")
    C=temp-273
    F=C*(9/5)+32
    print(f"celcius :{C}")
    print(f"farenhiet :{F}")

else:
    print("INVAILD SELECTION")
