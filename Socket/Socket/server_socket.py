import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lip = "127.0.0.1"
lport= 12345

server_socket.bind((lip,lport))
server_socket.listen()
print("Listening for connection")
conn, addr = server_socket.accept()
print(f"Connected at address {addr}")

data = conn.recv(1024)

print("Recieved", data.decode())
conn.sendall("server response:".encode())
data.decode()
conn.close()