import csv
with open("athu.csv","w",newline='') as file:
 write=csv.writer(file)
 write.writerow(["Sl No","Department","Division"])
 write.writerow(["1","MCA","S1"])
 write.writerow(["2","MCA","S2"])
with open("athu.csv") as csvfile:
 data=csv.reader(csvfile)
 for r in data:
  print(r)
