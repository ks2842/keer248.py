kk=int(input())
str=list(input())[::-1]
p=[]
v=['a','e','i','o','u']
for k in str:
  if k not in v:
    p.append(k)
print(*p,sep='')
