
for i in range(int(input())) :
    x=0
    a,b=[int(i) for i in input().split()]
    for i in range(min(a,b)+1,max(a,b)):
        if i%2 != 0 :
            
            x=x+i

    print(x)
        
