a = {"IronMan", "Hulk", "Thor", "Captain" }
b = {"Superman", "BaTMAN", "Wonder-Woman"}
c = {"Hulk", "Thor"}
#isdisjoint

print(a.isdisjoint(b))

#issubset
print(c.issubset(a))


#issuperset

print(c.issuperset(a))

#update
x = a.update(c)
print(a)


#clear
a.clear()
print(a)