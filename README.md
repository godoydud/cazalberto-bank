# cazalberto-bank
<img src="./img/default_765x625.png">

## Descrição 
Este é um projeto *cazalberto-bank* para a disciplina de Computação Distribuída da [Universidade Federal do Mato Grosso do Sul](https://www.ufms.br/).
Neste trabalho, utilizamos o protocolo UDP para trafegar mensagens e armazenar em uma fila implementada no Transaction Coordinator.

Para simularmos um ambiente de computação distribuída, estamos utilizando o Dockerfile.

# Como executar?
Clone o repositório utilizando o comando do Git.
Após isso, execute os comandos:

```
docker-compose up --build
```


## Requisitos do trabalho

### Cliente
A função OpClient() deve ser implementada no cliente com os seguintes parâmetros:
- Data da operação
- Conta do cliente
- Tipo de operação (C para crédito ou D para débito)
- Valor da operação

### Transaction Coordinator

A função Credito() deve ser implementada no Transaction Coordinator e enviar os seguintes parâmetros para o Shard A:
- Data da operação
- Conta do cliente
- Valor da operação

A função Debito() deve ser implementada no Transaction Coordinator e enviar os seguintes parâmetros para o Shard B:
- Data da operação
- Conta do cliente
- Valor da operação

### Shards
O Shard A deve implementar a função Credito que recebe os parâmetros:
- Data da operação
- Conta do cliente
- Valor da operação

O Shard B deve implementar a função Debito que recebe os parâmetros:
- Data da operação
- Conta do cliente
- Valor da operação