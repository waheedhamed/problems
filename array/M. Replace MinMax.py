x=1
y=1
# for i in range (int(input())) :
a=int(input())
l=[int(i) for i in input().split()]

x=min(l)
y=max(l)
    
for i  in range(a) :
    if l[i]==x  :
       l[i]=y
    elif l[i]==y :
         l[i]=x      
         
print(*l)
