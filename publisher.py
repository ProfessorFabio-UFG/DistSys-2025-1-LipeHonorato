import zmq, time, random
from constPS import * #-

def sum():
	value1 = random.randint(1,10)
	value2 = random.randint(1,10)
	soma = value1 + value2
	return "Sum from " + str(value1) + " and " + str(value2) + " = " + str(soma)

def loadedDice():
	if random.randint(1,5) == 3:
		a = random.randint(1,6)
		return "The dice roll was: " + str(a)
	else: 
		return "The dice roll was: 4"


context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://"+HOST+":"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:
	time.sleep(5)                    # wait every 5 seconds
	msg = str.encode("TIME " + time.asctime())
	s.send(msg) # publish the current time

	msg1 = str.encode("SUM " + sum())
	s.send(msg1) # publish the msg1

	msg2 = str.encode("DICE " + loadedDice())
	s.send(msg2) # publish the msg2

