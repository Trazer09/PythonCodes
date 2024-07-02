i = 1
n = int(input("Enter the number of rows and columns: "))

while i <= n:
    j = 1
    while j <= n:
        print(i, end=" ") # Print * followed by a space, without adding a newline
        j += 1
    print("\n")  # Print a newline after each row
    i += 1
