#conditional statements in python 
marks = input("Enter your marks: ")
if marks >= "90":
    print("A+")
elif marks >= "80":
    print("A")
elif marks >= "70":
    print("B")
elif marks >= "60":
    print("C")
elif marks >= "50":
    print("D")
else:
    print("Fail")


    
   #list of pythn assignment enter three fruits name and store in a list and print the list and lengyh of th list
fruit1 = input("Enter the name of first fruit: ")
fruit2 = input("Enter the name of second fruit: ")
fruit3 = input("Enter the name of third fruit: ")
fruits = [fruit1, fruit2, fruit3]
print("The list of fruits is:", fruits)
print("The length of the list is:", len(fruits))
