import socket

TCP_IP = 'localhost'
TCP_PORT = 5001


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((TCP_IP, TCP_PORT))
    server_socket.listen()

    try:
        while True:
            conn, address = server_socket.accept()
            try:
                while True:
                    message_from_client = conn.recv(256).decode()
                    if message_from_client:
                        print(f"Отримано сповіщення від клієнта {address}: {message_from_client}")
                        conn.send("OK".encode())
                        break
            except KeyboardInterrupt:
                print('Connection destroyed')
            finally:
                print(f'Connection {address} closed')
                conn.close()
    except KeyboardInterrupt:
        print('Server destroyed')
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
