import socket
HOST = 'cse224.sysnet.ucsd.edu'
PORT = 5555
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	s.sendall(b'A53284481\r\n')
	temp = s.recv(1024)
	data = temp
	while True:
		temp = s.recv(1024)
		if temp == b'':
			break
		data = data + temp  

print('received', repr(data))