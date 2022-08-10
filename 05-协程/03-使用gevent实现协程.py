# -- coding: utf-8 --
# @Time : 2022/8/10 10:25
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 03-使用gevent实现协程.py
# @Software: PyCharm

import gevent
import time
from gevent import monkey

monkey.patch_all()  # 打补丁。
# 这句话一定要放在 使用time等耗时操作的前面，它最后的效果是 将time模块中的延时 全部替换为gevent中的延时
# time模块中的延时 是不具备 自动切换任务的功能， 而gevent中的延时具备。因为如果不使用这个语句时，我们需要将time全部改为gevent.


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(1)
        time.sleep(1)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()  # join会等待g1标识的那个任务执行完毕之后，对其进行清理工作，其实这就是一个耗时操作。
g2.join()
g3.join()


'''
1. 使用gevent来实现多任务的时候，有一个和特殊的地方
它可以自动切换协程指定的任务，而且切换的前提是：当一个任务用到耗时操作（例如延时）, 它就会把这个时间拿出来做另外的任务，
这样最终实现了多任务。而且自动切换。
'''

