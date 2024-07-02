n = int(input("Enter the number of rows and columns: "))
count = 1
i = 0

while i < n:
    j = 0
    while j < n:
        print(count, end=" ")
        count += 1
        j += 1
    print()  # Move to the next line after each row
    i += 1
