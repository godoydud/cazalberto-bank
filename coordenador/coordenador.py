import socket

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 1024


def enviar_mensagem_credito():
    # Endereço IP e porta do servidor UDP
    server_ip = "shard_a"
    server_port = 6000

    # Cria um socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Mensagem a ser enviada ao servidor
    message = "Olá, shard_a!"

    # Envia a mensagem ao servidor
    client_socket.sendto(message.encode(), (server_ip, server_port))

    # Recebe a resposta do servidor
    response, server_address = client_socket.recvfrom(1024)

    # Exibe a resposta do servidor
    print("Resposta do shard_a:", response.decode())

    # Fecha o socket
    client_socket.close()


def enviar_mensagem_debito():
    # Endereço IP e porta do servidor UDP
    server_ip = "shard_b"
    server_port = 7000

    # Cria um socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Mensagem a ser enviada ao servidor
    message = "Olá, shard_a!"

    # Envia a mensagem ao servidor
    client_socket.sendto(message.encode(), (server_ip, server_port))

    # Recebe a resposta do servidor
    response, server_address = client_socket.recvfrom(1024)

    # Exibe a resposta do servidor
    print("Resposta do shard_a:", response.decode())

    # Fecha o socket
    client_socket.close()


# create a socket UDP to wait listen all clients in the network
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("Servidor UDP esperando conexão na porta", PORT)

while True:
    bytesAddressPair = server_socket.recvfrom(BUFFER_SIZE)
    
    print(bytesAddressPair)

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    # Sending a reply to client

    server_socket.sendto("teste".encode(), address)
