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

# num1 = int(input("Enter num 1 : "))
# num2 = int(input("Enter num 2 : "))

# operator_inp = input("Enter operation : ")

# if(operator_inp == '+'): 
#     print("Result : ", num1 + num2)
# elif(operator_inp == '-'): 
#     print("Result : ", num1 - num2)
# elif(operator_inp == '*'): 
#     print("Result : ", num1 * num2)
# elif(operator_inp == '/'):
#     if(num1 > 0 & num2 > 0):
#         print("Result : ", num1 / num2)
#     elif(num1 == 0): 
#         print("0 cannot be divided")
#     elif(num2 == 0): 
#         print("Cannot divide by 0")


# for i in range(10,0,-1):
#     print(i)

count = 1
# while(count<5):
#     print(count)
#     count+=1


# while True: print("Anirudh")


# for i in range(1,10):
#     if i==3: continue
#     if i==4: pass
#     if i==6: break
#     print(i)


user_choice = True

# while(user_choice):
#     user_input = int(input("Enter the number : "))
    
#     for i in range(1,10):
#         print(f"{user_input} x {i} = {user_input * i}")
    

#     user_input = int(input("Do you want to print another table (1/0): "))

#     if(user_input == 1): user_choice = True
#     elif(user_input == 0): 
#         user_choice = False
#         break


def print_hello():
    print("Hello world")


# print_hello()


def add(a,b):
    return a + b


# print(add(10,12))


def star_args(*marks):
    print("Marks : ", marks)

# star_args(10,20,30,40,50)

def kwargs_arg(**info):
    print("Information : ", info)

# kwargs_arg(name="Anirudh", age=20, email="anirudhhh637@gmail.com")


def ar_sq(side):
    return side**2

# print("Area of square : ", ar_sq(4))


# Creating object
class myClass():
    pass

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("xyz", "abc")

# print(car1.brand)
# print(car1.model)

# class attribute vs object attribute

class college:
    colleges = "ITM" # Class attribute

    def __init__(self, name):
        self.name = name # Object attribute

    def info(self):
        print(f"Name : {self.name}\nCollege : {self.colleges}")


coll = college("Anirudh")

# print(coll.name)
# print(coll.colleges)

# coll.info()

class frt:
    def __init__(self, name):
        self.fruit_name = name

    def __str__(self):
        return f"{self.fruit_name} : Name"
    
f1 = frt("Apple")

# print(f1)


# BHOT ADVANCED CONCEPT -- OOOOOOOOOOOOOOOP


# Encapsulation


class bankAccount:
    def __init__(self, balance):
        self.acc_balance = balance

    def deposit(self,amount):
        self.acc_balance += amount

    def show_balance(self):
        print(f"Total Balance : {self.acc_balance}")

    def withdraw_balance(self, with_amount):
        self.acc_balance -= with_amount

user = bankAccount(5000)

# print(user)

# user.show_balance()

# user.deposit(500)

# user.show_balance()

# user.withdraw_balance(1000)

# user.show_balance()


def print_table(num):
    for i in range(1,10):
        print(f"{num} x {i} = {num * i}")

# print_table(5)


def reverse_num(num):
    rev = 0
    while(num != 0):
        rev = (rev * 10) + (num % 10)
        num //= 10

    print(rev)

# reverse_num(123)