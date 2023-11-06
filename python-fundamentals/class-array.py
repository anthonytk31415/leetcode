## currently incomplete

class arr:
    def __init__(self):
        self.len = 0
        self.val = {}
        self.arrayMax = 10
        for i in range(self.arrayMax):
            self.val[i] = None
    # def __iter__(self):
    #     return self

    


    def read(self, index):
        if self.val[index]:
            return self.val[index]
        else:
            raise Exception("index is out of range :(")
        
    def push(self, value):
        ''' insert a new value at the length of the array. then increase length by 1. double the array if needed (accomodate array Max'''
        key = self.len
        self.len +=1
        # if the array needs to grow, accomodate by doubling its size


    # def pop
    # def shift
    # def unshift
    # def indexOf
    # ''' returns the index of first occurance of the value in the array or returns an error'''
    # def resize

x = arr()
