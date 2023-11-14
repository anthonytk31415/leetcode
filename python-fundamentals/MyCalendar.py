class MyCalendar:

    def __init__(self):
        self.entries = []
        

    def book(self, start: int, end: int) -> bool:
        for s, e in entries: 
            if max(start, s) < min(end, e):
                return False
                
        self.entries.append([start, end])

        return True
