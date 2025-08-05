
# list
# lst_of_numbers = ["1","2","3","56","32"]

# result = " ".join(lst_of_numbers)
# print(result)

#--------------------------------------------------
#Dictionary - with join it directly just join the keys not values because join only works on string

# labour_with_cost = {'Mahesh':500,"Mithilesh":400,
#                     'Ramesh':400,"Sumesh":300,
#                     "Jagmohan":1000,"Rampyare":800}

# result = " # ".join(labour_with_cost)
# print(result)


#-----------------------------------------------------------------------------------

# state_dept_info = [{"state":"Bihar","department":"IT"}
#                     ,{"state":"Delhi","department":"Marketing"}]

# # Find out all the employee name who are available in the above condition.
# # you don't know the exact number of filter condition
# # which will come in the above list. It can change in each run.

# query = """select * from(
# select e.employee_name, e.state, e.zip, e.salary, d.department
# from employee_tbl e
# inner join department d
# ON e.emp_id = d.emp_id
# )a
# where salary>100000"""

# final_filter_condition = []

# for condition in state_dept_info:
#     for key,value in condition.items():
#         final_filter_condition.append(f"{key} = {value}")

# print(final_filter_condition)

# result = " OR ".join(final_filter_condition) ## "".join() method converts here list(final_filter_condition) into string(result) if you look at this problem
# print(query + " AND " + result)
# # print(type(result)

#-----------------------------------------------------------------------------------------------------------

# Q1. Secure the PII data.
Input = ["mverma6250@gmail.com","ramesh02@hotmail.com",
        "sohansingh@gmail.com","swatirahane@outlook.com"]

# Input = ["m********0@gmail.com","r******2@hotmail.com",
#         "s********h@gmail.com","s*********e@outlook.com"]

encrypted_emails = []

for email in Input:
    name,domain = email.split("@")
    if len(name)>2:
        masked = name[0] + "*"*(len(name)-2) + name[-1]
    else:
        masked = name[o]+"*"

    masked_emails = masked + "@" + domain
    encrypted_emails.append(masked_emails)

print(encrypted_emails)

            