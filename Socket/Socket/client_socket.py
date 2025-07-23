import socket

from Cryptodome.IO.PEM import encode

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )

lip= "127.0.0.1"
lport =12345

client_socket.connect((lip,lport))

client_socket.sendall("message from the client" .encode())
data = client_socket.recv(1024)
print("Recieved:", data.decode())

client_socket.close()




