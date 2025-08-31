# SysMonX - Cross-Platform System Monitor

A lightweight floating window that displays real-time system metrics on your desktop.
Shows CPU usage, RAM usage, and network upload/download speeds in a compact, always-on-top window.

**Works on Windows, Linux, and macOS.**

## Features

- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Floating Window**: Small, draggable window that stays on top of other applications
- **Real-time Monitoring**: Updates every second with fresh system data
- **Two-column Layout**: System stats (CPU, RAM) | Network stats (Upload, Download)
- **Lightweight**: Minimal resource usage, clean interface
- **Single Dependency**: Only requires `psutil` library

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/capt-farvez/sysmonx.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd system_monitor
   ```

3. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**
    - **Windows:**
       ```bash
       .\venv\Scripts\activate
       ```
    - **Linux/macOS:**
       ```bash
       source venv/bin/activate
       ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the application:**
   ```bash
   python main.py
   ```
## Usage

1. **Navigate to the application directory:**
   ```bash
   cd system_monitor
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

The application will display a small floating window showing:
- **CPU**: Current processor usage percentage
- **RAM**: Current memory usage percentage  
- **↑**: Network upload speed in KB/s
- **↓**: Network download speed in KB/s

## Controls

- **Drag**: Click and drag anywhere on the window to move it around the screen
- **Close**: Close the terminal window to exit the application

## Requirements

- Python 3.6 or higher
- `psutil` library
- **Windows**: Works out of the box
- **Linux**: Requires `python3-tk` (usually pre-installed)
- **macOS**: Works with standard Python installation

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** and test them
4. **Commit your changes**: `git commit -m "Add some feature"`
5. **Push to the branch**: `git push origin feature-name`
6. **Open a Pull Request**

### Ideas for Contributions:
- Add more system metrics (disk usage, temperature, etc.)
- Improve cross-platform compatibility
- Add configuration options
- Create themes/color schemes
- Add keyboard shortcuts
- Improve performance
- Write tests

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License - see the [LICENSE](LICENSE) file for details.

This means you can:
- ✅ Use it for personal projects
- ✅ Use it for educational purposes
- ✅ Use it for non-profit organizations
- ✅ Modify and adapt the code
- ✅ Share and redistribute it
- ✅ Contribute to the project
- ❌ **Cannot sell or use commercially**
- ❌ **Cannot monetize the software**

**For commercial use, please contact the author for permission.**

## Author

**capt-farvez** - [GitHub Profile](https://github.com/capt-farvez)