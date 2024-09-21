# # Countdown
# # Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array?

def count_down(number):
    array = []
    while(number != 0):
        array.append(number)
        number -=1
    print(array)
        
number = int(input("Please enter a number: ")) 
count_down(number)       


# # Print and Return
# # Your function will receive an array with two numbers. Print the first value, and return the second.

def print_and_return(arr):
    print(arr[0])
    return arr[1]

number1 = int(input("Please enter the first number to file the array: "))
number2 = int(input("Please enter the second number to file the array: "))
array = [number1, number2]
print_and_return(array)    
    

# # First Plus Length
# # Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

def first_plus_length(arr):
    length = len(arr)
    total = 0
    if( type(arr[0]) == int or type(arr[0] == float) ):
        total = arr[0] + length
        print(f"the sum of the first index {arr[0] } + the length {length} is {total}")
    else:
        print("Please enter numbers for this array")    
    return total 

# # number1 = float(input("Please enter the first number to file the array: "))
# # number2 = float(input("Please enter the second number to file the array: "))
# # number3 = float(input("Please enter the third number to file the array: "))
# # number4 = float(input("Please enter the forth number to file the array: "))
# # array = [number1, number2, number3,number4] 

array_length = int(input("Please enter the length of the array: "))
array = []
for index in range(array_length):
    number = float(input(f"Enter the value for index {index + 1}: "))
    array.append(number)
    
first_plus_length(array)
    

# # Values Greater than Second
# # For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.

def value_greater_than_second(arr):
    if len(arr) <2:
        print("Your array must have at least 2 elements")
        return 0
    
    low = arr[1]
    counter = 0
    for index in range(len(arr)):
        if(arr[index] > low):
            print(f"The index {index} of the value {arr[index]} is greater than {low}")
            counter += 1
    return counter

array_length = int(input("Please enter the length of the array: "))
array = []
for index in range(array_length):
    number = float(input(f"Enter the value for index {index + 1}: "))
    array.append(number)
    
count_greater = value_greater_than_second(array)
print(f"Total values greater than the second value are {count_greater} values.")        
    

# Values Greater than Second, Generalized
# Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?

def generalized(arr):
    if (len(arr)) < 2:
        print("Your array must have at least 2 elements")
        return []
    second_value  = arr[1]
    counter = 0
    new_array =  []
    for index in range(len(arr)):
        if(arr[index] > second_value ):
            print(f"The index {index} of the value {arr[index]} is greater than {second_value}")
            new_array.append(arr[index])
            counter += 1
    print(f"you new array is {new_array} with length equal {counter}")    
    return new_array 


array_length = int(input("Please enter the length of the array: "))
array = []
for index in range(array_length):
    number = float(input(f"Enter the value for index {index + 1}: "))
    array.append(number)
    
generalized(array)        

# This Length, That Value
# Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.

def this_length_that_value(num1, num2):
    array = []
    for i in range(num1):
        if(num1 == num2):
            array.append("Jinx!")
        else:
            array.append(num2)
    print(array)        
    return array        
    
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))

this_length_that_value(number1, number2)     


# Fit the First Value
# Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!"; if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".

def first_value(arr):
    value = arr[0]
    length = len(arr)
    if( length > value):
        print("Too Big!")
    elif (length < value):
        print("Too Small!")
    else:
        print("Just Right!")
        
array_length = int(input("Please enter the length of the array: "))       
array = []
for index in range(array_length):
    number = float(input(f"Enter the value for index {index + 1}: "))
    array.append(number)
first_value(array)                
    

# Fahrenheit to Celsius
# Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit and returns the equivalent temperature as expressed in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.




# Celsius to Fahrenheit
# Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, and returns the equivalent temperature expressed in Fahrenheit degrees.

# (Optional): Do Fahrenheit and Celsius values equate at a certain number? The scientific calculation can be complex, so for this challenge just try a series of Celsius integer values starting at 200, going downward (descending), checking whether it is equal to the corresponding Fahrenheit value.