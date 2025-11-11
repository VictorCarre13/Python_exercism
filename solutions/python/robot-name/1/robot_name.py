import random
import string
class Robot:
    _rng=random.Random() #new generator independants 
    def __init__(self):
        self.reset()
    def reset(self):
        self.name=''.join(self._rng.choices(string.ascii_uppercase, k=2))+''.join(self._rng.choices('0123456789',k=3))
