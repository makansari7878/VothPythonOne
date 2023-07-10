
# print("hello world")
#
# name = "abc"
# age = 44
#
# print("my name is " + name)
#
# college = "ams"
# a = 10
# b = 4
# c = 11
# if a<b:
#     print("bis greater")
#     if c>a:
#         print("c is greater")
# else:
#     print("a is greater")
#
# for i in range (1,10):
#     print(i)
#
# # mutable or immutable,  ordered or unordered,  duplicate or no duplicate
# #List (mutable, ordered, duplicates)   dictionary
#
# mylist = [3,4,33,5,6, 3]
# print(mylist[0])
# mylist.insert(0,100)
# mytup= {4,5,6,7,8}
#
# print(mylist)
#
# # mydictionary = [{"name": "ansair", "id":101},
# #                 {"name": "abc", "id":102}]
#
# mydictionary = [{"name": "ansair", "id1":101},
#                 {"name1": "ansair", "id2":101},
#                 {"name2": "ansair", "id3":101}
#                 ]
#non parmaterize fun
"""
def playing():
    print("im playing")
    print("im running")

playing()

#parameterize function
def eating(food):
    print("i like this " + food)

eating("pizza")

#return type

def sum(a,b):
    res = a + b
    return  res

print(sum(4,5))
"""

#default parameters
def getDetails(name = "abc", age = 100):

    print(f"my name is {name} and my age is {age}")


getDetails("ansair", 33)
getDetails()
getDetails("ravi")
getDetails(age = 55, name="ramesh")


mydictionary = [{"name": "ansair", "id1":101},
                {"name1": "ravi", "id2":102},
                {"name2": "ramesh", "id3":103}
                ]



