class Test:
    def __init__(self): 
        self.counter = 0

    def increment(self):
        self.counter +=1
    

z = Test()

z.increment()
print(z.counter)
z.increment()
print(z.counter)