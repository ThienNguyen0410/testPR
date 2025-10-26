import socket
import os
#Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "1234"
port = 80
sock.bind((server_ip,port))
sock.listen()

