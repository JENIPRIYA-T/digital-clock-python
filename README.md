# Digital Clock (Python Tkinter)

A simple Digital Clock developed using Python and Tkinter.  
This project displays the current time in **Indian Standard Time (IST)** with a sleek digital interface.

## 🚀 Features
- Interactive Tkinter GUI
- 12-hour format with AM/PM
- Real-time time updates every second
- Stylish digital display with customizable colors

## 🛠️ Technologies Used
- Python
- Tkinter (GUI library)
- Pytz module (for timezone handling)
- Datetime module

## ▶️ How to Run
1. Make sure Python is installed
2. Install the `pytz` library (if not installed):

    ```bash
    pip install pytz
    ```

3. Run the Python file:

    ```bash
    python digital_clock.py
    ```

4. The clock window will open and start showing the current IST time

## 🎨 Customization
- Change font, size, and colors in the code:

    ```python
    label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
    ```

- Change the timezone:

    ```python
    ist = pytz.timezone('Asia/Kolkata')  # Change to your preferred timezone
    ```

## 👩‍💻 Author
Jeni Priya T