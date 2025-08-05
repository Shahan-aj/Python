
# set_variable = set() # this is how if we want define an empty set

set_variable = {1,2,3,2,45,65,3,4,7}

# print(set_variable) # if you print output u can see it came unodered and duplicates are removed

# for number in set_variable:
#     print(number)               # it gives one by one all the elements once

# new_set_variable = {2,4,6,5,15}

# print(set_variable.union(new_set_variable)) # combining everything 

# print(set_variable.intersection(new_set_variable)) # giving common elements

# print(set_variable.isdisjoint(new_set_variable)) # checks whether A and B has common elements or not, if yes returns True or else returns False

# set_variable.add(45)
# print(set_variable)

# set_variable.remove(45) # .discard also can we use 
# print(set_variable)

# set_variable.update(new_set_variable) # its just like union
# print(set_variable)

#---------------------------------------------------------------------------------------

#Q) given two lits, find the missing and additional values in both the lists.

# input :   
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8]

# set_1 = set()
# set_2 = set()

# for i in list1:
#     set_1.add(i)
# for j in list2:
#     set_2.add(j)
# print(f'missing values in List1 is {set_2.difference(set_1)}')
# print(f'missing values in List1 is {set_1.difference(set_2)}')

## or we can simply convert lsit in to set just like we do for tuple
# set_1 = set(list1)
# set_2 = set(list2)
# print(f'missing values in List1 is {set_2.difference(set_1)}')

#-----------------------------------------------------------------------------------

# Q) Given 3 arrays find common elements in 3 of them 

# input

ar1 = {1,5,10,20,40,80}
ar2 = {6,7,20,80,100}
ar3 = {3,4,15,20,30,70,80,120}

# ar4 = ar1.union(ar2)
# common_elements = ar3.intersection(ar4)

# print(f'the number elements are {common_elements}')

# print(type(common_elements))

# output = list(common_elements)
# print(output)

## or we can find iterate it by iteration

final_output = []

for i in ar1:
    if i in ar2 and ar3:
        final_output.append(i)
    else:
        continue

print(final_output)






