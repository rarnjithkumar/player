l=int(input())
o=[]
for r in range(0,l):
  log=input()
  o.append(log)
g=[]
for r in zip(*o):
  if(r.count(r[0])==len(r)):
    g.append(r[0])
  else:
    break
print(''.join(g))
