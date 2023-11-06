def tupleSameProduct(nums):
    list_sorted = sorted(nums)
    # find the pairs and products i.e. all a, b, a*b, order does not matter
    value_storage = {}
    for i in range(len(list_sorted)-1):
        for j in range(i+1, len(list_sorted)):
            pair = list_sorted[i] * list_sorted[j]
            if pair not in value_storage:
                value_storage[pair] = [[list_sorted[i], list_sorted[j]]]
            else:
                value_storage[pair].append([list_sorted[i], list_sorted[j]]) 
    def sum_k_integers(k):
        return (1/2)*k*(k+1)
    count = 0
    for value in value_storage.values(): 
        x = len(value)
        if x > 1:
            count = count + sum_k_integers(x-1)
    # print(f'{value_storage}')
    return int(count*8)


# z4 =  [2,3,4,6,8,12]
# z5 = tupleSameProduct(z4)
# print(z5)



z6 = [8,448,264,525,435,486,378,308,144,75,196,110,231,120,39,288,50,616,140,261,272,783,225,552,598,30,128,570,322,77,340,19,72,224,294,390,276,87,238,180,80,33,68,210,725,243,696,198,208,46,21,58,360,170,190,510,375,551,348,396,377,69,84,300,572,468,160,24,34,667,29,64,253,115,690,100,870,754,102,1,11,312,609,161,493,450,342,133,588,48,152,10,42,273,440,728,65,98,5,23,250,242,38,182,26,648,99,357,400,275,187,483,414,323,408,105,230,520,750,4,500,32,286,418,189,638,528,234,315,96,352,812,232,40,3,130,184,17,15,324,240,392,7,174,270,416,513,25,203,221,399,475,9,54,476,442,406,840,12,504,114,675,624,621,56,405,125,119,136,506,702,364,70,60,228,20,85,575,135,117,78,171,156,55,299,462,116,780,52,432,165,88,325,338,391,546,522,209,176,108]
z7 = tupleSameProduct(z6)
print(z7)
