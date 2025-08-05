 
# def sum(a,b):
#     total = a+b
#     return total


# sum_of_any_number = sum(400,200)
# print(sum_of_any_number)

#-------------------------------------------------------------
def final_cart_amont(*args,discount):
    result = 0
    for amount in args:
        result+=amount

    print(result)

    amount_after_discount = result - (result*discount)

    return amount_after_discount



final_amount_to_be_paid = final_cart_amont(100,500,100,300,500,discount=0.5)
print(final_amount_to_be_paid)

