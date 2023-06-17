x=10**5
g=1
a=int(input())
l=[int(i) for i in input().split()]
for i in range(a) :
    if l[i]<x :
        x=l[i]
        g=i
        
print(x,g+1)    
