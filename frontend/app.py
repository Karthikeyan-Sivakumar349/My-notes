import tkinter as tk
import requests

#C:\My Folder\PROJECTS\FILEMANAGER\frontend
#C:\My Folder\PROJECTS\FILEMANAGER\backend

BASE_URL = "http://127.0.0.1:8000"

current_note_id = None

#------------------ delete function ----------- #

def delete_note():

    global current_note_id

    if current_note_id is None:
        return

    response = requests.delete(f"{BASE_URL}/files/{current_note_id}")

    if response.status_code == 200:

        current_note_id = None

        note_name_entry.delete(0, tk.END)

        text_editor.delete("1.0", tk.END)

        load_notes()

        print("Note Deleted Successfully")

    else:

        print(response.text)
#---------------------------------------------
#------------------ create function ----------- #
def create_note():

    global current_note_id

    current_note_id = None

    note_name_entry.delete(0, tk.END)

    text_editor.delete("1.0", tk.END)

    note_name_entry.focus()
#------------------------------------------------ #

# -----------------Save function---------- #

def save_note():

    global current_note_id

    file_name = note_name_entry.get()

    content = text_editor.get("1.0", tk.END).strip()

    data = {
        "file_name": file_name,
        "content": content
    }

    if current_note_id is None:

        response = requests.post(
            f"{BASE_URL}/files",
            json=data
        )

    else:

        response = requests.put(
            f"{BASE_URL}/files/{current_note_id}",
            json=data
        )

    if response.status_code == 200:

        print("Saved Successfully")

        load_notes()

    else:

        print(response.text)

#--------------------- load all files function ----------------- #
def load_notes():

    response = requests.get(f"{BASE_URL}/files")

    if response.status_code == 200:

        notes = response.json()

        for widget in notes_frame.winfo_children():

            if widget != notes_label:
                widget.destroy()

        notes_label.pack(pady=10)

        for note in notes:

            btn = tk.Button(
    notes_frame,
    text=f"📄 {note['file_name']}",
    anchor="w",
    command=lambda note_id=note["id"]: open_note(note_id)
)

            btn.pack(fill="x", padx=10, pady=2)
#------------------------------------------------- #
#-------------------------- OPEN FILE CONTENT FUNCTION ----------------
def open_note(file_id):

    global current_note_id

    response = requests.get(f"{BASE_URL}/files/{file_id}")

    if response.status_code == 200:

        note = response.json()

        current_note_id = note["id"]

        note_name_entry.delete(0, tk.END)
        note_name_entry.insert(0, note["file_name"])

        text_editor.delete("1.0", tk.END)
        text_editor.insert("1.0", note["content"])

#------------------------------------------------- #
# ---------------- Window ---------------- #

root = tk.Tk()
root.title("My Notes")
root.state("zoomed")

# ---------------- Root Layout ---------------- #

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# ---------------- Title ---------------- #

title_frame = tk.Frame(root, bd=2, relief="solid")
title_frame.grid(row=0, column=0, sticky="ew")

title = tk.Label(
    title_frame,
    text="MY NOTES",
    font=("Arial", 22, "bold")
)
title.pack(pady=10)

# ---------------- Body ---------------- #

body_frame = tk.Frame(root)
body_frame.grid(row=1, column=0, sticky="nsew")

body_frame.grid_rowconfigure(0, weight=1)
body_frame.grid_columnconfigure(0, weight=1)
body_frame.grid_columnconfigure(1, weight=3)

# =====================================================
# LEFT PANEL
# =====================================================

left_frame = tk.Frame(body_frame, bd=2, relief="solid", bg="#ECECEC")
left_frame.grid(row=0, column=0, sticky="nsew")

left_frame.grid_rowconfigure(1, weight=1)
left_frame.grid_columnconfigure(0, weight=1)

# ---------- Top Buttons ---------- #

button_frame = tk.Frame(left_frame, bg="#ECECEC")
button_frame.grid(row=0, column=0, sticky="ew", pady=20)

create_btn = tk.Button(
    button_frame,
    text="Create Note",
    command=create_note
)
create_btn.pack(fill="x", padx=20, pady=5)



delete_btn = tk.Button(
    button_frame,
    text="Delete Note",
    command=delete_note
)
delete_btn.pack(fill="x", padx=20, pady=5)

# ---------- Notes List ---------- #

notes_frame = tk.Frame(left_frame, bd=1, relief="sunken")
notes_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=10)

notes_label = tk.Label(notes_frame, text="Notes", font=("Arial", 12, "bold"))
notes_label.pack(pady=10)

# Dummy notes (later these will come from SQLite)



# =====================================================
# RIGHT PANEL
# =====================================================

right_frame = tk.Frame(body_frame, bd=2, relief="solid")
right_frame.grid(row=0, column=1, sticky="nsew")

right_frame.grid_rowconfigure(1, weight=1)
right_frame.grid_columnconfigure(0, weight=1)

# ---------- Toolbar ---------- #


toolbar = tk.Frame(right_frame, bd=2, relief="ridge")
toolbar.grid(row=0, column=0, sticky="ew")

note_name_label = tk.Label(
    toolbar,
    text="Note Name:",
    font=("Arial", 11, "bold")
)
note_name_label.pack(side="left", padx=(10, 5), pady=8)

note_name_entry = tk.Entry(
    toolbar,
    font=("Arial", 11),
    width=30
)
note_name_entry.pack(side="left", padx=5)

save_btn = tk.Button(
    toolbar,
    text="💾 Save",
    command=save_note
)
save_btn.pack(side="right", padx=15, pady=8)
# ---------- Text Editor ---------- #

text_editor = tk.Text(
    right_frame,
    font=("Consolas", 12),
    wrap="word"
)

text_editor.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10
)
load_notes()
root.mainloop()