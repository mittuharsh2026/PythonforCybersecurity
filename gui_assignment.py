import tkinter as tk

window = tk.Tk()
window.title("My GUI App")
window.geometry("300x200")

label = tk.Label(window, text="Hello, welcome to my app!")
label.pack(pady=20)

button = tk.Button(window, text="Click Me")
button.pack()

window.mainloop() 
