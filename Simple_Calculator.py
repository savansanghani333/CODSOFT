#Task 2 Codsoft
# Python program to create a simple calculator

import tkinter as tk

def onClick(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def createButton(text, row, col, col_span=1):
    button = tk.Button(root, text=text, font=("Helvetica", 18), bd=5)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5)
    button.bind("<Button-1>", onClick)  # Bind the button click event to the onClick() function
    return button

root = tk.Tk()
root.title("Simple-Calculator")
root.geometry("300x400")


heading_label = tk.Label(root, text="Simple-Calculator", font=("Helvetica", 16, "bold"),highlightcolor=("red"))
heading_label.grid(row=0, column=0, columnspan=4, pady=20)

entry = tk.Entry(root, font=("Helvetica", 24), bd=5, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)


createButton("7", 2, 0)
createButton("8", 2, 1)
createButton("9", 2, 2)
createButton("/", 2, 3)

createButton("4", 3, 0)
createButton("5", 3, 1)
createButton("6", 3, 2)
createButton("*", 3, 3)

createButton("1", 4, 0)
createButton("2", 4, 1)
createButton("3", 4, 2)
createButton("-", 4, 3)

createButton("0", 5, 0)
createButton(".", 5, 1)
createButton("=", 5, 2)
createButton("+", 5, 3)

createButton("C", 6, 0, 3)

root.mainloop()
