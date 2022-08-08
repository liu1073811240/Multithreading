# -- coding: utf-8 --
# @Time : 2022/7/27 17:03
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 09-并发TCP服务器.py
# @Software: PyCharm

import socket
import threading

class HandleData(threading.Thread):
    def __init__(self, client_socket):
        super(HandleData, self).__init__()
        self.client_socket = client_socket

    def run(self):
        # 5. 接收/发送数据
        while True:
            recv_content = self.client_socket.recv(1024)
            if len(recv_content) != 0:
                print(recv_content)
                self.client_socket.send(recv_content)
            else:
                self.client_socket.close()
                break


class TCPServer(threading.Thread):
    def __init__(self, port):
        super(TCPServer, self).__init__()
        # 1. 创建套接字
        self.server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2. 绑定本地信息, 设置端口号
        self.server_s.bind(("", port))

        # 3. 将套接字由默认的主动连接模式改为被动模式（监听模块）
        self.server_s.listen(128)

    def run(self):

        while True:
            # 4. 等待客户端进行连接
            new_s, client_info = self.server_s.accept()  # 服务端接收 多个客户端进行连接
            print(client_info)  # ('192.168.133.1', 63889)

            # 创建一个新的线程，专门为刚刚连接的客户端服务
            handle_data_thread = HandleData(new_s)
            handle_data_thread.start()

    def __del__(self):
        # 6. 关闭套接字
        self.server_s.close()


tcp_server = TCPServer(7890)
tcp_server.start()
