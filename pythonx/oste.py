import time, threading

# 假定这是你的银行存款:
'''balance = 0
lock = threading.Lock()
#def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    lock.acquire()
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        print(n)
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)'''






import threading
import time

def run():

    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)

if __name__ == '__main__':

    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)
        t.setDaemon(True)
        t.start()

    print('主线程结束了！' , threading.current_thread().name)
    print('一共用时：', time.time()-start_time)