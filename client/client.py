import sys
import socket

def function(host,port):
	s = socket.socket()
	s.connect((host,port))
	print(s.recv(1024))
	s.close()

if __name__=='__main__':
	if len(sys.argv)==1:
		host = str(socket.gethostbyname(socket.gethostbyname()))
	elif len(sys.argv)==2:
		host = sys.argv[1]
		port = 12345
	else:
		host = sys.argv[1]
		port = sys.argv[2]
	
	function(host,port)
