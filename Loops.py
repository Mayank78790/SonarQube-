# Loops in Python - while & for loop 

# while loop 

count = 0 

while count < 5: #condition 
    print(count)
    count = count + 1


# print numbers from 1 to 5 using while loop
count = 1 
while count < 6: #condition 
    print(count)
    # count = count + 1
    count += 1 


count = 5 
while count > 0: #condition 
    print(count)
    # count = count + 1
    count -= 1 
else:
    print("while loop ended")


# while True:
#     print("again and again!!") 
# check conditions to avoid infinite loop


#for loop 

language = 'Python' # sequence 

for x in language:
    print(x) 

# range function
# range(stop)
# range(start, stop)
# range(start, stop, step)

for i in range(5):  # stop argument
    print(i)

for i in range(5,10):     # start, stop argument
    print(i)

for i in range(1,10,3):  # start, stop, step argument
    print(i)

for i in range(5):
    print(i)
else:
    print("for loop ended")


# loop control statements 
# 1. pass statement 

for i in range(5):
    # mann nahi hai 
    pass 

count = 5 
while count > 0:
    if count == 3:
        pass 
    else:
        print(count)
    count -= 1 


#2. break statement 

for i in range(5):
    if i == 3:
        break 
    print(i) 

print("---------")


#3. continue statement 

for i in range(5):
    if i == 3:
        continue 
    print(i) 


# pass statement vs continue statement
count = 5 
while count > 0:
    if count == 3:
        pass 
    else:
        print(count)
    count -= 1 

# continue statement: don't try - infinite loop
# count = 5 
# while count > 0:
#     if count == 3:
#         #continue 
#     else:
#         print(count)
#     count -= 1 


# validate user input: controlled infinite while loop using break statement
while True:
    user_input = input("Enter 'exit' to STOP: ")
    if user_input == 'exit':
        print("congrats! You guessed it right!")
        break 
    print("sorry, you entered: ", user_input) 
    
# Nested Loop

# loop inside another loop is Nested Loop
# syntax

# outer_loop:
#     inner_loop:
#         #block of code for inner loop 
# block of code for outer loop

# print numbers from 1 to 3 for 3 times 

for i in range(3):
    # print("Outer loop iteration no, ", i)
    for num in range(1,4):
        print(num) 
    print("- - -")

# print numbers from 1 to 3 for 3 times using while-for loop : nested loop 
i = 1

while i < 4:
    print("while loop iteration no.", i)
    for j in range(1,4):
        print(j)
    # print("- - -")
    i += 1 


# print prime numbers between range of 2 to 10 using nested loop:

for num in range(2,10):
    for i in range(2,num):
        if num % i == 0: 
            break 
    else:
        print(num) 