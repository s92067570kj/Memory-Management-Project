import tkinter as tk
from tkinter import messagebox
from memory_manager import FirstFitMemoryManager


class MemoryManagementApp:
    def __init__(self, root):
        self.manager = FirstFitMemoryManager([100, 500, 200, 300, 600])

        # Window setup
        root.title("Dynamic Memory Allocation (Enhanced UI)")
        root.geometry("600x500")
        root.config(bg="#f0f0f0")

        # Title label
        tk.Label(root, text="Dynamic Memory Allocation (First Fit)", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

        # Input section
        input_frame = tk.Frame(root, bg="#d9edf7", bd=2, relief="solid")
        input_frame.pack(pady=10, fill="x", padx=10)

        tk.Label(input_frame, text="Process ID:", font=("Arial", 12), bg="#d9edf7").grid(row=0, column=0, padx=10, pady=10)
        self.process_id_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.process_id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(input_frame, text="Memory Size:", font=("Arial", 12), bg="#d9edf7").grid(row=1, column=0, padx=10, pady=10)
        self.memory_size_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.memory_size_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button section
        button_frame = tk.Frame(root, bg="#dff0d8", bd=2, relief="solid")
        button_frame.pack(pady=10, fill="x", padx=10)

        tk.Button(button_frame, text="Allocate Memory", command=self.allocate_memory, bg="#5cb85c", fg="white", font=("Arial", 12)).pack(side="left", padx=20, pady=10)
        tk.Button(button_frame, text="Deallocate Memory", command=self.deallocate_memory, bg="#f0ad4e", fg="white", font=("Arial", 12)).pack(side="left", padx=20, pady=10)
        tk.Button(button_frame, text="Display Memory Status", command=self.display_memory_status, bg="#0275d8", fg="white", font=("Arial", 12)).pack(side="left", padx=20, pady=10)

        # Memory status display
        status_frame = tk.Frame(root, bg="#f2f2f2", bd=2, relief="solid")
        status_frame.pack(pady=10, fill="both", padx=10, expand=True)

        tk.Label(status_frame, text="Memory Status", font=("Arial", 14, "bold"), bg="#f2f2f2", fg="#333").pack(pady=5)
        self.memory_status = tk.Text(status_frame, height=10, width=60, font=("Courier", 12), bg="#fff", fg="#333")
        self.memory_status.pack(pady=5)

        # Initial memory display
        self.update_memory_status()

    def allocate_memory(self):
        try:
            process_id = int(self.process_id_entry.get())
            memory_size = int(self.memory_size_entry.get())
            if memory_size <= 0:
                messagebox.showerror("Invalid Input", "Memory size must be a positive integer.")
                return
            result = self.manager.allocate(process_id, memory_size)
            messagebox.showinfo("Allocation Result", result)
            self.update_memory_status()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

    def deallocate_memory(self):
        try:
            process_id = int(self.process_id_entry.get())
            result = self.manager.deallocate(process_id)
            messagebox.showinfo("Deallocation Result", result)
            self.update_memory_status()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric Process ID.")

    def display_memory_status(self):
        self.update_memory_status()

    def update_memory_status(self):
        self.memory_status.delete(1.0, tk.END)
        memory_layout = self.manager.display()
        for block in memory_layout:
            self.memory_status.insert(tk.END, block + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryManagementApp(root)
    root.mainloop()
