import time

class Clock():
    def __init__(self, hour = 0, minute = 0, second = 0, clock_format = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_format = clock_format
    def __str__(self):
        if self.clock_format == 0:
            return '{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second)
        elif self.clock_format == 1:
            if self.hour > 12:
                return '{:02}:{:02}:{:02} pm'.format(self.hour - 12, self.minute, self.second)
            elif self.hour == 0:
                return '{:02}:{:02}:{:02} am'.format(self.hour + 12, self.minute, self.second)
            else:
                return '{:02}:{:02}:{:02} am'.format(self.hour, self.minute, self.second)
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.clock_format == 0:
                    if self.hour == 24:
                        self.hour = 0
                elif self.clock_format == 1:
                    if self.hour == 24:
                        self.hour = 0

def get_inputs():
    while True:
        try:
            hour = int(input('Enter the current hour: '))
            break
        except ValueError:
            print('Enter an integer please.')
    while True:
        try:
            minute = int(input('Enter the current minute: '))
            break
        except ValueError:
            print('Enter an integer please.')
    while True:
        try:
            second = int(input('Enter the current second: '))
            break
        except ValueError:
            print('Enter an integer please.')
    return hour, minute, second

if __name__ == "__main__":
    hour, minute, second = get_inputs()
    clock_format = int(input('Enter 0 for 24 hr clock or 1 for 12 hr clock: '))
    while (clock_format != 1) and (clock_format != 0):
            clock_format = int(input('Enter 0 for 24 hr clock or 1 for 12 hr clock: '))
    clock1 = Clock(hour, minute, second, clock_format)
    while True:
        print(clock1)
        clock1.tick()
        time.sleep(1)