i = 1
n = int(input("Enter the number of rows and columns: "))

while i <= n:
    j = n
    while j >= 1:
        print(j, end=" ")
        j -= 1
    print()  
    i += 1
