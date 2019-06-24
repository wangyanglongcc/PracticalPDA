import os
import psutil
def show_memory_info(hint=None):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss/1024/1024/1024
    # print('{} memory used: {:.4f}GB'.format(hint,memory))
    return memory
