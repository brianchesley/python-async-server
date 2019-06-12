import socket
import sys


host = sys.argv[1]
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

while True:
    response = input("Please enter your message! ")
    sock.send(response.encode("utf-8"))
    msg = sock.recv(1000).decode('utf-8')
    print(msg)
