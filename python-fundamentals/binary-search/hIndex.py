def hIndex(citations):


    left = 0
    right = len(citations) - 1
    while left < right: 
        # print(left, right)
        mid = (left + right) // 2
        numCitationsLargerThanMid = len(citations) - mid
        citationScoreMid = citations[mid]
        if citationScoreMid == numCitationsLargerThanMid:
            return numCitationsLargerThanMid
        elif citationScoreMid < numCitationsLargerThanMid: # you can 
            left = mid +1
        else: 
            right = mid - 1
    # print(left, right)
    if citations[left] >= len(citations) - left: return len(citations) - left
    return len(citations) - left - 1


answers = []
answers.append([0,0])
answers.append([100]) # 1
answers.append([1]) # 1
answers.append([0]) # 1
answers.append([0,1,3,5,6]) # 3
answers.append([1,2,100]) # 2
for x in answers: 
    print(x, hIndex(x))