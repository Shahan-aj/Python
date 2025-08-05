
# create dictionary

labour_with_cost = {'Mahesh':500,"Mithilesh":400,
                    'Ramesh':400,"Sumesh":300}

# update

labour_with_cost["Jagmohan"] = 1000
labour_with_cost["Rampyara"] = 800

# print(labour_with_cost.keys()) # just printing the keys

# print(labour_with_cost.values()) # just printing the values

# print(labour_with_cost.items()) # it gives a tuple of key and value\

# --------------------------------------------------------------------------------------------------

##### when we iterate through a dictionary by default it returns the key ######

# for key in labour_with_cost:
#     print(key,labour_with_cost[key])



# or

# for key,value in labour_with_cost.items():
#     print(key,value)

# accesing list inside a dictionary

data = {"DERF":0,"POENKN":10,"DD":7,"MAINDATA":[{"IDD":"d3454355","BDD":"JSGDJAS"}]}

print(type(data["MAINDATA"]))

for i in range(len(data["MAINDATA"])):
    print(data["MAINDATA"][i]["IDD"])

# for i in range(len(data["MAINDATA"])):
#      print(i)  # it gives the total numbers of lists present inside a dictionary

#---------------------------------------------------------------------------------------

### Assignment

# Total labour cost if total working days was 50 
# out of which Mahesh was absent 3 days and Jagmohan was absent for 7 days
# find out the total labour cost??

total = 0
for day in range(50):
    for name in labour_with_cost:
       total+=labour_with_cost[name]

total_final = total-((3*labour_with_cost["Mahesh"])+(7*labour_with_cost["Jagmohan"]))

print(total_final)

    