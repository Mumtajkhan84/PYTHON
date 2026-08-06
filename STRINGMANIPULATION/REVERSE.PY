# Take a input from a user as a string then reverse it

# a = input("Enter a number: ")
# print(a[::-1])

## write a program to check if a string contains only digits
# a = input("Enter a string: ")
# print(a.isdigit())


### WRITE A PROGRAM TO CHECK IF A STRING IS PALINDROME OR NOT
# a = input("Enter a string: ")
# if a == a[::-1]:
#     print("The string is a palindrome.")
# else:    print("The string is not a palindrome.")

### 2nd way to check if a string is palindrome or not
# a = 313
# temp = a
# rev = 0
# while a>0:
#     dig = a %10
#     rev = rev*10 + dig
#     a = a//10
# if temp == rev:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")
    

####WRITE A PROGRAM TO FIND NUMBER OF VOWELS IN A STRING
# a="mumtaj khan is a good devloper"
# count = 0
# for i in a:
#   if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#     count += 1
#     print(i)
# print("Number of vowels in the string:", count)

##### Write a PROGRAM TO CHECK IF EVERY WORD IN  A STRING
#BEGINS WITH A CAPPITAL LETTER
a = str(input("Enter a str"))
b = a.istitle()
print(b)

