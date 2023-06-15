x=0

a,b=[int(i) for i in input().split()]
for i in range(1,min(a+1,b+1)) :
      if a%i == 0 and b%i==0  :
         x=i   
         
print(x)
