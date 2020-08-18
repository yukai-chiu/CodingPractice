#Brute force
#Time: O(n^2)
#Space: O(n)
class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if s < end and start < e:
                return False 
        self.calendar.append([start,end])
        return True