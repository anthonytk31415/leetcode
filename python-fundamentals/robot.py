class Robot:

    def __init__(self, width, height):
        self.xMax = width - 1
        self.yMax = height - 1 
        self.pos = 0
        self.firstMove = True



    def step(self, num):
        self.firstMove = False
        self.pos = (self.pos + num) % (2*(self.xMax + self.yMax))

    def getPos(self):
        curDir = self.getDir()
        if curDir == "East": return  [self.pos, 0]
        if curDir == "North": return [self.xMax, self.pos - self.xMax]
        if curDir == "West": return [ 2*self.xMax + self.yMax - self.pos, self.yMax] 
        if curDir == "South": return [0, 2*(self.xMax + self.yMax) - self.pos] 

    def getDir(self):
        if self.firstMove: 
            return "East"
        if 1 <= self.pos <= self.xMax: return "East"
        if self.xMax + 1 <= self.pos <= self.xMax + self.yMax: return "North"
        if self.xMax + self.yMax + 1 <= self.pos <= 2*self.xMax + self.yMax: return "West"
        if 2*self.xMax + self.yMax + 1 <= self.pos <= 2*(self.xMax + self.yMax): return "South"

    
r = Robot(20,14)
r.step(32)
r.step(18)
r.step(18)
print("pos: ", r.pos)
print("getpos: ", r.getPos())
print("getdir: ", r.getDir())
# r.step(2)
# print("pos: ", r.pos)
# print("getpos: ", r.getPos())
# print("getdir: ", r.getDir())
# r.step(1)
# r.step(4)
# print("pos: ", r.pos)
# print("getpos: ", r.getPos())
# print("getdir: ", r.getDir())