""" System Monitor - CPU and RAM usage tracking
"""

import psutil

class SystemMonitor:
    def __init__(self):
        pass

    def get_cpu_usage(self):
        # Returns CPU usage percentage (takes 1 second to measure)
        return psutil.cpu_percent(interval=1)

    def get_ram_usage(self):
        # Returns RAM usage percentage
        return psutil.virtual_memory().percent
