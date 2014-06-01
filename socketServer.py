import socket
host=""
port=2013
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.listen(1)
while True:
	conn,addr=serverSocket.accept()
	recvCommand=conn.recv(1024)
	if not recvCommand:
		break
	print("client send message:%s"%recvCommand)
	conn.sendall(recvCommand.upper())
serverSocket.close()



