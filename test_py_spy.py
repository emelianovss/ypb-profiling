import time
import os
from test_func_cpu_1 import func_1


while True:
    func_1(10)
    print(f'Sleep for {os.getpid()}')
    time.sleep(4)
