import serial
from collections import deque

serialInst = serial.Serial()

# set this yourself
serialInst.baudrate = 9600
serialInst.port = 'COM5'
serialInst.open()

history = deque([])
average = 0

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        
        try:
          data = int(packet.decode('utf').rstrip('\n'))
          history.append(data)
          print(sum(history)/len(history)) # bad, O(n2)
          
        except:
          print("malformated")

        if len(history) > 50:
            history.popleft()
