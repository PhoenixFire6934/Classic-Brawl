import string
import random
import time

class Helpers:

    def randomStringDigits(self):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))

    def randomID(self):
        length = 9
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))

    def randomClubID(self):
        length = 9
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))
    
    def LeaderboardTimer(self):
        result = time.localtime(int(time.time()))
        day = (result.tm_sec + (result.tm_min * 60) + (result.tm_hour * 3600) + (result.tm_mday * 86400))
        month = result.tm_mon
        if month == 1:
        	seconds = 2764800
        elif month == 2:
        	seconds = 2505600
        elif month == 3:
        	seconds = 2764800
        elif month == 4:
        	seconds = 2678400
        elif month == 5:
        	seconds = 2764800
        elif month == 6:
        	seconds = 2678400
        elif month == 7:
        	seconds = 2764800
        elif month == 8:
        	seconds = 2764800
        elif month == 9:
        	seconds = 2678400
        elif month == 10:
        	seconds = 2764800
        elif month == 11:
        	seconds = 2678400
        elif month == 12:
        	seconds = 2764800

        return (seconds - day)
        
    def EventTimer(self):
        result = time.localtime(int(time.time()))

        return (86400 - (result.tm_sec + (result.tm_min * 60) + (result.tm_hour * 3600)))
