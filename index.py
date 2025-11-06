name="Anirudh"
age = 20
# print(f"my name is {name} and i am {age} years old")

word = "Python"
# print(word[1::2])

word = "J" + word[1:]
# print(word)

# upper lower both negative


# name = "deepak"
# name = f"{name[0]}a{name[2:]}" #string slicing
# print(name)

# name1 = "deepak"
# name1 = name1.replace(name1[1], 'a') # replace
# print(name1)


ex_str = "   thirty Days of PYTHON  "
# print(dir(ex_str))

li = [10,20,30,40,50]
# print(li[:5:2])

li2 = [3,4]
li3 = li2 * 3
# print(li3)

ex_li = [1,2,3,4,5]

# print(ex_li.pop())
# print(ex_li.pop(1))
# del ex_li[0]
# print(ex_li)
# print(ex_li.remove(3))


fruit_li = ["apple", "banana", "cherry", "apple"]

num_li = [4,3,2,6,8,1]
num_li.sort()


# print(num_li)

ascending_li = sorted(num_li, reverse=False)
# print(ascending_li)


# copying

a = [1,2,3]

b = a.copy()
c = list(a)
d = a[:]

# print(f"{b}\n{c}\n{d}")



# nested condition
matrix = [[1,2,3],[4,5,6]]

# print(matrix[0]) # [1,2,3]
# print(matrix[1][2]) # 6


#  Tuple
example_tuple = (1,2,3)
# print(type(example_tuple))

# empty tuple = ()

# mixed
elem_tuple = ("anirudh", 20, True, [12,13,14], 5.6)
# print(elem_tuple)

# single
single = (4)
# print(single)

# slicing tuple

# print(elem_tuple[1:4])

# elem_tuple[0] = 10
# print(elem_tuple) # TypeError

elem_tuple = list(elem_tuple)

elem_tuple[0] = 10

elem_tuple = tuple(elem_tuple)

# print(elem_tuple)

ex_set = set([1,2,3,4]) # converting list to set

# example_set = {[1,2,3,4]} # cannot store mutable datasets in set
example_set = {1,2,2,4}

# print(type(ex_set))
# print(type(example_set))

# print(ex_set)

# for element in example_set:
#     print(element)

# A | B Union
# A & B Intersection
# A - B Difference
# A ^ B Symmetric Difference

# add()
# update[...]
# remove()
# discard()
# pop()
# copy()
# clear()


li1 = [1,2,3,4,5,6,6,7]
li_set = set(li1)

# print("List : ", li1)
# print("Set list : ", li_set)

fs = frozenset([1,2,3,4,5])
# print(fs)

# print(3 in li1)

ex_dict = {
    "name": "Anirudh",
    "age": 20,
    "contact_info" : {
        "country" : "India",
        "city" : "Gwalior"
    } 
}
ex_dict["email"] = "anirudhhh637@gmail.com"

# del ex_dict -- remove element
# get() -- get method

# for element in ex_dict:
#     print (f"{element} : {ex_dict[element]}")


# print(ex_dict)


# input_store = input("Enter name : ")
# print("Input name : ", input_store)

# if(input_store.lower() == 'admin'):
#     print("ok")
# else :
#     print("no ok")


# input_amount = int(input("enter amount : "))
balance = 5000

# if(input_amount <= balance): print("Transaction successful")
# elif(input_amount > balance): print("Cannot transact more than availalbe balance")
# elif(input_amount == 0): print("Cannot withdraw 0")
# else: print("Enter valid amount")

num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num 2 : "))

operator_inp = input("Enter operation : ")

if(operator_inp == '+'): 
    print("Result : ", num1 + num2)
elif(operator_inp == '-'): 
    print("Result : ", num1 - num2)
elif(operator_inp == '*'): 
    print("Result : ", num1 * num2)
elif(operator_inp == '/'):
    if(num1 > 0 & num2 > 0):
        print("Result : ", num1 / num2)
    elif(num1 == 0): 
        print("0 cannot be divided")
    elif(num2 == 0): 
        print("Cannot divide by 0")