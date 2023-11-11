from math import inf 

# You basically brutally backtrack. No tricks here. One optimization: there's no difference between person 1 and person 2 in terms of the 
# pattern of the distribution. E.G. 1,2,3 is no different than 3,2,1. So we can just initiate with putting the first item to person 1. 

# Time: O(k^(n-1))
# Space: O(k^(n-1)) for storing the path for each iteration

def distributeCookies(cookies, k):
    # path[i] = the int of where the cookie belongs to which person, person 0, ... k - 1 = k total people

    minOverallMax = [inf]

    def dfs(j, path):

        if j == 0: 
            totalCookieValue = [0 for _ in range(k)]
            for i in range(len(path)):
                person = path[i]
                totalCookieValue[person] += cookies[i]
            maxCookiePerson = max(totalCookieValue)
            minOverallMax[0] = min(maxCookiePerson, minOverallMax[0])
            return  
    
        for i in range(k):
            dfs(j - 1, path + [i])

    dfs(len(cookies) - 1 ,[1])
    return minOverallMax[0]

# cookies = [8,15,10,20,8]
# k = 2

# cookies = [6,1,3,2,2,4,1,2]
# k = 3

cookies = [76265,7826,16834,63341,68901,58882,50651,75609]
k = 8

print(distributeCookies(cookies, k))