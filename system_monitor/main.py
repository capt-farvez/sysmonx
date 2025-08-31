import os
import sys

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.background_service import BackgroundService
from display.floating_window import FloatingWindow

# Shared data between background service and display
SHARED_DATA = {
    'upload_speed': 0.0,
    'download_speed': 0.0,
    'cpu_usage': 0.0,
    'ram_usage': 0.0
}

def main():
    # Start background monitoring service
    background_service = BackgroundService(SHARED_DATA)
    background_service.daemon = True
    background_service.start()

    # Create and show floating window
    floating_window = FloatingWindow(SHARED_DATA)
    floating_window.start_display()

if __name__ == "__main__":
    main()
