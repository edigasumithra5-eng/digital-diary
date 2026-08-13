```python
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os


# --------------------------------
# Create diary folder
# --------------------------------

DIARY_FOLDER = "diary_entries"

if not os.path.exists(DIARY_FOLDER):
    os.makedirs(DIARY_FOLDER)


# --------------------------------
# Main Window
# --------------------------------

root = tk.Tk()

root.title("Digital Diary")
root.geometry("700x600")
root.resizable(False, False)


# --------------------------------
# Title
# --------------------------------

title_label = tk.Label(
    root,
    text="📔 DIGITAL DIARY",
    font=("Arial", 28, "bold")
)

title_label.pack(pady=20)


# --------------------------------
# Date Section
# --------------------------------

date_frame = tk.Frame(root)

date_frame.pack(pady=10)


date_label = tk.Label(
    date_frame,
    text="Date:",
    font=("Arial", 14, "bold")
)

date_label.grid(
    row=0,
    column=0,
    padx=10
)


date_entry = tk.Entry(
    date_frame,
    width=20,
    font=("Arial", 14)
)

date_entry.grid(
    row=0,
    column=1,
    padx=10
)


# Insert today's date

today = datetime.now().strftime("%d-%m-%Y")

date_entry.insert(
    0,
    today
)


# --------------------------------
# Diary Text
# --------------------------------

text_label = tk.Label(
    root,
    text="Write Your Diary Entry:",
    font=("Arial", 14, "bold")
)

text_label.pack(pady=10)


diary_text = tk.Text(
    root,
    width=70,
    height=18,
    font=("Arial", 12),
    wrap=tk.WORD
)

diary_text.pack(padx=20, pady=10)


# --------------------------------
# Get File Name
# --------------------------------

def get_file_name():

    date = date_entry.get().strip()

    if date == "":
        messagebox.showerror(
            "Error",
            "Please enter a date."
        )
        return None

    # Replace characters that are unsuitable for filenames
    safe_date = date.replace("/", "-")

    return os.path.join(
        DIARY_FOLDER,
        safe_date + ".txt"
    )


# --------------------------------
# Save Entry
# --------------------------------

def save_entry():

    file_name = get_file_name()

    if file_name is None:
        return

    entry = diary_text.get(
        "1.0",
        tk.END
    ).strip()

    if entry == "":
        messagebox.showwarning(
            "Empty Entry",
            "Please write something before saving."
        )
        return

    try:

        with open(
            file_name,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(entry)

        messagebox.showinfo(
            "Success",
            "Diary entry saved successfully!"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Could not save entry:\n{error}"
        )


# --------------------------------
# View Entry
# --------------------------------

def view_entry():

    file_name = get_file_name()

    if file_name is None:
        return

    if not os.path.exists(file_name):

        messagebox.showinfo(
            "No Entry",
            "No diary entry found for this date."
        )

        return

    try:

        with open(
            file_name,
            "r",
            encoding="utf-8"
        ) as file:

            entry = file.read()

        diary_text.delete(
            "1.0",
            tk.END
        )

        diary_text.insert(
            tk.END,
            entry
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Could not read entry:\n{error}"
        )


# --------------------------------
# Delete Entry
# --------------------------------

def delete_entry():

    file_name = get_file_name()

    if file_name is None:
        return

    if not os.path.exists(file_name):

        messagebox.showinfo(
            "No Entry",
            "No diary entry found for this date."
        )

        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this diary entry?"
    )

    if confirm:

        try:

            os.remove(file_name)

            diary_text.delete(
                "1.0",
                tk.END
            )

            messagebox.showinfo(
                "Deleted",
                "Diary entry deleted successfully!"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"Could not delete entry:\n{error}"
            )


# --------------------------------
# Clear Text
# --------------------------------

def clear_text():

    diary_text.delete(
        "1.0",
        tk.END
    )


# --------------------------------
# Buttons
# --------------------------------

button_frame = tk.Frame(root)

button_frame.pack(pady=15)


save_button = tk.Button(
    button_frame,
    text="Save Entry",
    width=14,
    font=("Arial", 11, "bold"),
    command=save_entry
)

save_button.grid(
    row=0,
    column=0,
    padx=5
)


view_button = tk.Button(
    button_frame,
    text="View Entry",
    width=14,
    font=("Arial", 11, "bold"),
    command=view_entry
)

view_button.grid(
    row=0,
    column=1,
    padx=5
)


delete_button = tk.Button(
    button_frame,
    text="Delete Entry",
    width=14,
    font=("Arial", 11, "bold"),
    command=delete_entry
)

delete_button.grid(
    row=0,
    column=2,
    padx=5
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=14,
    font=("Arial", 11, "bold"),
    command=clear_text
)

clear_button.grid(
    row=0,
    column=3,
    padx=5
)


# --------------------------------
# Footer
# --------------------------------

footer = tk.Label(
    root,
    text="Python Digital Diary | VS Code Project",
    font=("Arial", 10)
)

footer.pack(pady=10)


# --------------------------------
# Start Application
# --------------------------------

root.mainloop()
```
