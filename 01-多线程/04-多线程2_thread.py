# -- coding: utf-8 --
# @Time : 2022/7/27 11:17
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-多线程2_thread.py
# @Software: PyCharm

'''
多个线程执行相同的代码
'''

import time
import threading

def say_sorry():
    for i in range(5):
        print("I am sorry")
        time.sleep(1)

t1 = threading.Thread(target=say_sorry)
t2 = threading.Thread(target=say_sorry)

t1.start()
t2.start()


'''
小结:
1.一个程序中，可以有多个线程,执行相同的代码,但是每个线程执行每个线程的功能，互不影响，仅仅是做的事情相同罢了

2.当在创建Thread对象是target执行的函数的代码执行完之后，意味着这个子线程结束。

3.虽然主线程没有了代码，但是它依然会等待所有的子线程结束之后它才会真正的结束，
原因是:主线程有个特殊的功能用来对子线程产生的垃圾进行回收处理。

4.当主线程接收之后,才意味着整个程序真正的结束。

'''
