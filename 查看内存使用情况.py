import os
import psutil
from collections import OrderedDict

def show_memory_info(hint=None):
    memory_convent = 1024 * 1024 * 1024
    mem_info = psutil.virtual_memory()
    pid = os.getpid()
    p = psutil.Process(pid)
    mem_info = OrderedDict()
    mem_info['mem_pid'] = '{:.4f}GB'.format(p.memory_full_info().uss/memory_convent)
    mem_info['mem_used'] = '{:.4f}GB'.format(mem_info.used/memory_convent)
    mem_info['mem_ava'] = '{:.4f}GB'.format(mem_info.available/memory_convent)
    mem_info['mem_total'] = '{:.4f}GB'.format(mem_info.total/memory_convent)
    print('{} memory info: {}'.format(hint,mem_info))
    return mem_info

if __name__ == '__main__':
    show_memory_info('T')
