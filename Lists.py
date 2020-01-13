#create an array
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) #prints 1
print(mylist[1]) #prints 2
print(mylist[2]) #prints 3

#print out 1,2,3 in a for loop
for x in mylist:
	print(x)
	break

#accesses index w/ error since it is out of range
mylist = [1,2,3]
#print(mylist[10])
#w/o error
print(mylist[0])

