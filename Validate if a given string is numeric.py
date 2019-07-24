s=(input())
try:
  if "." in s:
    val=float(s)
    print("yes")
  else:
    val=int(s)
    print("yes")
except ValueError:
    print("No")
