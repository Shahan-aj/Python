
# def final_cart_amont(*args,discount):
#     try:
#         result = 0
#         for amount in args:
#             result+=amounts

#         print(result)

#         amount_after_discount = result - (result*discount)

#         return amount_after_discount
#     except TypeError:
#         print("Please provide the amount in integer")
#         raise Exception("value provide is not an integer")
#     # except Exception as e: # this part we generally wite at last for tracing general error for specific error we can write like above TypeError
#     #                         # but once TypeError runs it allow below except Exception to run.
#     #     print(e) #print("cannot provide the cart amount")
#     #     raise e

# try:
#     final_amount_to_be_paid = final_cart_amont(100,500,100,300,"500",discount=0.5) #function call
#     print(final_amount_to_be_paid) # since here we made 500 as string that's why its throwing, here when calling function it gives error
# except Exception as e:
#     print(e)                         #and then when we call function beacuse uske below waala line won't run that's when we use exception handling 
#     # raise e # this will cut the flow from going forward
# print("Entry in Database done. Job Ran succesfully") # try and catch[catching is done from function calling side and we raise exception inside function] this line will be printed and result of function will be showed as None


#---------------------------------------------------------------------------------------------------------------------------
def file_validation(path_to_file):
    with open(path_to_file, "r") as file:
        try:
            columns = file.readline()
            lines = file.readlines()
            unique_rows = set()

            if not columns:
                raise Exception("File is empty")
            if not lines:
                raise Exception("There is NO DATA")

            for line in lines:
                try:
                    data = line.strip().split(',')
                    if len(data) < len(columns.split(",")):
                        raise Exception("value missing for a column")
                                    
                    if not (data[1].startswith('"') and data[1].endswith('"')):
                        raise Exception(f"{line.strip()} : has datatype issue")
                    elif not (data[3].startswith('"') and data[3].endswith('"')):
                        raise Exception(f"{line.strip()} : has datatype issue")
                    else:
                        cleaned_name = data[1].strip('"').strip()
                        cleaned_gender = data[3].strip('"').strip()
                        cleaned_data = f"{data[0]},{cleaned_name},{data[2]},{cleaned_gender}"
                        unique_rows.add(cleaned_data)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    return unique_rows

try:
    result = file_validation(r"C:\Users\70q9136\OneDrive - Panasonic Europe\Documents\Python\assignment.txt.txt")
    print(result)
except Exception as e:
    print (e)
