import socket

# Defina a porta e o tamanho do buffer
PORT = 5000
BUFFER_SIZE = 1024
HOST = "0.0.0.0"

# Crie um socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associe o socket ao endereço e à porta
server_socket.bind((HOST, PORT))

print("Servidor UDP esperando conexão na porta", PORT)

while True:
    data, address = server_socket.recvfrom(BUFFER_SIZE)

    # Converta a mensagem recebida para uma string e imprima
    print("Mensagem recebida:", data.decode())
    # Envie uma resposta de volta para o cliente
    server_socket.sendto("Resposta do servidor".encode(), address)
