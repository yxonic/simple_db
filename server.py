import socket

def server_program():
    host = 'localhost'  # 连接本地主机
    port = 3000         # 客户端需要与服务器使用相同的端口

    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))  # 绑定主机地址和端口
    
    # 监听连接
    server_socket.listen()
    print(f"Server listening on {host}:{port}")
    
    while True:
        conn, address = server_socket.accept()  # 接受新连接
        print(f"New connection from: {address}")
    
        while True:
            # 接收数据流，数据流的大小为1024字节
            data = conn.recv(1024).decode()
            if not data:
                # 如果数据为空，意味着连接已关闭
                break
            print(f"Received: {data}")
            conn.send(data.encode())  # 发送数据到客户端

        conn.close()  # 关闭连接
        print("Connection closed")

if __name__ == '__main__':
    server_program()
