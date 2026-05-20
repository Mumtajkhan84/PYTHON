#WRITE A PROGRAM TO FIND MAX AND MIN IN SET
a = {12,56,34,8,90,1,57}
maximum = max(a)
minimum = min(a)

print("the maximum value ", maximum, "\n", "it is minimum value",minimum)

## WRITE A PROGRAM TO FIND COMMON ELEMENTS IN 
# THREE LISTS USING SETS
a= [1,5,6,8,2]
b=[4,5,6,7]
c = [1,9,6,2,5]
print(set(a)& set(b) & set(c))




### WRITE A PROGRAM TO FIND DIFFERENCE BETWEEN TWO SETS
a = {1,5,6,8,2}
b = {1,9,6,2,5}
print(a.difference(b))


#### WRITE A PROGRAM TO REMOVE AN ITEM FROM A SET IF IT IS PRESENT IN THE SET
a = {1,5,6,8,2}
a.discard(8)
print(a)

#####WRITE A PYTHON PROGRAM TO CHECK IF A SET IS A SUBSET OF ANOTHER SET
a = {1,5,6,8,2}
b = {5,6,2}
print(b.issubset(a))
