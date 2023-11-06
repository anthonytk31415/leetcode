from random import uniform, randint
from bisect import bisect


class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.prob = []
        self.buildProb()
    # for each rectangle, give the x0, x1 coordinates, append to array, then sort them
    #then do the same for the y coordinates
    def buildProb(self):
        total_area = 0
        for a, b, x, y in self.rects: 
            area = (x - a + 1) * (y-b +1)
            total_area += area
            self.prob.append(area)
        
        self.prob = list(map(lambda x: x/total_area, self.prob))
        print(self.prob)
        for i in range(1, len(self.prob)):
            self.prob[i] = self.prob[i] + self.prob[i-1]
        print(self.prob)

    def pick(self):
        rand = uniform(0, 1)
        idx = bisect(self.prob, rand)
        a, b, x, y = self.rects[idx]
        x_rand = randint(a, x)
        y_rand = randint(b, y)
        return [x_rand, y_rand]

sol = Solution([[82918473,-57180867,82918476,-57180863],[83793579,18088559,83793580,18088560],[66574245,26243152,66574246,26243153],[72983930,11921716,72983934,11921720]])
# sol = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
print(sol.pick())
print(sol.pick())




# sol = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
# print(sol.pick())
# print(sol.pick())
# print(sol.pick())
