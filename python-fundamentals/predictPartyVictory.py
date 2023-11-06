from collections import deque

def predictPartyVictory(senate):
    r_count = 0
    d_count = 0
    r_debt = 0
    d_debt = 0
    first = None
    queue = deque()
    for i, x in enumerate(senate): 
        print(r_count, r_debt, d_count, d_debt, i, x)
        if x == 'R':
            if d_debt > 0: 
                d_debt -=1
            else: 
                if d_count > 0: 
                    d_count -=1
                else: 
                    
                    r_debt += 1
                r_count +=1
        elif x == 'D': 
            if r_debt > 0: 
                r_debt -= 1
            else: 
                if r_count > 0:
                    r_count -=1
                else: 
                    d_debt += 1
                d_count +=1
    
    
    print(r_count, r_debt, d_count, d_debt)

# senate = 'RRDDRRDD'
#           xx  xx
# senate = 'RDRDRD'
#          x x x

# senate = 'DDRRRRD'
#         xxxx  

# senate = 'RRDDRDD'
senate = 'RDDDRR'
#          x  
#         x x x


print(predictPartyVictory(senate))



#        RRDDRR
# r_debt 121012
# d_debt 

#        RRDDRRDD   
# r_debt 12101210
# d_debt         1210

#     RRDDDDR
#       xx  
#     xx  x x

# rd  1210  
# dd        
# rc  12  10 
# dc      121      

#     RDR
# rd  1
# dd
# rc  1
# dc