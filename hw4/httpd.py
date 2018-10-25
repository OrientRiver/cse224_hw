import sys
import socket
import os
import time


class MyServer:
    def __init__(self, port, doc_root):
        self.port = port
        self.doc_root = doc_root
        self.host = "localhost"

    def __judge(self, GET, HOST, user_agent):
    	# error code type judge here
    	return 200

    def __response(self, error_code, path):
    	if error_code == 200:
	    	HTTP_version = 'HTTP/1.1'
	    	server = 'Myserver 1.0'
	    	last_modified = time.strftime('%a, %d %b %y %T %z', time.gmtime(os.path.getmtime(path)))
	    	content_name, content_suffix = os.path.splitext(path)
	    	file_type = {'.html': 'text/html', '.jpg': '/image/jpeg', '.png': 'image/png'}
	    	content_type = file_type[content_suffix]
	    	content_length = os.path.getsize(path)
	    	with open(path, 'r') as file:
	    		content = file.read()
	    		response = HTTP_version + ' 200 OK \r\nServer: ' + server + '\r\nLast-Modified: ' + last_modified + '\r\nContent-Type: ' + content_type + '\r\nContent-Length: ' + str(content_length) + '\r\n\r\n' + content
	    	return response



    def start(self):
    	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    		s.bind((self.host, self.port))
    		while True:
    			s.listen()
    			conn, addr = s.accept()
    			with conn:
    				print('Connected by', addr)
    				data = conn.recv(1024)
    				requestData = data.decode(encoding = "ascii")

    				# handle
    				print(requestData)
    				request = requestData.split('\r\n')
    				GET = request[0].split(' ')
    				HOST = request[1].split(' ')
    				user_agent = request[2].split(' ')
    				error_type = self.__judge(GET, HOST, user_agent)

    				if error_type == 200:
    					# error code 200 handle
    					print(GET, HOST, user_agent)
    					# path = 'C:/Users/ChenlinLiu/Desktop/homework/cse224_hw/hw4' + GET[1]
    					path = self.doc_root + GET[1]
    					response = self.__response(200, path)
    					print(response)
    					conn.sendall(response.encode(encoding = 'ascii'))

    				# else if:
    				# error code 400, 404 handle here





if __name__ == '__main__':
    input_port = int(sys.argv[1])
    input_doc_root = sys.argv[2]
    server = MyServer(input_port, input_doc_root)
    # Add code to start your server here
    server.start()

