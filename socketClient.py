import socket
host="127.0.0.1"
port=2013
cSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cSocket.connect((host,port))
while True:
	sendCommand=input("enter some command:")
	if not sendCommand:
		break
	cSocket.sendall(sendCommand)
	recvResult=cSocket.recv(1024)
	print("server return result:",recvResult)
cSocket.close()
