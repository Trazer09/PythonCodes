i = 1
n = int(input("Enter the number of rows and columns: "))

while i <= n:
    j = n
    while j >= 1:
        print(j, end=" ")
        j -= 1
    print()  
    i += 1

# n = 4

# for i in range(n):
#     for j in range(n, 0, -1):
#         print(j, end=" ")
#     print()  # Move to the next line after each row of numbers
