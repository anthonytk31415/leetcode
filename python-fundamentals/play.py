# import re 

# msg = 'hello world'
# print(f'{msg}')


# print(bool(re.match('^[a-zA-Z0-9]+$', '789def')))
# print(bool(re.match('^[a-zA-Z0-9]+$', '789def')))


# def seq_of_numbers(numstring, returnstring='', count=None, curchar=None):
#     if len(numstring) == 0:
#         returnstring = returnstring + str(count) + curchar
#         return returnstring
#     elif count==None:
#         count = 1
#         curchar = numstring[0]
#         return seq_of_numbers(numstring[1:], returnstring, count, curchar)
#     elif numstring[0]==curchar:
#         count +=1
#         return seq_of_numbers(numstring[1:], returnstring, count, curchar)
#     else:
#         returnstring = returnstring + str(count) + curchar
#         count = 1
#         curchar = numstring[0]        
#         return seq_of_numbers(numstring[1:], returnstring, count, curchar)

# x = seq_of_numbers("31131211131221")
# print(x)
# # print(seq_of_numbers("1211"))



def valid_zip_code(zip):
    first_five = zip[0:5]
    last_four = zip[6:10]
    total_length = len(zip)
    if total_length > 5:
        hyphen = zip[5]
    else:
        hyphen = None
    # check: total length = 5, first 5 valid
    if (first_five.isdigit() and total_length == 5):
        return zip
    # check 2: total length = 10, hyphen, first 5 valid, last 4 valid
    if (total_length == 10 and hyphen == '-' and first_five.isdigit() and last_four.isdigit()):
        return zip
    return False; 


