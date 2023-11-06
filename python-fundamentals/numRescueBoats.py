from collections import deque
# time: O(nlogn)
# space: O(1)

def countingSort(a):
    b = [0]*len(a)
    c = [0]*(max(a)+1)
    for i in range(len(a)):
        c[a[i]] +=1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i-1]
    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -=1
    return b

def numRescueBoats(people, limit):
    people = countingSort(people)
    people = deque(people)
    counter = 0
    while people: 
        if len(people) == 1: 
            people.pop()
        else: 
            left = people[0]
            right = people[-1]
            if left + right <= limit: 
                people.pop()
                people.popleft()
            else: 
                people.pop()
        counter +=1
    return counter

# people = [1,2]
# limit = 3

# people = [3,2,2,1]
# limit = 3







people = [3,5,3,4]
limit = 5

print(numRescueBoats(people, limit))