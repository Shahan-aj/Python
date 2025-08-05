

labour_with_cost = {'Mahesh':500,"Mithilesh":400,
                    'Ramesh':400,"Sumesh":300,
                    "Jagmohan":1000,"Rampyare":800}


# get method

# its also used to get the values for a specific key, but if key not in range it won't throw error rather gives out as "None" when compared eg: labour_with_cost[Mahes1] here it throws error

# print(labour_with_cost.get("Mahesh1")) # this gave out simply None, and rest of code will run without breaking, so this more used in real time.
# print(labour_with_cost["Mahesh1"]) # code will break due to error

#----------------------------------------------------------------------------

# Keys and Values

# print(labour_with_cost.keys())
# print(labour_with_cost.values())

#---------------------------------------------------------------------------------

# item method

# print(labour_with_cost.items()) # will give key value pair in a tuple

#----------------------------------------------------------------------------------

# update method

# print(labour_with_cost.update({'Manish':700})) # if we apply print() it gives "None", update simply append won't give any output

# new_dict = {"Manish":700,"Ram":800} 
# final_dict = {**labour_with_cost,**new_dict} # in reality rather than update method we merge dictionaries from various sources like this

# print(final_dict)

#-----------------------------------------------------------------------------------

# pop method

# print(labour_with_cost.pop("Mahesh")) # pop unlike update method we can print the deleted value and store it in a variable and use it
# labour_with_cost.popitem()     #The popitem() method removes the item that was last inserted into the dictionary 

#-----------------------------------------------------------------------------------

# Copy method

# new_labour_cost = labour_with_cost.copy() # different memory allocation

#--------------------------------------------------------------

#clear method

# labour_with_cost.clear()

# -----------------------------------------------------------

## Dictionary comprehension

# labour_with_cost = {'Mahesh':500,"Mithilesh":400,
#                     'Ramesh':400,"Sumesh":300,
#                     "Jagmohan":1000,"Rampyare":800}
# if we want to increase price of everyone by 100

# for key in labour_with_cost:
#     labour_with_cost[key]+=100

# print(labour_with_cost)

# now same with comprehension
# labour_with_cost = {key:labour_with_cost[key]+100 for key in labour_with_cost}

# if we don't want to involve 'Jagmohan"

# labour_with_cost = {key:labour_with_cost.get(key)+100 if key!="Jagmohan"
#                     else labour_with_cost.get(key)
#                     for key in labour_with_cost}

# print(labour_with_cost)

#----------------------------------------------------------------------------------------------------------------

## IN Method

# In interview they ask where we us IN method in dictionary or in list and where it will be faster

# name = 'Manish Kumar'

# letter_count = {}
# for letter in name:
#     if letter in letter_count:
#         letter_count[letter] +=1
#     else:
#         letter_count[letter] = 1

# print(letter_count)

# in dictionary using in we're storing keys in hash table and do the lookup for values, it reduces the time (time complexity, time is order of 1) but increases the space (sapce complexity, time order of n)

# --------------------------------------------------------------------------------------------

#Assignment

# data = {"DERF":0,"POENKN":10,"DD":7,"MAINDATA":[{"IDD":"d3454355","BDD":"5678hfjhjh","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"148877564"},{"FieldTypeName":"H3","Value":"20230930"},{"FieldTypeName":"H4","Value":"20231130"},{"FieldTypeName":"H5","Value":"2441.56"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"2411.56"},{"FieldTypeName":"H8","Value":"EUR"},{"FieldTypeName":"H9","Value":"00115190035"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"4500575382"},{"FieldTypeName":"H12","Value":"0.00"},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":""},{"FieldTypeName":"H15","Value":"F0"},{"FieldTypeName":"H16","Value":"87"},{"FieldTypeName":"H17","Value":"0.00"},{"FieldTypeName":"H18","Value":""},{"FieldTypeName":"H19","Value":""},{"FieldTypeName":"H20","Value":"No"}],"CodingLines":[],"Tables":[{"N1":"233553","N2":"3555","N3":"ASDDDD","N4":"334324","N5":"900.00","N6":"1.29","N7":"387.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"765765","N2":"67657657","N3":"ADFDFF)","N4":"667657","N5":"1000.00","N6":"1.94","N7":"1940.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"67657","N2":"76576576576","N3":"SFDFFDFSDF","N4":"7667676","N5":"1000.00","N6":"0.11456","N7":"114.56","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""}],"INININ":"148877564","SDRER":"null"},{"IDD":"frret5","BDD":"5trtry4566","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"ICI2300397"},{"FieldTypeName":"H3","Value":"20231219"},{"FieldTypeName":"H4","Value":"20240331"},{"FieldTypeName":"H5","Value":"76.44"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"76.44"},{"FieldTypeName":"H8","Value":"INR"},{"FieldTypeName":"H9","Value":"56676765"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"0.00"},{"FieldTypeName":"H12","Value":""},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":"F1"},{"FieldTypeName":"H15","Value":"87"},{"FieldTypeName":"H16","Value":"0.00"},{"FieldTypeName":"H17","Value":""},{"FieldTypeName":"H18","Value":""}],"CodingLines":[{"CODE1":0.0,"CODE2":76.44,"CODE3":"5645654","CODE4":"","CodingFields":[{"FieldName":"COL1","Value":"223DD666"},{"FieldName":"COL2","Value":"3454545"},{"FieldName":"COL3","Value":""},{"FieldName":"COL5","Value":""},{"FieldName":"COL5","Value":""}]}],"Tables":[],"INININ":"DER3434","SDRER":"null"}],"Final":"JKHJKLH0909908"}

# print(data.keys())

# print(type(data["MAINDATA"]))

# print(type(data["Final"]))

# count =0
# for i in data['MAINDATA']:
#     for j in i['HeaderFields']:
#         for k in j:
#             if k =='FieldTypeName':
#                 count+=1
# print(count)

#-------------------------------------------------------------------------------------------------------

# name = "Divya Akhmal"
# letter_count = {}

# for char in name:
#     if char in letter_count:
#         letter_count[char]+=1
#     else:
#         letter_count[char]=1

# print(letter_count)