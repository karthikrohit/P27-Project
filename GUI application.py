import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer App")

        self.timer_running = False
        self.timer_value = 0

        self.label = tk.Label(master, text="Timer: 0 seconds", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.timer_value = 0
        self.update_timer()

    def update_timer(self):
        if self.timer_running:
            self.timer_value += 1
            self.label.config(text=f"Timer: {self.timer_value} seconds")
            self.master.after(1000, self.update_timer)  # Update every 1000ms (1 second)
        else:
            self.label.config(text=f"Timer: {self.timer_value} seconds")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
