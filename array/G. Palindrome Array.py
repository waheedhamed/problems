def main() :
    a=int(input())
    l=[int(i) for i in input().split()]
    for i in range(a) :
        
        if l[i]!=l[-(i+1)] :
            print("NO")
            return
    
    print("YES")
main() 
