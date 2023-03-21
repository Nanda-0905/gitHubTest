import tkinter as tk

def save_name():
    name = name_entry.get()
    with open("name.txt", "w") as f:
        f.write(name)
    name_entry.delete(0, tk.END)

root = tk.Tk()

root.title("My Window")
root.geometry("400x300")

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

save_button = tk.Button(root, text="Save Name", command=save_name)
save_button.pack()

root.mainloop()
