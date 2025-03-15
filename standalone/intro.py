# name = "Rishi"
# print(name)
# x = 1
# y = 0.55
# # String -> between "", and its basically a list of characters
# # integer -> a whole number
# # float -> any number with decimal
# # boolean -> True or False (0, 1)

# #Function -> its reusable code, print(data)
# # name: print, arguments: 1, function: writes to the console

# #input(text[optional])
# # name: input, arguments: 0-1, function: takes input from the console(aka the user) and returns it

# if x > y and name != "Rishi":
#   print("True")
# elif name == "Rishi":
#   print(name)
# else:
#   print("False")


# box = input("Enter your age: ")
# print(box)

# # lists and loops
# name = [1,2,3,4,"strings"]
# # 0, 1, 2, 3, 4
# # index, address
# # 1st spot
# print (name[0])
# name[0] = "goob"
# print (name[0])

# # tuples
# name = (1,2,3,4,34,34,3,4,34,3)
# # name[0] = 20, doesn't work!!!

# # coordinates
# # keep track of a specific spot in a list
# tuple = (0,0)
# #tuples cannot be edited

# list = [[1],1]
# list[tuple[0]][tuple[1]]

# #set
# name = {1,2,2,2,2,2,2,2,2,3,4,5}
# print (name)
# l = [1,2,12,2,2,2,2,2222,2,2,2,2,2,2,2]
# l = set(l)
# print (l)
# #sets have no repeats


# # loops, are basically a way to do repetive code or tasks efficiently
# count = 5
# print(count)
# count -= 1
# print(count)
# count -= 1
# print(count)
# count -= 1
# print(count)
# count -= 1
# print(count)
# count -= 1
# print(count)


# # while loop, good for when you don't know how long something should run
# print("WHILE")
# countW = 5
# while countW > -1:
#   print(countW)
#   countW -= 1
#   #code
#   #continue
#   #break

# # for loop, good for when you do know how long something should run
# print("FOR")
# countF = 5
# list = [1,2,3,4,5]
# # range(5) -> [0,1,2,3,4]
# #range(start,end,stride)
# print(range(1,5, 2))
# for i in range(5,-1,-1):
#   print(i)
# # list = [1,2,4, "done"]
# # # iterate
# # for num in list:
# #   if num == 3:
# #     print("found it!")
# for temp in range(2):
#   print("goob")


#lists
# saich_way = ["bob", "jeff", "rob"]
# # index 0,1,2
# # len(list) -1
# print(saich_way)
# print(saich_way[2])


# saich_way.pop(1)
# print(saich_way)
# saich_way.append("jeff")
# print(saich_way)

# saich_way[0] = "jimbo"
# print(saich_way)

# list = [[1,2,3,4],
#         [5,6,7,8]]

# print(list[0][1])

# casting:
# str()
# int()
# float()
# bool()

# list()
# tuple()
# set()

# list, [], is a group of data, that has an order, and can be changed
# tuple, (), is a list that can't be changed
# set, {}, is a list that has no duplicates
# dictionary, {key:value}, its a list with no order (uses keys instead of indexes)


# while else, for else
# attempts = 5
# for i in range(attempts):
#     print(i)
#     if i == 3: # win
#         print("you win")
#         break
# else:
#     print("you lose")

# a = 5
# while a > 0:
#     print(a)
#     if a == 3:
#         print("Error")
#         break
#     a-=1
# else:
#     print("blast off")
