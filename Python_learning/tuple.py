
# test_tuple = (1,2,45,2,65,2,32,"True","Manish",True) # here one True is string and other one is boolean
# print(type(test_tuple))

# new_tuple = (2)

# print(type(new_tuple)) # if we have a single item inside a tuple type(tuple) != tuple rather str or int based on whats inside


# print(test_tuple[4:7])

# Test_tuple = [1,2,45,2,65,32,"True",2,"Manish",True]

# print(Test_tuple[4:7]) # when slicing last element wont be counted
#-----------------------------------------------------------------------------------

# in method also works in tuple

# if 1 in test_tuple:
#     print(f'the value is present in tuple')
#------------------------------------------------------------------------------------

# methods in tuple

# print(test_tuple.count(2)) # will give count of occurence for the elemnt in tuple

# print(test_tuple.index(2)) # this gives output 1 even though we have 2 at multiple index. It gives first occurence

# ----------------------------------------------------------------------------------

# Q) write a program to return entire element as a tuple which can have a 
#     list in the tuple inputs

test_tuple = ([5,6],[6,7,8,9],[3])

# output = []
# for i in range(len(test_tuple)):
#     for j in test_tuple[i]:
#         output.append(j)

# output_final = tuple(output) # we can convert list into tuple and vice versa

# print(output_final)

# output =[]
# for i in test_tuple:
#     new_var = i              # variable i will catch individual list, and list can be mutaually added
#     output = output+new_var

# print(tuple(output))

# here in this problem time complexity = oder(n), based on how many elements that much time it has to iterate and similarly space complexity = oder(n)

#------------------------------------------------------------------------------------------

# Q) write a program to return a tuple which is exponential of given two tuples as an input

tuple_1 = (10,2,3,5)
tuple_2 = (3,6,4,3)

tuple_output = []
for i in range(len(tuple_1)):
    result = tuple_1[i]**tuple_2[i]
    print(type(result))
    tuple_output.append(result)

print(tuple(tuple_output))