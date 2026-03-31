import tkinter as tk
from tkinter import scrolledtext
from explanation_model import explain_error

def analyze_code():
    code = code_input.get("1.0", tk.END)

    try:
        exec(code)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "No errors found.")
    except Exception as e:
        explanation = explain_error(e, code)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, explanation)


# Window
root = tk.Tk()
root.title("Python Error Explanation Tool")
root.geometry("700x500")

# Code input label
tk.Label(root, text="Enter Python Code").pack()

# Code input box
code_input = scrolledtext.ScrolledText(root, height=10)
code_input.pack(fill="both", padx=10, pady=10)

# Run button
run_button = tk.Button(root, text="Analyze Code", command=analyze_code)
run_button.pack(pady=10)

# Output label
tk.Label(root, text="Explanation").pack()

# Output box
output_box = scrolledtext.ScrolledText(root, height=10)
output_box.pack(fill="both", padx=10, pady=10)

root.mainloop()