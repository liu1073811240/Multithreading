# -- coding: utf-8 --
# @Time : 2022/8/1 15:35
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-通过继承Process实现多任务.py
# @Software: PyCharm

from multiprocessing import Process
import time


class MyNewProcess(Process):
    def run(self):
        while True:
            print("---1---")
            time.sleep(1)


if __name__ == '__main__':
    p = MyNewProcess()
    # 调用p.start()方法，p会先去父类中寻找start(), 然后再Process的start()方法中调用run犯法
    p.start()

    while True:
        print('---main---')
        time.sleep(1)

