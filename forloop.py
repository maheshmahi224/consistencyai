
"""
range1=int(input("enter the range : "))
#range1=10
i=1
sum=0
while i<=range1:
 sum+=i #sum=sum+i 0+1=1,2+2=4,3+4=7
 i+=1   #i=i+1 1+1=2  now i=2,2+1=3,i=3
print(sum)
"""
"""
n=int(input("enter the range : "))

#print teh even numbers ante 2 4 6 8 10 
i=1
while (i<=n):
    if i%2 ==0:
        print(i)
    i+=1

    

print(f"these are the even numbers from 1 to {n}")
"""
'''
n=int(input("enter the table : "))

i=1
while i<=n:
    print(f"{n}*{i}={n*i}")
    i+=1
    if i==11:
        break
'''
'''
n=5
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

'''

'''
n=5
fact=1

while n>0:
    fact*=n
    n-=1

print(fact) 
'''

"""
n=5
fact=1
for i in range(0,n):
    fact=fact*n
    n-=1
print(fact)
"""



