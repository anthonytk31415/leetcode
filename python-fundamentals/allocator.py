

## Time: 
# - allocate is O(N)
# - instantiate: O(N) for creation of array
# - free: O(N)
## Space: 
# - O(N) storage
# - O(N) for allocate, since you have the lps array
# - O(1) for 

class Allocator:
    def __init__(self, n: int):
        self.b = [None]*n
        self.n = n

    @staticmethod
    def lpsArray(pat, m, lps):
        len = 0
        lps[0] = 0
        i = 1
        while i < m: 
            if pat[i] == pat[len]:
                len +=1
                lps[i] = len
                i +=1
            else: 
                if len != 0: 
                    len = lps[len-1]
                else: 
                    lps[i] = 0
                    i +=1

    def kmp(self, size):
        # m = size
        # n = self.n
        lps = [0]*size
        pat = [None]*size
        self.lpsArray(pat, size, lps)
        # print(lps)
        i = 0
        j = 0
        while (self.n - i) >= (size - j):
            if self.b[i] == pat[j]:
                i +=1
                j +=1
            if j == size: 
                return i - j
            elif i < self.n and self.b[i] != pat[j]:
                if j != 0: 
                    j = lps[j-1]
                else: 
                    i +=1
        return -1

    def allocate(self, size: int, mID: int) -> int:
        index = self.kmp(size)
        if index == -1: 
            return -1
        for i in range(size):
            self.b[index+i] = mID
        return index
        
    def free(self, mID: int) -> int:
        counter = 0
        for i in range(len(self.b)):
            if self.b[i] == mID:
                self.b[i] = None
                counter +=1
        return counter




# Your Allocator object will be instantiated and called as such:
loc = Allocator(10)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

loc.allocate(1,1)
loc.allocate(1,2)
loc.allocate(1,3)
print(loc.free(2))
loc.allocate(3,4)
print(loc.b)