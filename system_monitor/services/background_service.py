""" Background Service - Continuously monitors system performance in a separate thread
"""

import threading
import time
from monitors.network_monitor import NetworkMonitor
from monitors.system_monitor import SystemMonitor

class BackgroundService(threading.Thread):
    def __init__(self, data_store):
        super().__init__()
        self.data_store = data_store
        self.running = True
        
        # Initialize monitors
        self.network_monitor = NetworkMonitor()
        self.system_monitor = SystemMonitor()

    def run(self):
        # Main monitoring loop - updates stats every second
        while self.running:
            # Get network speeds
            upload, download = self.network_monitor.get_network_usage()
            self.data_store['upload_speed'] = upload
            self.data_store['download_speed'] = download

            # Get system usage
            cpu_usage = self.system_monitor.get_cpu_usage()
            ram_usage = self.system_monitor.get_ram_usage()
            self.data_store['cpu_usage'] = cpu_usage
            self.data_store['ram_usage'] = ram_usage

            time.sleep(1)

    def stop(self):
        self.running = False
