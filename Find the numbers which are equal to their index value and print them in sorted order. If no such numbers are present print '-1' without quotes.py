r=int(input())
test_list=list(map(int,input().strip().split()))[:r]
for i in range(len(test_list)):
  if(i==test_list[i]):
    print(test_list[i],end=" ")
