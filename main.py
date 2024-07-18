from tkinter import ttk
import ttkbootstrap
import json
import datetime
from datetime import timedelta

root = tk.Tk()
# root = ttkbootstrap.Window(themename="cyborg")
root.title("Nowadays")
root.state('zoomed')

def see_date():
	date = cal.entry.get()
    with open(f"calendar.json", "r") as f:
        file = json.load(f)
    result = file[date]
	date_label.config(text=result)


cal = ttkbootstrap.DateEntry(root, dateformat="%d/%m/%Y", bootstyle="info")
# cal.pack(padx=40, pady=40)
cal.grid(row=0, column=1)

btn = ttk.Button(root, text="Show Date", bootstyle="light-outline", command=see_date)
btn.pack(padx=40, pady=45)

date_label = ttk.Label(root, text="No date selected")
date_label.pack(padx=40, pady=50)

# Menu de funciones de la ventana
frame_menu = ttk.Frame(root, bootstyle="dark")
frame_menu.grid(row=1, column=0)

frame_main = ttk.Frame(root, bootstyle="dark")
frame_main.grid(row=1, column=1)

btn_add_event = ttk.Button(frame_menu, text="Agregar evento", command=add_event, style="info.TButton")
btn_add_event.pack(side=tk.LEFT, pady=10)

btn_del_event = ttk.Button(frame_menu, text="Eliminar evento", command=del_event, style="info.TButton")
btn_del_event.pack(side=tk.LEFT, pady=10)

btn_edit_event = ttk.Button(frame_menu, text="Editar evento", command=edit_event, style="info.TButton")
btn_edit_event.pack(side=tk.LEFT, pady=10)



def load_date():
    try:
        with open("calendar.json", "r") as f:
            calendar_file = json.load(f)
        for date, content in calendar_file.items():
            # Add the note to the notebook
            date_content = tk.Text(frame_main, width=40, height=10)
            date_content.insert(tk.END, content)
    except FileNotFoundError:
        pass





# root.title("Notes App")
# root.geometry("500x500")
# style = Style(theme='journal')
# style = ttk.Style()

# style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

# notebook = ttk.Notebook(root, style="TNotebook")

events = {}
notes = {}


def load_file(file):

	try:
	    with open(f"{file}.json", "r") as f:
	        file = json.load(f)
	except FileNotFoundError:
	    pass

# notebook = ttk.Notebook(root)
# notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

def add_note():
    note_frame = ttk.Frame(notebook, padding=10)
    notebook.add(note_frame, text="New Note")
    
    title_label = ttk.Label(note_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
    
    title_entry = ttk.Entry(note_frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)
    
    content_label = ttk.Label(note_frame, text="Content:")
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
    
    content_entry = tk.Text(note_frame, width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10, pady=10)
    
    def save_note():
        title = title_entry.get()
        content = content_entry.get("1.0", tk.END)
        
        notes[title] = content.strip()
        
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        
        note_content = tk.Text(notebook, width=40, height=10)
        note_content.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(note_content, text=title)
        
    save_button = ttk.Button(note_frame, text="Save", 
                             command=save_note, style="secondary.TButton")
    save_button.grid(row=2, column=1, padx=10, pady=10)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)

        for title, content in notes.items():
            # Add the note to the notebook
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title)

    except FileNotFoundError:
        pass

load_notes()

def delete_note():
    current_tab = notebook.index(notebook.select())
    
    note_title = notebook.tab(current_tab, "text")
    
    confirm = messagebox.askyesno("Delete Note", 
                                  f"Are you sure you want to delete {note_title}?")
    
    if confirm:
        notebook.forget(current_tab)
        
        notes.pop(note_title)
        
        with open("notes.json", "w") as f:
            json.dump(notes, f)

new_button = ttk.Button(root, text="New Note", 
                        command=add_note, style="info.TButton")
new_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete", 
                           command=delete_note, style="primary.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)




root.mainloop()
