
a=int(input())
l=[int(i) for i in input().split()]
for i in range(a) :
    if l[i]<=10 :
      print(f"A[{i}] = {l[i]}")
