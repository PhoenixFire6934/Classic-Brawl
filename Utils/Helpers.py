import string
import random

class Helpers:

    def randomStringDigits(self):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))

    def randomID(self):
        length = 8
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))

    def randomClubID(self):
        length = 8
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))