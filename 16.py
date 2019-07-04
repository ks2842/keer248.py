p1=int(input())
p2=list(map(int,input().split()))
count=0
for j in range(0,p1+1):
  if(p2.count(j)==1):
   print(j)
   break
