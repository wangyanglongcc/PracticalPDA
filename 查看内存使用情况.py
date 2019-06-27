import os
import psutil
from collections import OrderedDict

def show_memory_info(hint=None):
    memory_convent = 1024 * 1024 * 1024
    mem_info = psutil.virtual_memory()
    pid = os.getpid()
    p = psutil.Process(pid)
    mem_pid = p.memory_full_info().uss
    mem_used = mem_info.used
    mem_ava = mem_info.available
    mem_total = mem_info.total
    mem_info = OrderedDict()
    mem_info['mem_pid'] = '{:.4f}GB'.format(mem_pid/memory_convent)
    mem_info['mem_used'] = '{:.4f}GB'.format(mem_used/memory_convent)
    mem_info['mem_ava'] = '{:.4f}GB'.format(mem_ava/memory_convent)
    mem_info['mem_total'] = '{:.4f}GB'.format(mem_total/memory_convent)
    print('{} memory info: {}'.format(hint,mem_info))
    return mem_info

if __name__ == '__main__':
    show_memory_info('T')
