import socket

TCP_IP = 'localhost'
TCP_PORT = 5001


def main():

    client_socket = socket.socket()
    client_socket.connect((TCP_IP, TCP_PORT))

    message = input(">> ").lower().strip()

    if len(message):
        while True:
            client_socket.send(message.encode())
            message_from_server = client_socket.recv(256).decode()
            if message_from_server == "OK":
                print(f'Cервер підтвердив отримання сповіщення')
                break
            else:
                print('Smth wrong wth server. Send message again')

    client_socket.close()


if __name__ == '__main__':
    main()
