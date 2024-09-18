# Setting and Swapping
# Set myNumber to 42. Set myName to your name. Now swap myNumber into myName & vice versa.


myNumber = 42
myName = 'Bayan'

swap = myNumber
myNumber = myName

myName = swap

print("swap my number to my name:" , myName)
print("swap my name to my number:" , myNumber)

# Print -52 to 1066
# Print integers from -52 to 1066 using a FOR loop.

for number in range(-52, 1067):
    print(number) 

# Don’t Worry, Be Happy
# Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.

def beCheerful():
    counter = 1
    while(counter < 99):
        print(counter , "good morning!")
        counter+=1
        
beCheerful()

# Multiples of Three – but Not All
# Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.
def multiple():
    for multiple in range(-300, 1):
        if(multiple % 3 == 0 and (multiple != -3 and multiple != -6)):
            print(multiple)
                
multiple()   


# Printing Integers with While
# Print integers from 2000 to 5280, using a WHILE.

def printing_integers():
    number = 2000
    while(number <= 5280):
        print(number)
        number +=1
        
printing_integers()

# You Say It’s Your Birthday
# If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day...." 

def your_birthday(day, month):
    if( day == 1 and month == "March"):
        print("How did you know?")
    else:
        print("Just another day...." )            

day = int(input("Enter a Day: "))
month= str(input("Enter the name of the Month: "))

your_birthday(day, month)

# Leap Year
# Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.
        
def leap_year(year):
    if((year% 400 == 0) or (year % 100 != 0 and year % 4 == 0 )):
        print(f"this year {year} is a leap year")
    else:
        print(f"this year {year} is not a leap year")    
        
        
leap_year(2024)  


# Print and Count
# Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.      

def multiples_of_five():
    counter = 0
    for integer in range(512, 4097):
        if(integer%5 == 0):
            print(f"{counter}: The integer {integer} is multiple of 5")
            counter +=1
            
multiples_of_five()


# Multiples of Six
# Print multiples of 6 up to 60,000, using a WHILE.    

def multiples_of_six():
    number = 0
    while( number < 60000):
        if(number % 6 == 0):
            print(number)
        number +=1
            
            
multiples_of_six() 

# Counting, the Dojo Way
# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".        

def divisible():
    integer = 0
    while(integer <= 100):
        if(integer % 10 == 0):
            print("Dojo")
        elif(integer % 5 == 0):
            print("Coding")
        else:
            print(integer)
        integer +=1    

divisible()

# What Do You Know?
# Your function will be given an input parameter incoming. Please console.log this value.

def incoming(input_value):
    print(input_value)
    

input_val = str(input("What do you know?  "))  
incoming(input_val)
    
    
# Whoa, That Sucker’s Huge…
# Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?   

def sum(num1, num2):
    sum = 0
    if(num1 %2 != 0 and num2 %2 != 0):
        sum = num1 + num2
        print(f"The sum of {num1} + {num2}= {sum}")
    else:
        print("Please enter an odd numbers")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        sum = num1 + num2
        print(f"The sum of {num1} + {num2}= {sum}")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: ")) 

sum(num1, num2)

# Countdown by Fours
# Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop

def countdown_by_fours():
    start = 2016
    while(start >0):
        print(start)
        start -=4

countdown_by_fours()        
        
# Flexible Countdown
# Based on earlier “Countdown by Fours”, given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).        
    
def flexible_countdown(lowNum, highNum, mult):
    for integer in range(highNum, lowNum, -1):
        if(integer % mult == 0):
            print(integer)
            

lowNum = int(input("Please enter a lower number: "))
highNum = int(input("Please enter a high number: "))  
mult = int(input("Please enter a multiple number: "))
flexible_countdown(lowNum, highNum, mult)


# The Final Countdown
# This is based on “Flexible Countdown”. The parameter names are not as helpful, but the problem is essentially identical; don’t be thrown off! Given 4 parameters (param1,param2,param3,param4), print the multiples of param1, starting at param2 and extending to param3. One exception: if a multiple is equal to param4, then skip (don’t print) it. Do this using a WHILE. Given (3,5,17,9), print 6,12,15 (which are all of the multiples of 3 between 5 and 17, and excluding the value 9).    

def final_countdown(mult, low, high, stop):
    while(low < high ):
        if((low % mult == 0) and (low != stop)):
            print(low)
        low +=1

param1 = int(input("Please enter a param1: "))
param2 = int(input("Please enter a param2: "))  
param3 = int(input("Please enter a param3: "))
param4 = int(input("Please enter a param4: "))

final_countdown(param1,param2,param3,param4)                  
                