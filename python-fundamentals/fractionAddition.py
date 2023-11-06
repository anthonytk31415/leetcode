

# print(gcd(12, 78))


def fractionAddition(expression):

    def gcd(a, b):
        if b == 0:
            return a 
        else: 
            return gcd(b, a % b)

    #         0          1          2      3
    # cycle: (+ or -) > integers > (/) > integers 

    fractions = []  # (sign) num, denom
    numerator = True
    cur_num = ''
    cur_denom = ''

    common_denom = 1

    for s in expression:
        if s == '-' or s == '+':
            numerator = True
            if cur_num != '' and cur_denom != '':
                fractions.append([int(cur_num), int(cur_denom)])            
                common_denom *= int(cur_denom)
            cur_num = s
            cur_denom = ''
        
        elif s == '/':
            numerator = False
        
        else: ## it's an integer 
            if numerator == True:
                cur_num += s
            else: 
                cur_denom += s

    fractions.append([int(cur_num), int(cur_denom)])
    common_denom *= int(cur_denom)

    res_num = sum([common_denom * x[0] / x[1] for x in fractions])
    res_denom = common_denom 

    gcDenom = gcd(res_num, res_denom)

    return str(int(res_num/gcDenom)) + '/' + str(int(res_denom/gcDenom))

    # print(fractions, common_denom)
    # print(res_num, res_denom, gcDenom)

expression = "-1/2+1/2+1/3"
print(fractionAddition(expression))