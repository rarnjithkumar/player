def factorial(num):
  if num==1:
    return num
  else:
    return num* factorial(num-1)
num=int(input())
if num<0:
  print()
elif num==0:
  print()
else:
  print(factorial(num))
