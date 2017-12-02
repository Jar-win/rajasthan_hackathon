import time

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

intersection1 = Signal_sim(10)
    
