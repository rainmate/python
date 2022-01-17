import threading
import time

value = []
def print_thread_body():
    print('t1 sub thread start ...')
    for n in range(2):
        print('t1 sub thread excute ...')
        value.append(n)
        time.sleep(2)
    print('t1 sub thread end')

print('main thread end')
t1 = threading.Thread(target=print_thread_body())
t1.start()
t1.join()
print('value = {0}'.format(value) )
print('main thread go on')