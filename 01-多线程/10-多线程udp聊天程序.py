# -- coding: utf-8 --
# @Time : 2022/7/27 18:01
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 10-多线程udp聊天程序.py
# @Software: PyCharm

import socket
import threading

def send_msg(udp_socket):
    '''
    获取键盘数据，并将其发送给对方
    :param udp_socket:
    :return:
    '''
    while True:

        # 2. 输入对方的ip地址
        dest_ip = input("\n请输入对方的ip地址：")

        # 3. 输入对方的port
        dest_port = int(input("\n请输入对方的port："))

        while True:
            # 1. 从键盘输入数据
            msg = input("\n请输入要发送的数据：")
            if msg:
                # 4. 发送数据
                udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))
            else:
                break


def recv_msg(udp_socket):
    """接受数据并显示"""
    while True:
        # 1. 接受数据
        recv_msg = udp_socket.recvfrom(1024)
        # 2. 解码
        recv_ip = recv_msg[1]
        recv_msg = recv_msg[0].decode("utf-8")
        # 3. 显示接收到的数据
        print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地信息
    udp_socket.bind(("", 7890))

    send_msg_t = threading.Thread(target=send_msg, args=(udp_socket,))
    recv_msg_t = threading.Thread(target=recv_msg, args=(udp_socket,))

    send_msg_t.start()
    recv_msg_t.start()


if __name__ == '__main__':
    main()
