import sys
import socket

debug = True
# the following function in server listens to a port
# ..once there is a request in the port, server sends a string message
def function(port,message="Thank you for connecting"):
	s=  socket.socket()

	print(f"socket created successfully")
	
	try:
		s.bind(('',port))
	except Exception as e:
		print(f"....error in binding the socket: {e}")
		s.close()
		return

	print(f"socket bound successfully to port {port}")
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
	s.close()

def functionSendFile(port,chunk_size = 1024,filename='test.dat'):
	s = socket.socket()

	if debug:
		print(f"socket created successfully")
	
	try:
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind(('',port))
	except Exception as e:
		print(f"....error in binding the socket: {e}")
		s.close()
		return
	
	print(f"socket bound successfully to port {port}")
	s.listen(5)
	print(f"..listening")
	
	while True:
		c,addr = s.accept()
		print(f"..got connection from {addr}")
		c.send(message.encode())
		with open(filename,'rb') as file_handler:
			l = file_handler.read(chunk_size)
			while (l):
				c.send(l)
				l = file_handler.read(chunk_size)
		c.close()
		if debug:
			print(f".. sent file completed")
			print(f"..closing connection")
	return


if __name__=="__main__":
	port = 12345
	chunk_size = 1024
	filename = 'test.dat'

	if len(sys.argv)==1:
		functionSendFile(port)
	elif len(sys.argv)==2:
		port = int(sys.argv[1])
		functionSendFile(port)
	elif len(sys.argv)==3:
		port = int(sys.argv[1])
		chunk_size = int(sys.argv[2])
		functionSendFile(port,chunk_size)
	elif len(sys.argv)>=4:
		port = int(sys.argv[1])
		chunk_size = int(sys.argv[2])
		filename = sys.argv[3]
		functionSendFile(port,chunk_size,filename)