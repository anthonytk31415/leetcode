# - numbers in non increasing order
# - 

def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1
    cur_sum = numbers[i] + numbers[j]
    while numbers[i] + numbers[j] != target: 
        if cur_sum > target: 
            j -=1
        else: 
            i +=1
        cur_sum = numbers[i] + numbers[j]
    return [i+1, j+1]

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))
