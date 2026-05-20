a = {"IronMan", "Hulk", "Thor", "Captain" }
b = {"Superman", "Batman", "Wonder-Woman"}
c = {"Hulk", "Thor", "Spiderman"}
#UNION
print(a.union(b))

##DIFFERENCE
print(a.difference(b))

### DIFFERENCE UPDATE
a.difference_update(b)
print(a)

####INTERSECTION
print(a.intersection(c))

##### SYMETRIC_DIFFERENCE
x = a.symmetric_difference(c)
print(x)

######SYMETRIC DIFFERENCE UPDATE
a.symmetric_difference_update(c)
print(a)