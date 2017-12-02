import time
import googlemaps

SIGNAL_SWITTCH_TIME = 10
SPEED_LIMIT = 75


handler = googlemaps.Client("AIzaSyAH3qRKfcvNK-Jv3BFj3Rm2ggs91ElQOjE")
epochstart = time.time()
class Signal_sim:
    def __init__(self, t_step ,num_gates=4):
        self.t_step = t_step
        self.gates = [True]

        for i in range(num_gates-1):
            self.gates.append(False)
    def switch(self):
        for i in range(len(self.gates)):
            if self.gates[i] == True:
                self.gates[i+1] = True
                self.gates[i] = False
                break
    def get_status(self):
        curr_time = time.time()
        rectified = (curr_time - epochstart) % SIGNAL_SWITTCH_TIME * 4
        if rectified < SIGNAL_SWITTCH_TIME:
            return True
        else:
            return False
    def time_to_next_green(self):
        curr_time = time.time()
        rectified = (curr_time - epochstart) % SIGNAL_SWITTCH_TIME * 4
        return 4 * SIGNAL_SWITTCH_TIME - rectified

intersection1 = Signal_sim(10)

def get_speed_stat(curr_lat,curr_long,dest_lat,dest_long):
    itenary = handler.directions((curr_lat,curr_long),(dest_lat,dest_long))
    legss = itenary[0]['legs'][0]['steps']
    total_dist = 0
    for i in range(len(legss)):
        total_dist = total_dist + legss[i]['distance']['value']
    time_left = intersection1.time_to_next_green()
    speed = total_dist/time_left
    while(speed>SPEED_LIMIT):
        time_left = time_left + 40
        speed == total_dist/time_left
    
