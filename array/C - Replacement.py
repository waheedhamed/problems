a=int(input())
l=[int(i) for i in input().split()]
for i in l :
   if i <0 :
       print("2",end=" ")
   elif i>0 :
       print("1",end=" ")
   else :
       print("0",end=" ")    
