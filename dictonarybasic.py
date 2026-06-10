#dictonary is a collection which is unordered, changeable and indexed. In python dictionaries are written with curly brackets, and they have keys and values.
student = {"name": "Muzammil",
            "age": 20,
            "city": "Karachi",
            "course": "Python",
            "roll_no": 101}
print(type(student))
print (student)
#we can access the items of a dictionary by referring to its key name, inside square brackets.
print(student["name"])
print(student["age"])
print(student["city"])
print(student["course"])
print(student["roll_no"])
#we can also use the get() method to access the items of a dictionary.
print(student.get("name"))
print(student.get("age"))
print(student.get("city"))
print(student.get("course"))
print(student.get("roll_no"))
#we can change the value of a specific item by referring to its key name.
student["age"] = 21
print(student)
student["course"] = "Data Science" #u can see the value of course is changed to data science
#we can also use the update() method to change the value of a specific item.
student.update({"course": "Machine Learning"})
print(student)
#we can add new key in the dictionary by referring to the new key name and assigning a value to it.
student["email"] = "muzammil@example.com"
print(student)
student["phone"] = "1234567890"
#we can remove an item from thhe dictonarty by using the pop() method and specifying the key name of the item we want to remove.
student.pop("phone")
print(student)
#we can print keys and values of the dictionary by using the keys() and values() method.
print(student.keys())
print(student.values())
print(student.items()) #will print the key and value pairs of the dictionary as a list of tuples.
print(len(student)) #will print the number of key-value pairs in the dictionary.
print(student["name"]) #will print the value of the key "name" in the dictionary.
