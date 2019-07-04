ii1=list(map(int,input().split()))
ii2=list(map(int,input().split()))
for i in range(0,ii1[1]):
  inp2=[ii2[-1]] + ii2[:-1]
print(*ii2,end=' ')
