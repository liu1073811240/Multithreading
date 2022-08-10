# -- coding: utf-8 --
# @Time : 2022/8/10 11:11
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-使用gevent实现协程2.py
# @Software: PyCharm

import gevent
import random
import time
from gevent import monkey


monkey.patch_all()  # 打补丁。
# 这句话一定要放在 使用time等耗时操作的前面，它最后的效果是 将time模块中的延时 全部替换为gevent中的延时
# time模块中的延时 是不具备 自动切换任务的功能， 而gevent中的延时具备。因为如果不使用这个语句时，我们需要将time全部改为gevent.


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


gevent.joinall([
    gevent.spawn(coroutine_work, "work1"),
    gevent.spawn(coroutine_work, "work2")
])

