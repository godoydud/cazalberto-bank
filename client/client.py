import socket


import json

def OpClient(data_operacao, conta_cliente, tipo, valor_operacao):
    op_data = {
        "data_operacao": data_operacao,
        "conta_cliente": conta_cliente,
        "tipo": tipo,
        "valor_operacao": valor_operacao
    }
    return json.dumps(op_data)

# Endereço IP e porta do servidor UDP
server_ip = 'coordenador'
server_port = 5000

# Cria um socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mensagem a ser enviada ao servidor
message = 'Olá, servidor!'

# Envia a mensagem ao servidor
client_socket.sendto(message.encode(), (server_ip, server_port))

# Recebe a resposta do servidor
response, server_address = client_socket.recvfrom(1024)

# Exibe a resposta do servidor
print('Resposta do servidor:', response.decode())

# Fecha o socket
client_socket.close()