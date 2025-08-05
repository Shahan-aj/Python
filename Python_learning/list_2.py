#  Adding two lists

# labour_names = ['Mahesh','Ramesh','Mithilesh','Sumesh']

# new_labour = ['Ram','Mohan']

# labour_names = labour_names + new_labour # we can sipmly use add

# print(labour_names)

# -------------------------------------------------------------------------

# How to access tyhe lists

# labour_names = ['Mahesh','Ramesh','Mithilesh','Sumesh',500,400,400,300]

# print(labour_names[0:2])

# print(labour_names[::-1]) # to print rverse list

# ---------------------------------------------------------------------------

# Length method - to find how many values present inside ( to simply get the count or to get the range of list)

# labour_names = ['Mahesh','Ramesh','Mithilesh','Sumesh',500,400,400,300]

# print(len(labour_names))

# -----------------------------------------------------------------------------

# Insert method

# labour_names = ['Mahesh','Ramesh','Mithilesh','Sumesh',500,400,400,300]

# labour_names.insert(3,"Ram")

# labour_names.append(600)

# print(labour_names)

# ----------------------------------------------------------------------------------

# Pop method - to delete the element from the list

# labour_names = ['Mahesh','Ramesh','Mithilesh','Sumesh',500,400,400,300]

# labour_names.pop() # if no index given inside pop last element is dropped
# print(labour_names.pop())

# -----------------------------------------------------------------------------------

# to change the list value - eg: to edit the spelling of the cureent element

labour_names = ['Maheeh','Rameh','Mithileh','Sumeh',500,400,400,300]
# print(labour_names)
# labour_names[0] = 'Mahesh'
# print(labour_names)

labour_names[0:4] = ['Mahesh','Ramesh','Mithilesh','Sumesh']
print(labour_names)

# ---------------------------------------------------------------------------

# Split method - important for real world programming