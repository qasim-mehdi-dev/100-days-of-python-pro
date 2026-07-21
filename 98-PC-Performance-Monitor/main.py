import tkinter as tk
from tkinter import ttk
import psutil


class HardwareMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hardware Performance Monitor")
        self.root.geometry("380x320")
        self.root.resizable(False, False)
        
        self.bg_color = "#1e1e2e"
        self.card_bg = "#2b2b3b"
        self.text_color = "#cdd6f4"
        self.accent_green = "#a6e3a1"
        self.accent_red = "#f38ba8"
        self.accent_blue = "#89b4fa"

        self.root.configure(bg=self.bg_color)

        title_label = tk.Label(
            root, 
            text="⚡ SYSTEM TELEMETRY", 
            font=("Consolas", 14, "bold"), 
            bg=self.bg_color, 
            fg=self.accent_blue
        )
        title_label.pack(pady=(15, 10))

        main_frame = tk.Frame(root, bg=self.bg_color, padx=15, pady=5)
        main_frame.pack(fill="both", expand=True)

        self.cpu_label = tk.Label(
            main_frame, 
            text="CPU Utilization: 0%", 
            font=("Consolas", 10, "bold"), 
            bg=self.bg_color, 
            fg=self.text_color, 
            anchor="w"
        )
        self.cpu_label.pack(fill="x")

        self.cpu_bar = ttk.Progressbar(main_frame, length=300, mode="determinate")
        self.cpu_bar.pack(fill="x", pady=(2, 12))

        self.ram_label = tk.Label(
            main_frame, 
            text="RAM Utilization: 0 GB / 0 GB (0%)", 
            font=("Consolas", 10, "bold"), 
            bg=self.bg_color, 
            fg=self.text_color, 
            anchor="w"
        )
        self.ram_label.pack(fill="x")

        self.ram_bar = ttk.Progressbar(main_frame, length=300, mode="determinate")
        self.ram_bar.pack(fill="x", pady=(2, 12))

        self.disk_label = tk.Label(
            main_frame, 
            text="Disk Space: 0 GB / 0 GB (0%)", 
            font=("Consolas", 10, "bold"), 
            bg=self.bg_color, 
            fg=self.text_color, 
            anchor="w"
        )
        self.disk_label.pack(fill="x")

        self.disk_bar = ttk.Progressbar(main_frame, length=300, mode="determinate")
        self.disk_bar.pack(fill="x", pady=(2, 12))

        cores_logical = psutil.cpu_count(logical=True)
        cores_physical = psutil.cpu_count(logical=False)
        self.info_label = tk.Label(
            main_frame, 
            text=f"Cores: {cores_physical} Physical | {cores_logical} Threads", 
            font=("Consolas", 9, "italic"), 
            bg=self.bg_color, 
            fg="#a6adc8"
        )
        self.info_label.pack(pady=(10, 0))

        self.update_metrics()

    def update_metrics(self):
        cpu_usage = psutil.cpu_percent(interval=None)
        self.cpu_bar['value'] = cpu_usage
        self.cpu_label.config(
            text=f"CPU Utilization: {cpu_usage:.1f}%",
            fg=self.accent_red if cpu_usage > 85 else self.text_color
        )

        ram = psutil.virtual_memory()
        ram_used_gb = ram.used / (1024 ** 3)
        ram_total_gb = ram.total / (1024 ** 3)
        self.ram_bar['value'] = ram.percent
        self.ram_label.config(
            text=f"RAM: {ram_used_gb:.1f} GB / {ram_total_gb:.1f} GB ({ram.percent:.1f}%)",
            fg=self.accent_red if ram.percent > 85 else self.text_color
        )

        disk = psutil.disk_usage('/')
        disk_used_gb = disk.used / (1024 ** 3)
        disk_total_gb = disk.total / (1024 ** 3)
        self.disk_bar['value'] = disk.percent
        self.disk_label.config(
            text=f"Disk: {disk_used_gb:.1f} GB / {disk_total_gb:.1f} GB ({disk.percent:.1f}%)"
        )

        self.root.after(1000, self.update_metrics)


if __name__ == "__main__":
    root = tk.Tk()
    app = HardwareMonitorApp(root)
    root.mainloop()