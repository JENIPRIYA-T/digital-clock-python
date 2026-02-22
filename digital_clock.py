from tkinter import *
from tkinter.ttk import *
from datetime import datetime
import pytz

root = Tk()
root.title("Digital Clock-IST using Python by Jeni Priya T")

def time():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%I:%M:%S %p')  # 12-hour format
    label.config(text=current_time)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

time()
mainloop()
