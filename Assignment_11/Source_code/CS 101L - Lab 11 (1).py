#############################################################################
##
## CS 101 Lab
## Lab 11
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM:
##  Create a clock class that can keep track of hours, minutes and second.
##
## ALGORITHM:
##  1. Start
##  2. Define class House.
##  3. Define constructor with parameters, hour, minute, second, and clock type.
##      a. Set the default clock type to 0.
##  4. Define __str__ method to override the constructor and display the time.
##      a. Use if-statements to identify whether to display the 24 hour format
##         or the 12 hour format.
##  5. Define tick method to increment the number of hours, minutes, and/or
##     seconds.
##  6. In the main, ask user to input hour, minute, and time.
##  7. Create an object of class Clock and call it in a while loop to display
##     the time continously.
##  8. Stop
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
##############################################################################

class Clock:
    def __init__(self, hour, minute, second, clock_type = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    def __str__(self):
        if self.clock_type == 0: # 24 hour clock
            return '{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second)
        if self.clock_type == 1: # 12 hour clock
            if self.hour >= 13: # hour is 13 or greater --> pm
                hour_dict = {13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 19: 7, 20: 8, 21: 9, 22: 10, 23: 11, 24: 12}
                self.hour = hour_dict[self.hour] # convert 24 hour time clock to 12 hour time clock
                return '{:02}:{:02}:{:02} pm'.format(self.hour, self.minute, self.second)
            if self.hour == 12: # hour is 12 --> pm
                return '{:02}:{:02}:{:02} pm'.format(self.hour, self.minute, self.second)
            if self.hour < 12: # hour is less than 12 --> am
                if self.hour == 0: 
                    self.hour = 12
                    return '{:02}:{:02}:{:02} am'.format(self.hour, self.minute, self.second)
                else:
                    return '{:02}:{:02}:{:02} am'.format(self.hour, self.minute, self.second)

    def tick(self):
        if self.second < 60:
            self.second += 1
        if self.second >= 60:
            self.minute += 1
            self.second = 0
        if self.minute >= 60:
            self.hour += 1
            self.minute =0
        return '{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.second)
            
if __name__ == '__main__':

    import time
    
    hours = int(input('What is the current hour ==> '))
    minutes = int(input('What is the current minute ==> '))
    seconds = int(input('What is the current second ==> '))

    clock = Clock(hours, minutes, seconds, 1)

    while True:
        print(clock)
        clock.tick()
        time.sleep(1)
