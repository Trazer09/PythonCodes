# rows and columns 
#  * one row with one column

#  * * one row with two column

#  * * two row with two column
#  * *


i = 0
n = int(input("Enter the number of rows and columns: "))

while i < n:
    j = 0
    while j < n:
        print("*", end=" ") # Print * followed by a space, without adding a newline
        j += 1
    print("\n")  # Print a newline after each row
    i += 1


    