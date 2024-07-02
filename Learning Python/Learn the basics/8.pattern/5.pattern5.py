# n = 4
# i = 1

# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print()  # Move to the next line after each row
#     i += 1


# * 
# * * 
# * * * 
# * * * * 


# n = 4
# i = 1
# num = 1

# while i <= n:
#     j = 1
#     while j <= i:
#         print(num, end=" ")
#         num += 1
#         j += 1
#     print()  # Move to the next line after each row
#     i += 1


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 


# n = 4
# i = 1

# while i <= n:
#     j = i
#     while j > 0:
#         print(j, end=" ")
#         j -= 1
#     print()  # Move to the next line after each row
#     i += 1

# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 

# n = 3
# i = 0

# while i < n:
#     j = 0
#     while j < n:
#         print(chr(65 + i), end=" ")
#         j += 1
#     print()  # Move to the next line after each row
#     i += 1

# A A A 
# B B B 
# C C C 


# n = 4
# i = 0

# while i < n:
#     j = 0
#     while j <= i:
#         print(chr(65 + (n - 1 - i) + j), end=" ")
#         j += 1
#     print()  # Move to the next line after each row
#     i += 1

# D 
# C D 
# B C D 
# A B C D 

# n = 3
# i = 1

# while i <= n:
#     # Print leading spaces
#     j = n
#     while j > i:
#         print(" ", end=" ")
#         j -= 1

#     # Print asterisks
#     k = 1
#     while k <= i:
#         print("*", end=" ")
#         k += 1

#     print()  # Move to the next line after each row
#     i += 1

#     * 
#   * * 
# * * * 


# n = 4
# i = 0

# while i < n:
#     # Print leading spaces
#     j = 0
#     while j < i:
#         print(" ", end=" ")
#         j += 1

#     # Print asterisks
#     k = i
#     while k < n:
#         print("*", end=" ")
#         k += 1

#     print()  # Move to the next line after each row
#     i += 1

# * * * * 
#   * * * 
#     * * 
#       * 


# n = 4
# i = 1

# while i <= n:
#     # Print leading spaces
#     j = 0
#     while j < n - i:
#         print("  ", end=" ")
#         j += 1

#     # Print ascending numbers
#     k = 1
#     while k <= i:
#         print(k, end=" ")
#         k += 1

#     # Print descending numbers
#     k = i - 1
#     while k >= 1:
#         print(k, end=" ")
#         k -= 1

#     print()  # Move to the next line after each row
#     i += 1


#           1 
#         1 2 1 
#       1 2 3 2 1 
#     1 2 3 4 3 2 1 

# n = 5
# i = 1

# while i <= n:
#     # Print numbers in increasing order
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1

#     # Print asterisks
#     k = 1
#     while k <= (n - i) * 2:
#         print("*", end=" ")
#         k += 1

#     # Print numbers in decreasing order
#     j = i
#     while j >= 1:
#         print(j, end=" ")
#         j -= 1

#     print()  # Move to the next line after each row
#     i += 1

# 1 2 3 4 5 5 4 3 2 1 
# 1 2 3 4 * * 4 3 2 1 
# 1 2 3 * * * * 3 2 1 
# 1 2 * * * * * * 2 1 
# 1 * * * * * * * * 1 

# n = 5

# # Print upper triangle
# for i in range(1, n + 1):
#     # Print left side of the pattern
#     for j in range(1, i + 1):
#         print("*", end=" ")

#     # Print spaces in the middle
#     for j in range(1, 2 * (n - i) + 1):
#         print(" ", end=" ")

#     # Print right side of the pattern
#     for j in range(1, i + 1):
#         if j == i:
#             print("*", end="")
#         else:
#             print("*", end=" ")

#     print()  # Move to the next line

# # Print lower triangle
# for i in range(n - 1, 0, -1):
#     # Print left side of the pattern
#     for j in range(1, i + 1):
#         print("*", end=" ")

#     # Print spaces in the middle
#     for j in range(1, 2 * (n - i) + 1):
#         print(" ", end=" ")

#     # Print right side of the pattern
#     for j in range(1, i + 1):
#         if j == i:
#             print("*", end="")
#         else:
#             print("*", end=" ")

#     print()  # Move to the next line

# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 * 


# n = 5

# # Print upper triangle
# for i in range(1, n + 1):
#     # Print numbers in ascending order
#     for j in range(1, i + 1):
#         print(j, end=" ")

#     # Print asterisks
#     for j in range(1, 2 * (n - i) + 1):
#         print("*", end=" ")

#     # Print numbers in descending order
#     for j in range(i, 0, -1):
#         print(j, end=" ")

#     print()  # Move to the next line

# # Print lower triangle
# for i in range(n - 1, 0, -1):
#     # Print numbers in ascending order
#     for j in range(1, i + 1):
#         print(j, end=" ")

#     # Print asterisks
#     for j in range(1, 2 * (n - i) + 1):
#         print("*", end=" ")

#     # Print numbers in descending order
#     for j in range(i, 0, -1):
#         print(j, end=" ")

#     print()  # Move to the next line

# 1 * * * * * * * * 1 
# 1 2 * * * * * * 2 1 
# 1 2 3 * * * * 3 2 1 
# 1 2 3 4 * * 4 3 2 1 
# 1 2 3 4 5 5 4 3 2 1 
# 1 2 3 4 * * 4 3 2 1 
# 1 2 3 * * * * 3 2 1 
# 1 2 * * * * * * 2 1 
# 1 * * * * * * * * 1 


# n = 5
# start_number = 1

# for i in range(1, n + 1):
#     for j in range(1, n - i + 2):
#         print(start_number, end=" ")
#         start_number += 1
    
#     for j in range(1, i):
#         print(start_number, end=" ")
#         start_number += 1
    
#     print()


# 1 2 3 4 5 16 17 18 19 20 
# 6 7 8 9 21 22 23 24 
# 10 11 12 25 26 27 
# 13 14 28 29 
# 15 30 

# n = 4

# for i in range(1, 2 * n):
#     for j in range(1, 2 * n):
#         min_distance = min(i, j, 2 * n - i, 2 * n - j)
#         print(n - min_distance + 1, end="")
#     print()

# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444
