import time
import googlemaps
handler = googlemaps.Client("AIzaSyAH3qRKfcvNK-Jv3BFj3Rm2ggs91ElQOjE")

class Signal_sim:
    def __init__(self, t_step ,num_gates=4):
        self.t_step = t_step
        self.gates = [True]
        self.last_update_time =  time.hepochstart = time.time()

        for i in range(num_gates-1):
            self.gates.append(False)
    def switch(self):
        for i in range(len(self.gates)):
            if self.gates[i] == True:
                self.gates[i+1] = True
                self.gates[i] = False
                break

intersection1 = Signal_sim(10)

def Get_Speed_Stat(curr_lat,curr_long,dest_lat,dest_long):
    

while True:
    
    
    
