import sys
import socket

debug = True

def function(host,port):
	s = socket.socket()
	s.connect((host,port))
	print(s.recv(1024))
	s.close()

def functionRecvFile(host,port,chunk_size=1024,filename = "test.dat"):
	# create a socket and conenct to the host
	if debug:
		print(f"..opening socket for connection")
	s = socket.socket()
	if debug:
		print(f"..connecting to the host {host}:{port}")
	try:
		s.connect((host,port))
	except Exception as e:
		print(f"....error in connecting to the host: {e}")
		s.close()
		return

	with open(filename,'wb') as file_handler:
		l = s.recv(chunk_size)
		while(l):
			file_handler.write(l)
			l = s.recv(chunk_size)
		if debug:
			print(f"..finished reading the file from server")
	s.close()
	return

if __name__=='__main__':
	print("attempting connection")
	host = str(socket.gethostbyname(socket.gethostname()))
	port = 12345
	filename = 'test.dat'
	chunk_size = 1024
	if len(sys.argv)==2:
		host = sys.argv[1]
	elif len(sys.argv)==3:
		host = sys.argv[1]
		port = sys.argv[2]
	elif len(sys.argv)==4:
		host = sys.argv[1]
		port = sys.argv[2]
		chunk_size = sys.argv[3]
	elif len(sys.argv)>4:
		host = sys.argv[1]
		port = sys.argv[2]
		chunk_size = sys.argv[3]
		filename = sys.argv[4]
	
	functionRecvFile(host,int(port),chunk_size,filename)
