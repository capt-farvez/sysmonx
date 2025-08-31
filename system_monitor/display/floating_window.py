""" Floating Window - Draggable always-on-top window showing system stats
"""

import tkinter as tk

class FloatingWindow(tk.Tk):
    def __init__(self, data_store):
        super().__init__()
        self.data_store = data_store
        
        # Window setup
        self.title("System Monitor")
        self.overrideredirect(True)          # No borders
        
        # Try to stay on top (works on most systems)
        try:
            self.attributes('-topmost', True)     # Always on top
        except tk.TclError:
            # Fallback for systems that don't support -topmost
            pass
            
        self.geometry("+100+100")

        # Main container
        frame = tk.Frame(self, bg='black')
        frame.pack(fill='both', expand=True)

        # Left column: CPU and RAM
        col1 = tk.Frame(frame, bg='black')
        col1.grid(row=0, column=0, sticky='nsew', padx=(5,2), pady=2)
        self.cpu_label = tk.Label(col1, text="CPU: --.--%", bg='black', fg='lime', font=("Consolas", 9), width=15)
        self.cpu_label.pack(fill='x')
        self.ram_label = tk.Label(col1, text="RAM: --.--%", bg='black', fg='lime', font=("Consolas", 9), width=15)
        self.ram_label.pack(fill='x')

        # Right column: Network speeds
        col2 = tk.Frame(frame, bg='black')
        col2.grid(row=0, column=1, sticky='nsew', padx=(2,5), pady=2)
        self.upload_label = tk.Label(col2, text="↑: --.-- KB/s", bg='black', fg='lime', font=("Consolas", 9), width=18)
        self.upload_label.pack(fill='x')
        self.download_label = tk.Label(col2, text="↓: --.-- KB/s", bg='black', fg='lime', font=("Consolas", 9), width=18)
        self.download_label.pack(fill='x')

        # Equal column widths
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        self.update_metrics()

        # Drag setup
        self._x = 0
        self._y = 0
        
        # Make all widgets draggable
        self.bind_drag_events(self)
        self.bind_drag_events(frame)
        self.bind_drag_events(col1)
        self.bind_drag_events(col2)
        self.bind_drag_events(self.cpu_label)
        self.bind_drag_events(self.ram_label)
        self.bind_drag_events(self.upload_label)
        self.bind_drag_events(self.download_label)

    def bind_drag_events(self, widget):
        widget.bind("<ButtonPress-1>", self.start_move)
        widget.bind("<ButtonRelease-1>", self.stop_move)
        widget.bind("<B1-Motion>", self.on_move)

    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def stop_move(self, event):
        self._x = None
        self._y = None

    def on_move(self, event):
        if self._x is not None and self._y is not None:
            deltax = event.x - self._x
            deltay = event.y - self._y
            x = self.winfo_x() + deltax
            y = self.winfo_y() + deltay
            self.geometry(f"{self.winfo_width()}x{self.winfo_height()}+{x}+{y}")

    def update_metrics(self):
        # Get current stats
        cpu = self.data_store.get('cpu_usage', 0.0)
        ram = self.data_store.get('ram_usage', 0.0)
        upload = self.data_store.get('upload_speed', 0.0)
        download = self.data_store.get('download_speed', 0.0)

        # Update labels
        self.cpu_label.config(text=f"CPU: {cpu:.1f}%")
        self.ram_label.config(text=f"RAM: {ram:.1f}%")
        self.upload_label.config(text=f"↑: {upload:.1f} KB/s")
        self.download_label.config(text=f"↓: {download:.1f} KB/s")

        # Update every second
        self.after(1000, self.update_metrics)

    def start_display(self):
        self.mainloop()

    def stop_display(self):
        self.quit()
        self.destroy()

