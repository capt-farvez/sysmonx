""" Network Monitor - Internet upload/download speed tracking
"""

import psutil

class NetworkMonitor:
    def __init__(self):
        # Store initial network stats to calculate speed differences
        net_stats = psutil.net_io_counters()
        self.last_sent = net_stats.bytes_sent
        self.last_recv = net_stats.bytes_recv
        self.upload_speed = 0
        self.download_speed = 0

    def get_network_usage(self):
        # Calculate current upload and download speeds in KB/s
        net_stats = psutil.net_io_counters()
        current_sent = net_stats.bytes_sent
        current_recv = net_stats.bytes_recv

        # Calculate speed based on bytes transferred since last check
        self.upload_speed = (current_sent - self.last_sent) / 1024
        self.download_speed = (current_recv - self.last_recv) / 1024

        # Update for next calculation
        self.last_sent = current_sent
        self.last_recv = current_recv

        return self.upload_speed, self.download_speed
