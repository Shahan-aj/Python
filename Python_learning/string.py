
# name = 'Manish'

# lst=[1,2,3,4]

# print(name[0:2]) # when we slice string/lis t in output things come togther
# print(lst[0:2])

# for i in name:
#     print(i)

# in string there is lower case and upper case (t and T are treated as different)

# name = 'Manish Kumar'

# counter = 0
# for char in name:
#     print(counter,char)
#     counter+=1

#---------------------------------------------------------------------------------------

# methods in String:

# name = 'mAnisH kuMar'
# print(name.capitalize()) # It capitalize the first letter and rest everything will be outputed as samll letters

# print(name.count("a"))

# python ord() function - Return the integer that represents the character eg:"h":
# print(ord("m"))
# print(ord("A"))

# print(chr(65)) # with ord(charachter) we get integer; and chr(integer) we get character

# print(name.endswith("r")) # it used to cchek whether it ends the specified character and it returns True/false. its used -
                          # to move something that into list and all based on th ending

# print(name.islower()) # also gives True/False now it gives false because our name is combination of capital and small letters. Trues only when
                      # everything is small or low case letters

# name2 = 'AKHMAL'
# print(name2.isupper()) # name1 it gave false and for name2 it gave true

# print(name.lower()) 
# print(name.upper()) # These two are mostly used especially when we're doing joins and all we make both sides either capital or small and do join

# print(name.replace('mAnisH kuMar',"Rohan"))

# name = "manIsh kuMar "
# print(len(name))
# print(name.strip()) # it removes the spaces at front and at the end of a string, just like trim in excel
# print(len(name.strip()))

# print(name.swapcase()) # it swaps caps into small and small into caps within the string

#--------------------------------------------------------------------------------------------------------

# Q) Swap the case of the string without using swapcase inbuilt method for string

# Input:- Programming Aasan Hai
# Output:- pROGRAMMING aASAN hAI 


# input = "Programming Aasan Hai"
# output = ""

# for i in input:
#     if i.isupper():
#         output+=i.lower()
#     elif i.lower():
#         output+=i.upper()
#     else:
#         output+=i

# print(output)

#----------------------------------------------------------------------------------------            
# Q) lst = [random_email id]
# convert this into a****l@gmail.com 

email = input("Enter your email:" )
email = email.split("@")


name = ""
for i in range(len(email[0])):
    if i==0:
        name+=email[0][i]
    elif i==len(email[0])-1:
        name+=email[0][-1]
    else:
        name+="*"

print(name+"@"+email[1])
print(type(email[1]))

#----------------------------------------------------------------------------------------------------

# Q) Print the list of all unique ip addresses?

# input = ["/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
# "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
# "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
# "/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
# "/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
# "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
# "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
# "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
# ]
    
# input = str(input)
# input = input.split("/")
# # print(input)

# output = []
# for i in range(len(input)):
#     if input[i]=="server":
#         i+=1
#         output.append(input[i])


# print(list(set(output)))

# # or

# print(list(dict.fromkeys(output)))




   





