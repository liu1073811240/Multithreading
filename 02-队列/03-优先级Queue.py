# -- coding: utf-8 --
# @Time : 2022/7/28 10:02
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 03-优先级Queue.py
# @Software: PyCharm

import queue

q = queue.PriorityQueue()
q.put((10, 'Q'))
q.put((30, 'Z'))
q.put((20, 'A'))

print(q.get())  # (10, 'Q')
print(q.get())  # (20, 'A')
print(q.get())  # (30, 'Z')

'''
小结：
1. 存放的数据是元祖类型，第1个元素表示优先级，第2个元素表示存储的数据。
2. 优先级数字越小优先级越高。
3. 数据优先级高的优先被取出。
4. 用于VIP用户数据优先被取出的场景。因为上面两种都要挨个取出。
'''