 
# def sum(a,b):
#     total = a+b
#     return total


# sum_of_any_number = sum(400,200)
# print(sum_of_any_number)

#-------------------------------------------------------------

# Shopping cart problem

# def final_cart_amont(*args,discount):
#     result = 0
#     for amount in args:
#         result+=amount

#     print(result)

#     amount_after_discount = result - (result*discount)

#     return amount_after_discount



# final_amount_to_be_paid = final_cart_amont(100,500,100,300,500,discount=0.5)
# print(final_amount_to_be_paid)

#-------------------------------------------------------------------------------------

# write a program to take input of n numbers and fins uts sum

l = []
while True:
    user= int(input("enter the number: "))
    print("To check the sum write '-1'")
    l.append(user)
    if user == -1:
        l.pop(-1)
        break
def amount(*args):
    total_sum = 0
    for i in range(len(args)):
        total_sum+=args[i]
    return total_sum
final = amount(*l)
print(final)

# or


# def add(*args):
#     sum=0
#     for arg in args:
#         sum+=arg
#     return sum

# listnumber=[]
# while(True):
#     numbers = input("enter number by space, right done for finsihed: ")
#     if numbers.lower()=='done':
#         break
#     if numbers.isdigit():
#         listnumber.append(int(numbers))
#     else:
#         print("invaild number")

# result=add(*listnumber)
# print(result)

#------------------------------------------------------------------------------------------------------
# write a program in which function take logs input from the user and write this into a file.




