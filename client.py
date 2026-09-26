import socket


def jsend(input):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5000))

    message = input
    client.sendall(message.encode())
    client.close()

def send_wait(input):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5000))

    message = input
    client.sendall(message.encode())

    response = client.recv(1024)
    print(response.decode())

    client.close()  



while True:
    option = input('choose option: ')
    if option in ('a', 'b', 'd'):
        jsend(option)
    elif option == 'c':
        send_wait(option)
    else:
        print('not valid')     
