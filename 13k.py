p=int(input())
k=0
while p>0:
  r=p%10
  k=k+r*r
  p=p//10
print(k)
