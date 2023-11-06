from functools import lru_cache

# Time: O(M*N)
# Space: O(M*N) for the array for getting min
def minHeightShelves(books, shelfWidth):
    @lru_cache(None)
    def helper(i):
        if i >= len(books): 
            return 0

        curShelfWidth = 0
        # curShelf = []
        curShelfHeight = 0
        res = []
        while i < len(books) and curShelfWidth < shelfWidth:
            thickness, height = books[i]
            if curShelfWidth + thickness <= shelfWidth:
                curShelfWidth += thickness
                # curShelf.append(books[i])
                curShelfHeight = max(curShelfHeight, height)
                i +=1
                res.append(curShelfHeight + helper(i))            
            else:   ## start a new shelf 
                break
        return min(res)

    return helper(0)
        

# books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
# shelfWidth = 4

books = [[1,3],[2,4],[3,2]]
shelfWidth = 6

print(minHeightShelves(books, shelfWidth))