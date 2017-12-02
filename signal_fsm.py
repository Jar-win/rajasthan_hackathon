import time

class Signal():
    
    def __init__(offset, change_time, right, left, straight):
        self.offset = 0
        self.right = right
        self.left = left
        self.straight = straight
        self.start_state(self.offset, self.right, self.left, self.straight)

    def start_state(offset, right, left, straight):
        
        time_to_green = 0
        return time_to_green

    

