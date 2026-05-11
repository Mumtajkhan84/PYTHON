# num = 6
# for i in range(1, num):
#     for j in range(i,num):
#         print( end="*")
#     print()


## 1,12,123,1234,12345 next line
# for i in range(1, num):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()




### 1,22,333,4444,55555 next line
# for i in range(1, num):
#     for j in range(1, i+1):
#         print(i, end="")
#     print()


#### wRITE A PROGRAM TO DISPLAY THIS PATTERN 11111, 2222, 333, 44, 5

# for i in range(1, num):
#     for j in range(i, num):
#         print(i, end="")
#     print()

##### WRITE A PROGRAM TO DISPLAY THIS PATTERN 54321, 5432, 543, 54,5
# for i in range(1, num):
#     for j in range(num, i-1, -1):
#         print(j, end="")
#     print()


###### 

# for i in range(1, 6):
#     for j in range(4, i, -1):
#         print(" ", end=" ")
#     for k in range(i):
#         print(" *", end=" ")
#     print()


####### problem solve IMPORTANT
# for i in range(1,6):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()


######### problem solve
# for i in range(1,6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

######### for i in range(1,6):
for i in range(1,6):
    for j in range(1, i+1):
        print(i*j, end=" ")
        
    print()