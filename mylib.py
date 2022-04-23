import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.time_in_pause = 0
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()

    def pause(self):
        self.time_in_pause = self.elapsed_time
 
    def unpause(self):
        self.start_time = time.time()
        
    def current_time(self):
        self.elapsed_time = round(time.time() - self.start_time, 2) + self.time_in_pause

    def end(self):
        pass