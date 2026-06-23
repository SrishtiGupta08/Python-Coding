# python function using function to calculate the average of three numbers using three different approaches 

# user input taken inside the function

def avg3():# function without perameter
    a, b, c=map(int,input("enter the three numbers: ").split())
    average=(a+b+c)/3
    print("Average is: ",average)    # to print the output
avg3() # function calling


print()  # for one line space between the functions

# function with argument

def avg2(a, b, c):  # function with parameter
    average=(a+b+c)/3
    print("Average is: ",average)     # to print the output
a=int(input("enter the first number:"))  # user input 1
b=int(input("enter the second number:")) # user input 2
c=int(input("enter the third number: ")) # user input 3
avg2(a, b, c)  # function calling with argument


print() # for one line space between the functions

# function without argument

def avg1(): # function
    a=int(input("enter the first number:"))   # user input 1
    b=int(input("enter the second number:"))  # user input 2
    c=int(input("enter the third number: "))  # user input 3
    average=(a+b+c)/3
    print("Average is: ",average)  # to print the output
avg1() # function calling


# the programe demonstrate the use of functions, parameter and using user input in python


