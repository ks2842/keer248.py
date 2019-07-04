n1,n2=map(int,input().split())
num=[]
for i in range(n1+1,n2+1):
  if i>1:
    for w in range(2,i):
      if(i%w==0):
        break
    else:
      n.append(w)
print(len(num)+1)
