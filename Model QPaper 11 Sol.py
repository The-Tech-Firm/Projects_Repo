"""Chapter STRING"""
"""Q1 Palindrome Test"""

# user_string = input("Enter string: ")

# list_str = user_string.split(" ")

# length = len(list_str)

# joiner = ""

# for i in range(length,-1):
#     joiner = list_str[i] + list_str[i]
    
# rev_joiner = joiner[::-1]
# if rev_joiner.casefold() == joiner.casefold():
#     print(f"\"{user_string}\" is a Palindrome String")
# else:
#     print(f"{user_string} is not a Palindrome String")


"""Q2 Display even position elements from a user input."""

user_string = "String"

length = len(user_string)
print("The even position elements are: ")
list1 =[]
for i in range(0, length):
    if i%2 == 0:
        list1.append(user_string[i])
    else:
        continue

print(*list1, sep=", ")


