import socket
import json

HOST = '0.0.0.0'
PORT = 6000
BUFFER_SIZE = 4096

print("shard_a recebendo operações de crédito instanciado")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print('Servidor UDP esperando conexão na porta', PORT)

while True:
    message, client_address = server_socket.recvfrom(BUFFER_SIZE)
    print('Mensagem recebida do cliente',
          client_address, ':', message.decode())

    mensagem = {
        "tipo_mensagem": "commit",
        "detalhes": {
            "mensagem": "OK",
        }
    }
    server_socket.sendto(str(json.dumps(mensagem)).encode(), client_address)
