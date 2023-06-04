'''
Description: None
version: None
Author: None
Date: 2023-04-04 16:05:48
LastEditors: None
LastEditTime: 2023-04-06 15:21:18
'''

i=" ciallo2 "
j=12700721

k=["C","i","a"]

print("Ciallo")
print(i)

print(i.title())
print(i.upper())
print(i.lower())

print(i+" "+str(j))
print(i.rstrip()+" "+str(j))
print(i.lstrip()+" "+str(j))
print(i.strip()+" "+str(j))

print(k[0]+k[1]+k[2])

k.append("llo")
k.insert(4,"!")
k.insert(5,"!")
print(k)

print(k.pop(5))
print(k)

del k[4]
print(k)
