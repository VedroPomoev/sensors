# -*- coding: utf-8 -*-

from collections import namedtuple
import psutil


cpu_count = psutil.cpu_count()
probe_struct = namedtuple('cpu', ['total'] + ['cpu_{}'.format(cpu_num) for cpu_num in range(cpu_count)])

def cpu_utilization():
    per_cpu_utilization_snapshot = psutil.cpu_percent(interval=1, percpu=True)
    cpu_utilization_snapshot = probe_struct._make([sum(per_cpu_utilization_snapshot)] + per_cpu_utilization_snapshot)
    return cpu_utilization_snapshot


def memory_percentage():
    used_memory = psutil.virtual_memory().percent
    return used_memory


def swap_percentage():
    used_swap = psutil.swap_memory().percent
    return used_swap


def zombie_processes_count():
    zombies_count = 0
    for p in psutil.process_iter():
        if p.status() == psutil.STATUS_ZOMBIE:
            zombies_count += 1
    return zombies_count
