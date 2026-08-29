import tkinter as tk
from tkinter import messagebox
import pyperclip

from generator import (
    build_character_sets,
    generate_password,
    calculate_strength
)


# Stores the last 5 generated passwords
password_history = []


def copy_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    pyperclip.copy(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )


def update_history(password):
    password_history.insert(0, password)

    # Keep only the latest 5 passwords
    if len(password_history) > 5:
        password_history.pop()

    history_list.delete(0, tk.END)

    for item in password_history:
        history_list.insert(tk.END, item)


def update_strength_display(strength):
    if strength == "Weak":
        strength_bar.config(
            text="████",
            fg="red"
        )
        strength_label.config(
            text="Strength: Weak",
            fg="red"
        )

    elif strength == "Medium":
        strength_bar.config(
            text="████████",
            fg="orange"
        )
        strength_label.config(
            text="Strength: Medium",
            fg="orange"
        )

    else:
        strength_bar.config(
            text="████████████",
            fg="green"
        )
        strength_label.config(
            text="Strength: Strong",
            fg="green"
        )


def generate():
    # Get password length
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Length",
            "Please enter a valid number for password length."
        )
        return

    # Minimum length
    if length < 4:
        messagebox.showerror(
            "Invalid Length",
            "Password length must be at least 4."
        )
        return

    # Build character sets
    character_sets = build_character_sets(
        uppercase_var.get(),
        lowercase_var.get(),
        numbers_var.get(),
        symbols_var.get(),
        ambiguous_var.get()
    )

    # At least two character types
    if len(character_sets) < 2:
        messagebox.showerror(
            "Character Selection",
            "Please select at least two character types."
        )
        return

    # Length must support all selected character types
    if length < len(character_sets):
        messagebox.showerror(
            "Invalid Length",
            "Password length is too short for the selected character types."
        )
        return

    # Generate password
    password = generate_password(
        length,
        character_sets
    )

    # Calculate strength
    strength = calculate_strength(password)

    # Display password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # Display strength
    update_strength_display(strength)

    # Update history
    update_history(password)


# ==================================================
# MAIN WINDOW
# ==================================================

root = tk.Tk()

root.title("Advanced Random Password Generator")
root.geometry("600x700")
root.resizable(False, False)


# ==================================================
# TITLE
# ==================================================

title_label = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=(25, 5))


subtitle_label = tk.Label(
    root,
    text="Generate secure and customizable passwords",
    font=("Arial", 10)
)

subtitle_label.pack(
    pady=(0, 20)
)


# ==================================================
# PASSWORD SETTINGS FRAME
# ==================================================

settings_frame = tk.LabelFrame(
    root,
    text="Password Settings",
    padx=20,
    pady=15
)

settings_frame.pack(
    padx=40,
    fill="x"
)


# Password length

length_frame = tk.Frame(settings_frame)

length_frame.pack(
    fill="x",
    pady=5
)


length_label = tk.Label(
    length_frame,
    text="Password Length:",
    font=("Arial", 11)
)

length_label.pack(
    side=tk.LEFT
)


length_entry = tk.Entry(
    length_frame,
    width=10,
    justify="center"
)

length_entry.insert(0, "12")

length_entry.pack(
    side=tk.RIGHT
)


# ==================================================
# CHARACTER OPTIONS
# ==================================================

options_label = tk.Label(
    settings_frame,
    text="Character Types",
    font=("Arial", 11, "bold")
)

options_label.pack(
    anchor="w",
    pady=(15, 5)
)


uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
ambiguous_var = tk.BooleanVar(value=False)


# First row

options_row1 = tk.Frame(settings_frame)

options_row1.pack(
    fill="x"
)


tk.Checkbutton(
    options_row1,
    text="Uppercase (A-Z)",
    variable=uppercase_var
).pack(
    side=tk.LEFT,
    expand=True,
    anchor="w"
)


tk.Checkbutton(
    options_row1,
    text="Lowercase (a-z)",
    variable=lowercase_var
).pack(
    side=tk.LEFT,
    expand=True,
    anchor="w"
)


# Second row

options_row2 = tk.Frame(settings_frame)

options_row2.pack(
    fill="x"
)


tk.Checkbutton(
    options_row2,
    text="Numbers (0-9)",
    variable=numbers_var
).pack(
    side=tk.LEFT,
    expand=True,
    anchor="w"
)


tk.Checkbutton(
    options_row2,
    text="Symbols",
    variable=symbols_var
).pack(
    side=tk.LEFT,
    expand=True,
    anchor="w"
)


# Ambiguous characters

tk.Checkbutton(
    settings_frame,
    text="Exclude ambiguous characters (0, O, l, 1)",
    variable=ambiguous_var
).pack(
    anchor="w",
    pady=(5, 0)
)


# ==================================================
# GENERATE BUTTON
# ==================================================

generate_button = tk.Button(
    root,
    text="GENERATE PASSWORD",
    command=generate,
    width=30,
    height=2,
    font=("Arial", 11, "bold")
)

generate_button.pack(
    pady=25
)


# ==================================================
# PASSWORD OUTPUT
# ==================================================

output_frame = tk.LabelFrame(
    root,
    text="Generated Password",
    padx=15,
    pady=15
)

output_frame.pack(
    padx=40,
    fill="x"
)


password_entry = tk.Entry(
    output_frame,
    width=50,
    justify="center",
    font=("Arial", 12)
)

password_entry.pack(
    pady=5
)


# ==================================================
# STRENGTH
# ==================================================

strength_label = tk.Label(
    output_frame,
    text="Strength: -",
    font=("Arial", 11, "bold")
)

strength_label.pack(
    pady=(10, 2)
)


strength_bar = tk.Label(
    output_frame,
    text="",
    font=("Arial", 12, "bold")
)

strength_bar.pack()


# ==================================================
# COPY BUTTON
# ==================================================

copy_button = tk.Button(
    root,
    text="COPY PASSWORD",
    command=copy_password,
    width=25
)

copy_button.pack(
    pady=15
)


# ==================================================
# HISTORY
# ==================================================

history_frame = tk.LabelFrame(
    root,
    text="Recent Passwords (Last 5)",
    padx=15,
    pady=10
)

history_frame.pack(
    padx=40,
    fill="x"
)


history_list = tk.Listbox(
    history_frame,
    width=55,
    height=5,
    font=("Consolas", 10)
)

history_list.pack()


# ==================================================
# START APPLICATION
# ==================================================

root.mainloop()