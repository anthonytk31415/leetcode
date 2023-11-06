# integer to roman


def intToRoman(num):
    base = 10
    res = ''
    roman = {
                1: 'I',
                5: 'V',
                10: 'X',
                50:'L',
                100:'C',
                500:'D',
                1000:'M',
            }
    
    digits = len(str(num)) # how many 10s 
    stack = []              ## throw in smallest first, then process largest first then smallest, to largest 
    while num > 0: 
        diff = num % base
        num = num - diff

        ## take care of the 1-3, 5-8 cases; antic ase: 4, 9
        temp = diff/(base/10)
        if temp == 4:

        elif temp == 9: 



        base *= 10