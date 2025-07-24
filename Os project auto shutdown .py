
import tkinter as tk
from tkinter import messagebox
import os
import time
import platform

def shutdown_timer():
    try:
        seconds = int(entry_timer.get())
        if platform.system() == "Windows":
            os.system(f"shutdown /s /t {seconds}")
        else:
            os.system(f"shutdown -h +{seconds // 60}")
        messagebox.showinfo("Scheduled", f"Shutdown in {seconds} seconds.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def shutdown_exact():
    try:
        hour = int(entry_hour.get())
        minute = int(entry_minute.get())
        now = time.localtime()
        shutdown_time = time.mktime((now.tm_year, now.tm_mon, now.tm_mday,
                                     hour, minute, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
        delay = int(shutdown_time - time.mktime(now))
        if delay > 0:
            if platform.system() == "Windows":
                os.system(f"shutdown /s /t {delay}")

            else:
                os.system(f"shutdown -h +{delay // 60}")
            messagebox.showinfo("Scheduled", f"Shutdown scheduled at {hour:02}:{minute:02}.")
        else:
            messagebox.showerror("Error", "Time must be in the future.")
    except ValueError:
        messagebox.showerror("Error", "Enter valid time.")

def cancel_shutdown():
    if platform.system() == "Windows":
        os.system("shutdown /a")
    else:
        os.system("shutdown -c")
    messagebox.showinfo("Canceled", "Shutdown canceled.")

app = tk.Tk()
app.title("Auto Shutdown Scheduler")
app.geometry("350x300")
app.configure(bg="#2c3e50")

title_label = tk.Label(app, text="Auto Shutdown Scheduler", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=15)

frame_timer = tk.Frame(app, bg="#2c3e50")
frame_timer.pack(pady=10)
tk.Label(frame_timer, text="Shutdown in (seconds):", bg="#2c3e50", fg="#ecf0f1").pack()
entry_timer = tk.Entry(frame_timer, width=20)
entry_timer.pack(pady=5)
tk.Button(frame_timer, text="Schedule Timer", command=shutdown_timer, bg="#27ae60", fg="white", width=20).pack()

frame_exact = tk.Frame(app, bg="#2c3e50")
frame_exact.pack(pady=15)
tk.Label(frame_exact, text="Or Shutdown at (HH:MM):", bg="#2c3e50", fg="#ecf0f1").pack()
time_input = tk.Frame(frame_exact, bg="#2c3e50")
time_input.pack()
entry_hour = tk.Entry(time_input, width=5)
entry_hour.pack(side="left")
tk.Label(time_input, text=":", bg="#2c3e50", fg="#ecf0f1").pack(side="left")
entry_minute = tk.Entry(time_input, width=5)
entry_minute.pack(side="left")
tk.Button(frame_exact, text="Schedule Exact Time", command=shutdown_exact, bg="#2980b9", fg="white", width=20).pack(pady=5)

tk.Button(app, text="Cancel Shutdown", command=cancel_shutdown, bg="#c0392b", fg="white", width=20).pack(pady=10)

app.mainloop()
