#tupple ma ham bht c values store kr skty hain but is immutable yani change nhi kr skty hain even is say pahly 
#hamy list ko cover kia hy wo mutable hoti hai yani change kr skty hain but tupple immutable hoti hai yani change nhi kr skty hain
tup = (1, 2, 3, 4, 5)
print(tup[0]) #accessing the first element of the tupple
print(tup[1:4]) #accessing a range of elements from the tupple
#what is the defference between empaty tupple and single tupple 
empty_tup = ()
signle_tup1 = (1) #ye single tupple nhi hai ye int hai
single_tup = (1,) #single tupple banany k liye comma lagana zaruri hai warna wo int samjha jayega
print(type(empty_tup))
print(type(signle_tup1))     #ye int hai run kr k dekho result
print(type(single_tup))
#Assignmen 6 create a tupple with 5 elements and print the total number of fruits in the tupple
fruits = ("apple", "banana", "orange", "grape", "kiwi")
print("The total number of fruits in the tupple is:", len(fruits))
#index of one selected fruit in the tupple 
print("The index of orange in the tupple is:", fruits.index("orange"))
print("The index of banana in the tupple is:", fruits.index("banana"))
