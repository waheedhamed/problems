
while True :
    a,b=[int(i) for i in input().split()]
    if a <=0 or b<=0 :
     break 
    x=0
    for i in range(min(a,b),(max(a,b))+1) :
        print(i,end=" ")
        x=x+i    
    print(f"sum ={x}")
 
