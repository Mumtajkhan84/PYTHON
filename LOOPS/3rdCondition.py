#1.     WRITE A PROGRAM TO FIND SUM OF ALL THE EVEN NUMBERS UP TO 50
# even = 0
# for num in range(1, 51):
#     if num % 2 == 0:
#         even += num
# print("Sum of even numbers up to 50:", even)


# WRITE A PROGRAM TO WRITE FIRST 20 NUMBER AND THIER SQUARED NUMBERS

## for num in range(1, 21):
#     print(num, "squared is", num**2)




### WRITE A PROGRAM TO FIND SUM OF FIRST 10 ODD NUMBER #USING WHILE LOOP
# sum =0
# num = 1
# while num < 10:
#     if num % 2 != 1:
#         sum += num
#     num += 1
# print("Sum of first 10 odd numbers:", sum)

#### WRITE A PROGRAM TO CREATE IF A NUMBER IS DIVISIBLE BY #8 AND 12, UP TO 100 NUMBERS
# for num in range(1,100):
#     if num%12==0 and num%8==0:
#         print(num)


##### write a programto create a billing system at supercart
while True:
      name = input("enter customer name: ")
      total = 0
      while True:
       print("enter the amount and quantity ")           
       amount = float(input("amount: ")) 
       quantity = float(input("quantity: "))
       total += amount * quantity
       repeat = input("do you want to add more items? (yes/no): ")
       if repeat == "no" or repeat == "No":
           break
     
      print("Total amount for", name, "is:", total)
      print("Thank you for shopping with us!")
       
      repeat1 = input("do you want to add more customers? (yes/no): ")
      if repeat1 == "no" or repeat1 == "No":
           break