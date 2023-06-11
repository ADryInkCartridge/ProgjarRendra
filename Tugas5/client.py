import socket

server_address = ('localhost', 44444)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)