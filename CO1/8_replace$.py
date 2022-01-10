a=input("enter a string")
str1=""
s=a[0]
b=a[1:]
for i in b:
  if s==i:
    str1=b.replace(i,"$")
print(s+str1)