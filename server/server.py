import sys
import socket

def function(ipaddress,port,message="Thank you for connecting"):
	s=  socket.socket()
	print(f"socket created successfully")
	
	s.bind('',port)
	print(f"socker bound successfully to port {port}")
	s.listen(5)
	print(f"..listening")
	
	while True:
		c,addr = s.accpet()
		print("..got connection from {addr}")
		c.send(message)
		c.close()

if __name__=="__main__":
	if len(sys.argv)==1:
		ipaddress = str(gethostbyname(gethostbyname()))
		port = 12345
		function(ipaddress,port)
	elif len(sys.argv)==2:
		ipaddress = sys.argv[1]
		port = 12345
		function(ipaddress,host)
	elif len(sys.argv)==3:
		ipaddress = sys.argv[1]
		port = sys.argv[2]
		function(ipaddress,host)
	else:
		ipaddress = sys.argv[1]
		port = sys.argv[2]
		message = sys.argv[3]
		function(ipaddress,port,message)
