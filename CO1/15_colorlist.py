col1=['orange','blue','yellow','red','black']
col2=['green','blue','red']
print(col1)
print(col2)
for i in range(len(col1)):
    if col1[i] not in col2:
      print("the colour is:",col1[i])

