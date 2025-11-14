#area  of circle
"""
pie=22/7
def area(radi):
    a=(pie)*radi**2
    return a

radi=int(input("enter the radius"))
print(area(radi))
"""

#solving quadratic equations using functions
"""
a=0
b=0
c=0
def roots(a,b,c):
    d=(b**2)-4*a*c
    root1=0
    root2=0
    root2=(-b+d**(0.5))/2*a
    root1=(-b-d**(0.5))/2*a
    return root1,root2

a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
c=int(input("enter the value of c : "))
print(f"root 1 is {roots(a,b,c)}")
print(f"root 2 is {roots(a,b,c)}")
#this has errors
"""
 
def calroot(a,b,c):
    root1=0
    root2=0
    d=(b**2) - 4*a*c
    root1=(-b+(d**(0.5)))/2*a
    root2=(-b-(d**(0.5)))/2*a
    print(f"the value of root1 is ({root1}) and root2 is ({root2}) ")
    

a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))
c=int(input("enter the value of c :"))

calroot(a,b,c)


