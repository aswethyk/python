def merge(dict1,dict2):
    return (dict2.update(dict1))
dict1={'athu','achu','ammu'}
dict2={1,2,3}
print(merge(dict1,dict2))
print(dict2)