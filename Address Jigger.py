import random
import tkinter as tk
from tkinter import messagebox

def add_symbols(name):
    symbols = ', . / ; : \' " [ ] { }'.split()
    new_name = ''
    for i, letter in enumerate(name):
        if letter.isdigit():
            new_name += letter
        else:
            new_name += letter
            if i % 2 == 1:
                new_name += random.choice(symbols)
    return new_name

def generate_names():
    name = name_entry.get()
    num_outputs_str = num_outputs_entry.get()
    if not name:
        messagebox.showwarning('Missing input', 'Please enter an address')
        return
    try:
        num_outputs = int(num_outputs_str)
        if num_outputs <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning('Invalid input', 'Please enter a positive integer')
        return
    generated_names = []
    while len(generated_names) < num_outputs:
        new_name = add_symbols(name)
        if new_name not in generated_names:
            generated_names.append(new_name)
    for name in generated_names:
        names_output.insert(tk.END, name)



def reset_fields():
    name_entry.delete(0, tk.END)
    num_outputs_entry.delete(0, tk.END)
    names_output.delete(0, tk.END)

def check_duplicates():
    names = names_output.get(0, tk.END)
    unique_names = set(names)
    if len(names) == len(unique_names):
        tk.messagebox.showinfo('No duplicates found', 'All names are unique!')
    else:
        duplicates = []
        for name in unique_names:
            if names.count(name) > 1:
                duplicates.append(name)
        tk.messagebox.showwarning('Duplicates found', 'The following names are duplicated:\n' + '\n'.join(duplicates))

def copy_output():
    output = names_output.get(0, tk.END)
    root.clipboard_clear()
    root.clipboard_append('\n'.join(output))

# Create the GUI
root = tk.Tk()
root.title('Address Jigger')
root.resizable(True, True)
root.geometry("300x450+250+250")

# Add input fields and labels
name_label = tk.Label(root, text='Enter Address:')
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

num_outputs_label = tk.Label(root, text='Enter the amount of outputs:')
num_outputs_label.pack()
num_outputs_entry = tk.Entry(root)
num_outputs_entry.pack()

# Add button to generate names
generate_button = tk.Button(root, text='Generate', command=generate_names, width=15)
generate_button.pack()

# Add check duplicates button
check_duplicates_button = tk.Button(root, text='Check Duplicates', command=check_duplicates, width=15)
check_duplicates_button.pack()

# Add output listbox
names_output = tk.Listbox(root, height=17, width=20)
names_output.pack()

# Add copy output button with universal copy emoji
copy_button = tk.Button(root, text='\U0001F4CB', command=copy_output, font=('Arial Unicode MS', 18))
copy_button.pack(side=tk.RIGHT, anchor=tk.SE)

# Add reset button
reset_button = tk.Button(root, text='\U0001F501', command=reset_fields, font=('Arial Unicode MS', 18))
reset_button.pack(side=tk.LEFT, anchor=tk.SW)

root.mainloop()
