# -- coding: utf-8 --
# @Time : 2022/7/28 9:53
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-队列queue.py
# @Software: PyCharm

import queue

q = queue.Queue()
q.put('11')  # 存入字符串
q.put(22)  # 存入整数
q.put({'num': 100}) # 存入字典
q.put(['123', '456'])  # 存入列表

print(q.get())  # 11
print(q.get())  # 22
print(q.get())  # {'num': 100}
print(q.get())  # ['123', '456']

'''
小结：
1. 先进先出 （FIFO）
2. 可以存放任意类型数据
'''

