# -- coding: utf-8 --
# @Time : 2022/8/1 17:54
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 05-进程间通信-Queue.py
# @Software: PyCharm

from multiprocessing import Queue

q = Queue(3)
q.put("消息1")
q.put("消息2")
print(q.full())  # False
q.put("消息3")
print(q.full())  # True

# 因为消息队列已满，所以会导致下面的try都会抛出异常。
# 第一个try会等待2秒后再抛出异常
# 第二个try会立刻抛出异常

try:
    q.put("消息4", timeout=2)

except:
    print("消息队列已满，现有消息数量：%s" % q.qsize())

try:
    q.put_nowait("消息4")
except:
    print("消息队列已满，现有消息队列：%s" % q.qsize())


# 推荐的方式，先判断消息队列是否已满，再写入。
if not q.full():
    q.put_nowait("消息4")

# 读取消息时，先判断消息队列是否为空，再读取。
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())

