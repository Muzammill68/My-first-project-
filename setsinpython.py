#sets in python
#A set is a collection which is unordered, unchangeable*, and unindexed. In Python, sets are written with curly brackets.
myset = {"apple", "banana", "cherry" , "apple" , "banana"} #u can see that we have added "apple" twice but it will only be stored once in the set because sets do not allow duplicate values.
print(myset)
print(type(myset)) #u can see in the result its type is set.
#we can also use the set() constructor to create a set.
myset2 = set(("apple", "banana", "cherry"))
print(myset2)
print(type(myset2)) #u can see in the result its type is set.
empty_set = set() #u cannot create an empty set using empty curly brackets because it will create an empty dictionary instead, so you have to use the set() constructor to create an empty set.
print(type(empty_set)) #u can see in the result its type is set.
#clear() method is used to remove all the elements from the set.
myset.clear()
print(myset) #u can see in the result the set is empty now.