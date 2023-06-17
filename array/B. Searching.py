a=int(input())
l=[int(i) for i in input().split()]
b=int(input())

for i in range(a) :
    if l[i]==b :
       print(i)
       break
else :
    print("-1")
