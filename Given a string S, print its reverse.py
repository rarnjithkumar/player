def reverse(str):
  r=""
  for ch in str:
    r=ch+r
  return r
mystr=input()
print(reverse(mystr))
