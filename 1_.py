#functions are ways to wrap your code
#into reusable units
#def is useless without invoking and vice versa

#function = A block of reusable code
#place () after the function to invoke it 

# #position of the parameters matters
# def happy_birthday(name, age): #def DEFINES the function (make sure to indent) #name is a parameter (a parameter is a temporary name or place holder) - what's inside the parenthesis in the definition    
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")

#     print("Happy Birthday to you!!")

# #to invoke or "call the function"
# happy_birthday("bro",20) #bro is the the argument 
# happy_birthday("Esteban",17)
# happy_birthday("Jesse",17)


# def display_invoice(username, amount, due_date):
#     print(f"hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("BroCode", 42.50, "01/01")


# return = statement used to end a function
# and send a result block to the caller

# def add(x,y):
#     z = x + y
#     return z

# def subrtract(x, y):
#     z= x - y
#     return z

# def multiply(x, y):
#     z= x * y
#     return z

# def divide(x, y):
#     z= x / y
#     return z

# print(add(1, 2))
# print(subrtract(1, 2))
# print(multiply(1 ,2))
# print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Daniel", "Reyes")
print(full_name)