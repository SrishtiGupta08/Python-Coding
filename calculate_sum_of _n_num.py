'Calculate the sum of first n natural numbers using recursive function'

def sum(n):            #here n is the parameter which is used to calculate the sum of first n natural numbers
    if(n==1 or n==0):  # this is the base case which is used to stop the recursion when n is 1 or 0

        return n       #it return the value of n when n is 1 or 0
    else:
        return n + sum(n-1)     #this is the recursive case which is used to calculate the sum of first n natural numbers by adding n to the sum of first n-1 natural numbers

print(sum(int(input("enter the value:")))) # this is the main function which is used to take input from the user and call the sum functionto calculate the sum of first n natural numbers and print the result



'calculate the sum of digits of a number using recursive function'

def rec(n):            #here n is the parameter which is used to calculate the sum of digits of a number
    
    if n==1 or n==0:   #this is the base case which is used to stop the recursion when n is 1 or 0
        return n
    else:
        r=n%10         #this is used to get the last digit of the number
        
        return r + rec(n//10)    #this is the recursive case which is used to calculate the sum of digits of a number by adding the last digit to the sum of digits of the number without the last digit
    
print(rec(int(input("enter the value:"))))   # this is the main function which is used to take input from the user and call the rec function to calculate the sum of digits of a number and print the result