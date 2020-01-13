#Argument specifiers are %s and %d 
#
#This prints out "Hello, John"
name = "John"
print("Hello, %s!" % name)

#exercise: Print this "Hello John Doe. Your current balance is $53.44."
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)