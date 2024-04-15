import tkinter as tk

class MyTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Tkinter Application")
        
        self.label = tk.Label(self.root, text="Welcome to my App!")
        self.label.pack(pady=10)
        
        self.button = tk.Button(self.root, text="Click Me!", command=self.button_click)
        self.button.pack(pady=5)
        
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=5)
        
    def button_click(self):
        user_input = self.entry.get()
        self.label.config(text=f"You clicked! Entered: {user_input}")

root = tk.Tk()

app = MyTkinterApp(root)

root.mainloop()
