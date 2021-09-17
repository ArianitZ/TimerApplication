import time

class Timer():
    current_time = None

    def __init__(self, time = 0):
        self.current_time = time

    def reset_time(self):
        self.current_time = 0
    
    def set_timer(self, time):
        self.current_time = time

    def decrease_time(self, delta):
        self.current_time -= delta
        self.current_time = self.current_time
   