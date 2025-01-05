                                      #list

# list is like a container that store a set of any data type
# friends =["atul",7,False,55.66]
# # print(type(friends[0]))

# friends [0] = " banana"
# print(friends)                 #list are mutable. unlike string
                         #methods
# friends =["atul",7,False,55.66]
# friends.append("gorakh")
# l1=[1,22,45,67,26]
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.pop()
# print(l1)
# l1.insert(3,5656)
# print(l1)


                             #tuple
#they are immutable can not chanage can store any data type
# tuple = ('m','e','f','mh','md','am')
# print(tuple)
# print(tuple[0])

# del tuple # to delete entire tuple
# tuple1 = ('m','e','f','mh','md','am')
# print(tuple1)

        #operator
#concatenation: addting tu tuples(+)
# repetition: multiply(*)
# membership:to see whether item exists in the tuple or not(in or not in)    
# tuple1 = ('m','e','f','mh','md','am')
# tuple2 = (1,3,5,7,9)
# print(tuple1)
# print(tuple2)
# print("concatenation:",tuple1+tuple1)
# print("repetition",tuple2*2)
# print("membership:",1 in tuple2)
# print("membership:",2 not in tuple1)

# # methods
# no = tuple2.count(9)# gives u count how many time that apperar in the tuple
# a = tuple2.index(7)# gives u indes no of the specific number
# print(no)
# print(a)

#tuple function
# tuple2 = (1,3,5,7,9)
# print(tuple2)
# print("min no:",min(tuple2))# give u min number from the tuple
# print("max no:",max(tuple2))# give u max number from the tuple
# print("length no:",len(tuple2))# gives u length of the tuple
# hy =[1,3,5,3]
# print("length no:",tuple(hy)) # convert list into tuple

                             #problem
#1. Write a program to store seven fruits in a list entered by the user
# friends = []

# f1 = input("enter fruit name: ")
# friends.append(f1)
# f2 = input("enter second fruit name:")
# friends.append(f2)
# print(friends)

# #2.Write a program to accept marks of 6 students and display them in a sorted manner.

# marks = []

# s1 = input("enter student makrks: ")
# marks.append(s1)
# s2 = input("enter student makrks:")
# marks.append(s2)
# s3 = input("enter student makrks: ")
# marks.append(s3)

# marks.sort()

# print(marks)

#count zero from the tuple
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
