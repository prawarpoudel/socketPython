import sys
import socket

def function(port,message="Thank you for connecting"):
	s=  socket.socket()
	print(f"socket created successfully")
	
	s.bind(('',port))
	print(f"socker bound successfully to port {port}")
	s.listen(5)
	print(f"..listening")
	
	while True:
		c,addr = s.accept()
		print(f"..got connection from {addr}")
		c.send(message.encode())
		c.close()
		if(input("listen again(y/n)?")=='y'):
			continue
		else:
			return


if __name__=="__main__":
	port = 12345
	if len(sys.argv)==1:
		function(port)
	elif len(sys.argv)==2:
		port = int(sys.argv[1])
		function(port)
	else:
		port = int(sys.argv[1])
		message = sys.argv[2]
		function(port,message)
