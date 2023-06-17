x=0
a=int(input())
l=[int(i) for i in input().split()]
# for i in range(int(input())) :
for i in l :
    if i<0 :
        i//-1
    (x)=(x)+i
print(abs(x)) 
