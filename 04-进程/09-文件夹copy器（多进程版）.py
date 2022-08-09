# -- coding: utf-8 --
# @Time : 2022/8/8 10:42
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 09-文件夹copy器（多进程版）.py
# @Software: PyCharm

import multiprocessing
import os
import time
import random


# 7. 定一个函数u，当做进程池中进程执行的代码
def copy_file(q, name, folder_name, dest_folder_name):

    time.sleep(random.randint(1, 5))

    # 7.1 使用open打开一个文件，用来读取内容
    with open(folder_name + "/" + name, "rb") as f:
        content = f.read()

    # 7.2 使用open新建一个文件，用来存储新的文件内容
    with open(dest_folder_name + "/" + name, "wb") as f:
        f.write(content)

    q.put(name)  # 将文件名放入队列


def main():
    # 1. 获取用户需要复制的文件夹
    folder_name = input("请输入要复制文件夹的名字：")

    # 8. 定义一个变量用来存储目标文件夹的名字
    dest_folder_name = folder_name + "[复件]"
    if not os.path.exists(dest_folder_name):
        os.mkdir(dest_folder_name)

    # 2. 通过listdir 获取指定的文件夹下的所有的文件名字
    file_names = os.listdir(folder_name)
    print(file_names)

    q = multiprocessing.Manager().Queue()  # 创建多进程队列

    # 3. 创建一个进程池
    pool = multiprocessing.Pool(3)

    # 4. 循环的方式向进程池中添加任务、复制文件
    for name in file_names:
        print(name)
        pool.apply_async(copy_file, (q, name, folder_name, dest_folder_name))

    print('==========')
    # 主进程从Queue中获取已经复制完成的文件名
    for i in range(len(file_names)):
        file_name = q.get()
        print("\r当前的进度是：%.2f 已经复制完成的文件名是：%s%s" % ((i + 1) / len(file_names) * 100, file_name, " " * 30), end=" ")

    print()
    # 5. 进程池关闭
    pool.close()

    # 6. 等待进程池中所有的进程结束
    pool.join()


if __name__ == '__main__':
    main()


