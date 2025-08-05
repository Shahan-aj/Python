
labour_name = ["Mahesh","Ramesh","Mithilesh","Sumesh"]

for i in range(len(labour_name)):
    print(i)
count =1
for i in range(len(labour_name)):
    print(f' labour {count} name is {labour_name[i]}')
    count += 1

print(count)

# (or)

# for i in range(len(labour_name)):  # len(labou_name)=4 then range(4)= 0,1,2,3 this is how the logic flows
#     print(f' labour {i+1} name is {labour_name[i]}')

# # ----------------------------------------------------
# for name in labour_name:
#     print(name)
# --------------------------------------------------------------------

# pattern printing

# print(2*'$')


# for i in range(6):
#     print(i*" *")

# ---------------------------------------------------------------------------

# print all the ven number from 1 to 100

# for number in range(101):
#     if (number%2==0):
#         print(number)

# ---------------------------------------------------------------------------

# for i in range(4,0,-1):
#     print(i*" *")