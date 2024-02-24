import socket
import json

# Defina a porta e o tamanho do buffer
PORT = 5000
BUFFER_SIZE = 1024
HOST = "0.0.0.0"

# Crie um socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associe o socket ao endereço e à porta
server_socket.bind((HOST, PORT))

# enviar mensagem de operações de debito ao shard_a na porta 6000
def enviar_mensagem_debito():
    shard_a_ip = 'shard_a'
    shard_a_port = 6000
    message = "operacao de debito"
    server_socket.sendto(message.encode(), (shard_a_ip, shard_a_port))
    print("mensagem de debito enviada")

# enviar mensagem de operações de credito ao shard_b na porta 7000
def enviar_mensagem_credito():
    shard_b_ip = 'shard_b'
    shard_b_port = 7000
    message = "operacao de credito"
    server_socket.sendto(message.encode(), (shard_b_ip, shard_b_port))
    print("mensagem de credito enviada")


print("Servidor UDP esperando conexão na porta", PORT)

while True:
    data, address = server_socket.recvfrom(BUFFER_SIZE)

    # Converta a mensagem recebida para uma string e imprima
    print("Mensagem recebida:", data.decode())
    mensagem_recebida = json.loads(data.decode())
    
    try:
        if mensagem_recebida["tipo_mensagem"] == "operacao":
            print("OPERACAO RECEBIDA:", mensagem_recebida)
            if mensagem_recebida["detalhes"]["tipo"] == "C":
                enviar_mensagem_credito()
            elif mensagem_recebida["detalhes"]["tipo"] == "D":
                enviar_mensagem_debito()
        elif mensagem_recebida["tipo_mensagem"] == "commit":
            print("COMMIT RECEBIDO:", mensagem_recebida)
    except:
        print("mensagem inválida recebida")
        server_socket.sendto("mensagem inválida".encode(), address)
    
    # Envie uma resposta de volta para o cliente
    server_socket.sendto("Resposta do servidor".encode(), address)
