import socket
import json
import random
import string

def OpClient(tipo_mensagem, data_operacao, conta_cliente, tipo, valor_operacao):
    op_data = {
        "tipo_mensagem": tipo_mensagem,
        "detalhes": {
            "data_operacao": data_operacao,
            "conta_cliente": conta_cliente,
            "tipo": tipo,
            "valor_operacao": valor_operacao
        }
    }
    return json.dumps(op_data)

# Endereço IP e porta do servidor UDP
server_ip = 'coordenador'
server_port = 5000

# Cria um socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tipo_mensagem = 'operacao'
data_operacao = '2024-02-24'
conta_cliente = ''.join(random.choices(string.digits, k=9))
tipo = random.choice(['C', 'D'])  
valor_operacao = round(random.uniform(0.01, 1000.0), 2)

message = OpClient(data_operacao, conta_cliente, tipo, valor_operacao)

# Envia a mensagem ao servidor
client_socket.sendto(message.encode(), (server_ip, server_port))

# Recebe a resposta do servidor
response, server_address = client_socket.recvfrom(1024)

# Exibe a resposta do servidor
print('Mensagem enviada ao servidor:', message)
print('Resposta do servidor:', response.decode())

# Fecha o socket
client_socket.close()