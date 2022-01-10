
l1=[10,20,30,40,50]
l2=[5,10,15,20,25]

leg1=len(l1)
leg2=len(l2)
if leg1==leg2:
  print("a)lists length are same")
else:
  print("a)not same")

total1=sum(l1)
total2=sum(l2)
print("  sum of the list1",total1)
print("  sum of list2",total2)
if total1==total2:
  print("b)sums are same value")
else:
  print("b)not same")

for i in l1:
  for x in l2:
    if i==x:
      print("c)match values are:",i)