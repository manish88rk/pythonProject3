L=['p','y','t','h','o','n']
length=len(L)
for a in range(length):
    print("At index",a,"and",(a-length),"element: ",L[a])
L2=['e','r']
L.extend(L2)
print(L)
L.insert(3,'n')
print(L)
j=L.pop(5)
print(j)
L.reverse()
print(L)
L.sort()
print(L)
L.sort(reverse=True)
print(L)
