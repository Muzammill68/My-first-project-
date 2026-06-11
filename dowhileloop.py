#print a program from 1 to 10

num = 1
while num <= 10:
    print(num)
    num += 1
print("question one completed ")
# print a program from 10 to 1
num1 = 10
while num1 >= 1:
    print(num1)
    num1 -= 1
print("question two completed ")

#now the question three is to print the even numbers from 1 to 50
num2 = 1
while num2 <= 50:
    if num2 % 2 == 0:
        print(num2)
    num2 += 1
print("question three completed ")

#now get input from the user and print the sum the numbers from 1 to that number
num3 = int(input("Enter any number u want: "))
sum = 0
i = 0
while i<=num3:
    sum += i
    i += 1
    print(i)
print("The sum of the numbers from 1 to " + str(num3) + " is " + str(sum))
print("question four completed ")
#now the next question
#print the pattern shown below using while loop
# *
# * *
# * * *
# * * * * 
i = 1
while i <= 4:
    print("* " * i)
    i += 1
print("question five completed ")
#now the next question is to print the name of the user 5 times with the number of times it has been printed
name = input("Enter your name: ")
i = 1
while i <= 5:
    print(str(i) + ". " + name)
    i += 1
    #next question is get the input from user and print the table of that number
    num4 = int(input("Enter any number to print its table: "))
    i =1
    while i<=10:
        print(f"{num4} x {i} = {num4*i}")
        i += 1
        #now the table question is completed
        