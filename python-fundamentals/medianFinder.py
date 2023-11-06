# find median 
# for find median, 
# time: O(nlogn)
# space: O(n)  

class MedianFinder:

    def __init__(self):
        self.container = []
        self.med_index = []

    def addNum(self, num: int) -> None:
        self.container.append(num)
        self.container = sorted(self.container)
        if len(self.container) % 2 == 0:
            self.med_index = [len(self.container) //2, len(self.container)// 2 - 1]
        else: 
            self.med_index = [len(self.container)//2]

    def findMedian(self) -> float:
        if len(self.med_index) == 1: 
            return self.container[self.med_index[0]]
        else: 
            return (self.container[self.med_index[0]] + self.container[self.med_index[1]])/2