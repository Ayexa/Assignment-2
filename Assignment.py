# 1-> Create a function that takes a string s and an integer i as parameters and returns a string that
# has in it s reversed and concatenated i times.
# EX: if s is “hello” and i is 2, the function returns “olleholleh”. If i is 0, the function returns an
# empty string.

# def reverse_concatenate(s, i):
#     reverse_s = s[::-1]
#     concatenate_s = reverse_s*i
#     return concatenate_s
#
#
# print(reverse_concatenate("Hello World", 2))

# ----------------------------------------------------------------------------------->
# 2-> Create a function that takes a string s as a parameter and returns another string where all
# the letters in s has been re-arranged such that upper case letters appear before the lower case
# letters.
# EX: if s is “Hello World”, the function returns “HWelloorld”.

# def upper_lower(s):
#     upper = " ".join(i for i in s if i.isupper())
#     lower = " ".join(i for i in s if i.islower())
#     return upper + lower
#
# print(upper_lower("Hello World"))

# ----------------------------------------------------------------------------------->

# 3-> Create a function that takes two strings s1 and s2 as parameters and returns True if s1 is a
# reordering of the characters in s2.
# EX: if s1=”abcde” and s2=”edacb” , the function returns True. If s1=”aabc” and s2=”edabc”,
# the function returns False.

# def reordering(s1, s2):
#     re_s1 = sorted(s1)
#     re_s2 = sorted(s2)
#     if re_s1 == re_s2:
#         return True
#     else:
#         return False
#
# print(reordering("abcde", "edacb"))


# ----------------------------------------------------------------------------------->

# 4-> Python has an inbuilt function called max() that returns the element with the maximum
# value.
# Create a function that does a very similar thing (without using the max() function). The
# function takes a list of numbers l as a parameter and returns the highest number in the list and
# its index.
# EX: if l = [5,6,3,2,7,2,0,1,6], the function should return “the highest value in the list is 7 at
# index 4”


# def find_highest_number(lst):
#     if not lst:
#         return "lst is empty"
#
#     highest_number = lst[0]
#     highest_index = 0
#
#     for i in range(1, len(lst)):
#         if lst[i] > highest_number:
#             highest_number = lst[i]
#             highest_index = i
#
#     return f"highest number is {highest_number} fount at index {highest_index}"
#
# print(find_highest_number([8, 77, 10, 9, 0, 5, 1, 0, 55]))

# ----------------------------------------------------------------------------------->
# 4-> found minimum number:

# def find_highest_number(lst):
#     if not lst:
#         return "lst is empty"
#
#     lowest_number = lst[0]
#     lowest_index = 0
#
#     for i in range(1, len(lst)):
#         if lst[i] < lowest_number:
#             lowest_number = lst[i]
#             lowest_index = i
#
#     return f"lowest number is {lowest_number} fount at index {lowest_index}"
#
# print(find_highest_number([8, 77, 10, 9, 0, 5, 1, 0, 55]))

# ----------------------------------------------------------------------------------->

# 5-> Write a function that counts the digits of a given number recursively.
# Ex : input= 123 output : 3, input 10000 output :5

# def counts(lst):
#     counting = 0
#     for i in lst:
#         counting += 1
#     print(counting)
# counts([1, 4, 5, 7])
