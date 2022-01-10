list=[]
for i in range(5):
  n=int(input("enter numbers"))
  if n<100:
    list.append(n)
  else:
    list.append("over")
print(list)