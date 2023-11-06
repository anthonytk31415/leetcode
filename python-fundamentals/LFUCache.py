from heapq import heappush, heappop

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.queue = []

    def get(self, key: int) -> int:
        
        

    def put(self, key: int, value: int) -> None: