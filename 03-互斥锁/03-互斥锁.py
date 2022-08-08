# -- coding: utf-8 --
# @Time : 2022/7/29 17:33
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 03-互斥锁.py
# @Software: PyCharm

import threading

# 创建一个互斥锁
metex = threading.Lock()

# 上锁
metex.acquire()

#  如果想要对某些代码一起执行，不想被其它的线程打扰，可以将这些代码放到互斥锁上锁 到 互斥锁解锁之间 。

print("嘿嘿嘿")

#  如果这个互斥锁已经被上锁了，那么在这个锁被解开之前，是不能再次上锁的，也就是说，如果这个锁被上锁了，在解开之前，谁要是再次
#  调用acquire对其上锁，那么谁就被堵塞，直到这个互斥锁被解锁为止。注意：一定是同一把锁。


# metex.acquire()

# 解锁
metex.release()


