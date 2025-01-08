# def check_3_digits(number):
#     return number in range(100, 1000)

# result = check_3_digits(120)
# print(result)


# def check_3_digits(list1):
#     for n in list1:
#         if n in range (100, 1000):
#             return True
#         else:
#             pass

# result = check_3_digits([555, 999, 600])
# print(result)


# def check_3_digits(list1):
#     three_digits_list = []
#     for n in range(100, 1000):
#         three_digits_list.append(n)
#     else:
#         pass

#     return False

# result = check_3_digits([555, 99, 600])


# coffee_prices = [('cappuccino', 1.5), ('espresso', 1.2), ('mocha', 1.9)]

# def most_expensive_coffee(list_of_prices):

#     highest_price = 0
#     my_most_expensive_coffee = ''

#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price = price
#             my_most_expensive_coffee = coffee
#         else:
#             pass

#     return (my_most_expensive_coffee, highest_price)

# print(most_expensive_coffee(coffee_prices))

# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

# num_list = [-1, 12, 54, -98] #list of values

# def all_positives(num_list): #defining the list so that I can find the positive values 
#     for n in num_list: 
#         if n > 0: #makes sure that the list would be true if all numbers would be positive 
#             return True 
#     else:
#         return False #if there are negative values the output would be false 
# print(all_positives(num_list))





# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

numbers = [12, 101, 800, 32, 55] #Create list of values

def sum_less(numbers): #Define sum_less
    total = 0 #Sets total to 0 at first
    for n in numbers: 
        if n > 0 and n < 1000: #Only allows numbers within the range of 100 to 1000
            total += n #If number is eligible, add it to the total and now do it for every numberin the for loop
    return total
print(sum_less(numbers))




# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #making the numbers a list so that its easy to do the same function for every number

def count_even(values):
    count = 0 #starts the count at 0 
    for n in values:
        if n %2 == 0: #checks that a number is even/divisible by 2 
            count += 1 #counts how many even numbers there are 

    return count

print(count_even(values))