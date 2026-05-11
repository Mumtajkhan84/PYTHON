# for num in range(1, 10):
#     if num==6:
#         print("six")
#     else:
#         print(num)


## 2nd problem
count = 0
for num in range(1,100):
    if num%12==0 and num%8==0:
        count+=1
        print(num)
print("Sum of numbers divisible by both 12 and 8:", count)