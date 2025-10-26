import socket
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = "1234"
port = 80
sock.connect((server_ip,port))
print("Connect successfully")
