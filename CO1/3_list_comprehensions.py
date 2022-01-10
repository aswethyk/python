# list comprehension
# a)positive numbers from given list
list = [-3,-2,-1,0,1,2,3]
newlist = [x for x in list if x > 0]
print(newlist)


#b)square of n numbers
n=int(input("Enter nth number: "))
sum = 0
for s in range(1,n+1):
    squre=(s*s)
    print("squre of n numbers :",squre)


#c)vowels in word
word = input("Enter word : ")
vowels = "aeiouAEIOU"
vowels_list = [each for each in word if each in vowels]
print(vowels_list)


#d)ordinal value
w=input("enter a word:")
ord=[ord(x) for x in w]
print("the ordinal value is:",ord)

