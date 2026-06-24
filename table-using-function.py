# table using function

n=int(input("Enter the value:"))

def table():  # function without parameter 

    for i in range(1,11):   # loop 1 to 10 ascending order

        print(i,"X",n,"=",i*n)  # print the table
        
table()  #function calling 