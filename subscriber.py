import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages
s.setsockopt_string(zmq.SUBSCRIBE, "SUM")  # subscribe to SUM messages
s.setsockopt_string(zmq.SUBSCRIBE, "DICE")  # subscribe to DICE messages



for i in range(5):  # Five iterations
	time = s.recv()   # receive a message
	print (bytes.decode(time))

	sum = s.recv() # receive a message
	print(bytes.decode(sum))

	dice = s.recv() # receive a message
	print(bytes.decode(dice))

	print("====================================")
