class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        if not self.events:
            self.events.append([start, end])
            return True

        new_events = []
        i = 0
        while i < len(self.events):
            prev_start, prev_end = self.events[i][0], self.events[i][1]
            if end <= prev_start:
                new_events.append([start, end])
                new_events += self.events[i:]
                self.events = new_events
                return True
            elif start >= prev_end:
                new_events.append([prev_start, prev_end])
            else:
                return False
            i += 1
        new_events.append([start, end])
        self.events = new_events
        return True


class MyCalendar1:
    x = MyCalendar()
    print(x.book(10, 20))
    print(x.book(5, 25))
    print(x.book(20, 30))
    print(x.book(20, 30))
    print(x.events)
