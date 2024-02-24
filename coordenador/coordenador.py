import socket
import json
import queue

# Defina a porta e o tamanho do buffer
PORT = 5000
BUFFER_SIZE = 1024
HOST = "0.0.0.0"

# Crie um socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associe o socket ao endereço e à porta
server_socket.bind((HOST, PORT))

# fila de mensagens
fila_de_mensagens = queue.Queue()


# enviar mensagem de operações de debito ao shard_a na porta 6000
def enviar_mensagem_debito(message):
    shard_a_ip = 'shard_b'
    shard_a_port = 7000
    message = f"operacao de debito: Cliente {message['conta_cliente']} Valor: {message['valor_operacao']}"
    server_socket.sendto(message.encode(), (shard_a_ip, shard_a_port))
    print("mensagem de debito enviada")

# enviar mensagem de operações de credito ao shard_b na porta 7000


def enviar_mensagem_credito(message):
    shard_b_ip = 'shard_a'
    shard_b_port = 6000
    message = f"operacao de credito: Cliente {message['conta_cliente']} Valor: {message['valor_operacao']}"
    server_socket.sendto(message.encode(), (shard_b_ip, shard_b_port))
    print("mensagem de credito enviada")


print("Servidor UDP esperando conexão na porta", PORT)


def processar_mensagem(mensagem):
    commit = ""
    try:
        if mensagem["tipo_mensagem"] == "operacao":
            if mensagem["detalhes"]["tipo"] == "C":
                enviar_mensagem_credito(mensagem["detalhes"])
                mensagem = {
                    "tipo_mensagem": "commit",
                    "detalhes": {
                        "mensagem": "OK",
                    }
                }
                server_socket.sendto(
                    str(json.dumps(mensagem)).encode(), address)
            elif mensagem["detalhes"]["tipo"] == "D":
                enviar_mensagem_debito(mensagem["detalhes"])
                mensagem = {
                    "tipo_mensagem": "commit",
                    "detalhes": {
                        "mensagem": "OK",
                    }
                }
                server_socket.sendto(
                    str(json.dumps(mensagem)).encode(), address)
            print("OPERACAO RECEBIDA:", mensagem)
        elif mensagem["tipo_mensagem"] == "commit":
            print("COMMIT RECEBIDO:", mensagem)
            commit = mensagem
    except:
        print("mensagem inválida recebida")
        pass


while True:
    data, address = server_socket.recvfrom(BUFFER_SIZE)

    # Converta a mensagem recebida para uma string e imprima
    print("Mensagem recebida:", data.decode())
    mensagem_recebida = json.loads(data.decode())

    # Adiciona a mensagem à fila
    fila_de_mensagens.put(mensagem_recebida)

    # Processa todas as mensagens na fila
    while not fila_de_mensagens.empty():
        mensagem = fila_de_mensagens.get()
        processar_mensagem(mensagem)
