# -- coding: utf-8 --
# @Time : 2022/7/28 14:15
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-带有聊天记录的udp聊天程序.py
# @Software: PyCharm
import queue
import threading
import socket

class RecvMsg(threading.Thread):
    def __init__(self, udp_s, q):
        super(RecvMsg, self).__init__()
        self.udp_s = udp_s
        self.q = q

    def run(self):
        while True:
            recv_content, client_info = self.udp_s.recvfrom(1024)  # 接受信息
            # print(">>>%s(%d):%s" % (client_info[0], client_info[1], recv_content.decode("gbk")))  # 发送过来的数据是gbk格式，需要转换
            temp_content = ">>>%s(%d):%s" % (client_info[0], client_info[1], recv_content.decode("gbk"))
            self.q.put(temp_content)

    def __del__(self):
        self.udp_s.close()


class SendMsg(threading.Thread):
    def __init__(self, udp_s, q):
        super(SendMsg, self).__init__()
        self.udp_s = udp_s
        self.q = q

    def run(self):
        while True:
            dest_ip = input("请输入对方的IP：")
            dest_port = int(input("请输入对方的port:"))

            while True:
                send_content = input("请输入要发送的数据：")
                if send_content:
                    self.udp_s.sendto(send_content.encode("utf-8"), (dest_ip, dest_port))
                    temp_info = "<<<%s(%d):%s" % (dest_ip, dest_port, send_content)
                    self.q.put(temp_info)
                else:
                    break

    def __del__(self):
        self.udp_s.close()


class ChatHistory(threading.Thread):
    def __init__(self, q):
        super(ChatHistory, self).__init__()
        self.q = q

    def run(self):
        while True:
            # 从Queue中读取数据
            content = self.q.get()
            # 将数据写入到文件中
            with open("./chat.txt", "a", encoding='GBK') as f:
                f.write(content + '\n')


def main():
    # 1. 创建一个udp套接字
    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地信息
    udp_s.bind(("", 7890))

    # 创建一个FIFO的队列
    q = queue.Queue()

    # 3. 创建一个新的线程对象，目的用来接受数据
    recv_msg_thread = RecvMsg(udp_s, q)

    # 4. 创建一个新的线程对象，目的用来检测键盘发送数据
    send_msg_thread = SendMsg(udp_s, q)

    # 5. 创建一个新的线程对象，目的用来存储聊天记录
    chat_history_thread = ChatHistory(q)

    recv_msg_thread.start()
    send_msg_thread.start()
    chat_history_thread.start()


if __name__ == '__main__':
    main()



