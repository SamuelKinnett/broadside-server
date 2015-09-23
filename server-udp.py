# server.py
import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = '' # symbolic name, all available interfaces

port = 19440

# bind to the port
serversocket.bind((host, port))

while True:
	# wait for an incoming message, maximum size 4096 bytes
	print("Waiting for connection...\n")
	data, address = serversocket.recvfrom(4096)

	print("Received %s bytes from %s, sending response packet" % (str(len(data)),  address))
	currentTime = time.ctime(time.time()) + "\r\n"
	serversocket.sendto(currentTime.encode('ascii'), address)
