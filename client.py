import socket

def client_program():
    host = 'localhost'  # 连接本地主机
    port = 3000         # 客户端需要与服务器使用相同的端口

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("> ")  # 等待用户输入命令

    while message.strip() != 'exit':
        client_socket.send(message.encode())  # 发送数据到服务器
        data = client_socket.recv(1024).decode()  # 接收从服务器返回的数据
        print(data)
        message = input("> ")  # 再次等待输入命令

    client_socket.close()

if __name__ == '__main__':
    client_program()
