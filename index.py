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

print(elem_tuple[1:4])

# elem_tuple[0] = 10
# print(elem_tuple) # TypeError

elem_tuple = list(elem_tuple)

elem_tuple[0] = 10

elem_tuple = tuple(elem_tuple)

print(elem_tuple)