import socket

HOST = '0.0.0.0'
PORT = 5000
BUFFER_SIZE = 50

def main():
    # create a socket UDP to listen and print all message received
    print("Hello from coordenador")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            data, addr = s.recvfrom(BUFFER_SIZE)
            print(f"Received {data.decode()} from {addr}")

if __name__ == "__main__":
    main()
    