str = input("Enter the name of owner: ")
mid = len(str) // 2
output1 = str[mid-1:mid+2]
print("Middle three characters of the name is " + output1)
output2 = str[-2:]
print("last two characters of the name is " + output2)
str1 = "Khan sahab"
print(str1.upper())
print(str1.lower())
print(str1.find("ab"))
name = "Muzammil yaseen"
age = 20
print(f"My name is {name} and my age is {age}")
print(name.title())
print(name.replace("Muzammil", "Ghulam"))
print(name.capitalize())