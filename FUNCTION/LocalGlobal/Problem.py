#1 WRITE A PROGRAM TO FIND MAXIMUM OF THREE NUMBERS IN PYTHON
# def maximum_num(val1, val2, val3):
#     if val1>val2 & val1>val3:
#         print("val1 is gretest of three number", val1)
#     elif val2>val1 & val2>val3:
#         print ("val2 is greter than of three val;ue", val2)
#     else:
#         print("val3 is greter than of three number", val3)
        
# maximum_num(5,6,9)       



#2 WRITE A PYTHON FUNCTION TO CREATE AND PRINT A LIST WHERE THE VALUE
#ARE SQUARE OF NUMBERS BETWEEN 1 AND 30.
# def square_num():
#     square = []
#     for i in range(1,31):
#         square.append(i**2)
#     return square
# print(square_num())



###3 WRITE A PYTHON FUNCTION THAT TIMES A NUMBER AS A PARAMETER AND CHECK IF THE NUMBER 
# IS PRIME OR NO  

# def check_prime(num):
#     if num == 1:
#         print("it is not prime number")
#     if num == 2:
#          print("it is not prime number")
#     if num>2:
#          for i  in range(2, num):
#           if num % i==0:
#             print("it is not prime number:")
#             break
#           else:
#               print("It is prime number:")

# check_prime(5)   


####4 WRITE A PYTHON FUNCTION TO SUM ALL THE NUMBERS  IN A LIST
# def add(numbers):
#     total = 0
#     for i in numbers:
#         total = total + 1
#         return (total)
# print(add([10, 11, 12, 13]))




#####5 WRITE A PYTHON PROGRAM TO SOLVE THE FIBONACCI SEQUENCE AND RECURSION
def fs(num):
     if num == 1:
         return 0
     elif num==2:
         return 1
     else:
         return (fs(num-1) + fs(num-2))
     
print(fs(8))