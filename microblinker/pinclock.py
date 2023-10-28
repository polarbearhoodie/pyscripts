# virtual class with functions state() and tickdown()
class ledState:
    def state(self):
        raise NotImplementedError
    
    def tickDown(self):
        raise NotImplementedError
    

# this is the simplest state;
# it is on or off, unless changed
class constPin(ledState):
    def __init__(self, state):
        self.state = state;


    def tickDown(self):
        pass


    def state(self):
        return self.state
    

# blinks a pin in an on-off cycle for a set number of cycles
class blinker(ledState):
    def __init__(self, on, off, cycles):
        self.on = on 
        self.off = on + off
        self.cycles = cycles - 1
        
        self.time_on = on
        self.time_off = on + off
        return 


    def state(self):
        return self.on > 0


    def tickDown(self, ticks=1):
        if self.on <= 0 and self.off <= 1 and self.cycles > 0:
            self.cycles -= 1
            self.on = self.time_on
            self.off = self.time_off
        
        elif self.off > 0:
            self.on -= 1
            self.off -= 1

        else:
            return


# implement flashing binary
class sequence(ledState):
    def __init__(self, binary):
        pass

# implement flashing morse code
class morse(ledState):
    def __init__(self):
        pass
