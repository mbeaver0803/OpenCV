#tutorial 2
#Variables and Types
myint = 7
print(myint)

#float
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

#Difference of ' and "
mystring = "Don't worry about apostrophes"
print(mystring)

#simple operators
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#simultaneous assignments
a, b= 3, 4
print(a,b)

#mixing operators doesnt world this way
print(one+two+hello)
#this way works
helloworld = str(one) + str(two) + hello
print(helloworld)