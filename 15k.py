p1 = input()
p2 = []
for x in range(len(p1)):
  p2.append(p1.count(p1[x]))
x = p2.index(max(p2))
print (p1[x])
