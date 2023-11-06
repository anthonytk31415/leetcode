#buildset



class RandomizedSet:

    def __init__(self):
        self.container = set()

    def insert(self, val: int) -> bool:
        if val not in self.container:
            self.container.add(val)
            return True
        else: 
            return False

    def remove(self, val: int) -> bool:
        if val in self.container:
            self.container.remove(val)
            return True
        else: 
            return False

    def getRandom(self) -> int:
        from random import randint
        return list(self.container)[randint(0, len(self.container) -1)]





a = RandomizedSet()
# print(a.insert(1))
# print(a.insert(1))
# print(a.insert(2))
# print(a.remove(2))
# print(a.remove(2))
# print(a.insert(3))
# print(a.insert(4))
# print(a.insert(5))

a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
# a.remove(1)
# print(1 in a)


print(a.getRandom())

# from random import randint
# z = {1,2,3,4}
# z1 = randint(0, len(z) -1)
# print(z1)