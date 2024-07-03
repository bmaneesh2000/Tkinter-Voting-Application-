import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time  
import winsound  

# File to store the votes
votes_file = 'votes.txt'

# Function to load votes from file
def load_votes():
    if os.path.exists(votes_file):
        with open(votes_file, 'r') as file:
            lines = file.readlines()
            if len(lines) == 4:
                return {
                    'cone': int(lines[0].strip()),
                    'ctwo': int(lines[1].strip()),
                    'cthree': int(lines[2].strip()),
                    'cfour': int(lines[3].strip())
                }
    return {'cone': 0, 'ctwo': 0, 'cthree': 0, 'cfour': 0}

# Function to save votes to file
def save_votes(votes):
    with open(votes_file, 'w') as file:
        file.write(f"{votes['cone']}\n")
        file.write(f"{votes['ctwo']}\n")
        file.write(f"{votes['cthree']}\n")
        file.write(f"{votes['cfour']}\n")

# Function to play a beep sound
def beep_sound():
    frequency = 2500 
    duration = 1000
    winsound.Beep(frequency, duration)

# Function to restart the application
def restart_app():
    for widget in root.winfo_children():
        widget.destroy()
    initialize_app()

# Load initial votes
votes = load_votes()

def initialize_app():
    global sp_submitted, asp_submitted, selected_sp_image, selected_asp_image, sp_labels, asp_labels, sp_submit_button, asp_submit_button

    sp_submitted = False
    asp_submitted = False

    # Header label for SP election
    header_sp_label = tk.Label(root, text="SP Election", font=('Helvetica', 18, 'bold'), bg='red', fg='white')
    header_sp_label.pack(pady=10)

    # Load and resize images
    try:
        img1 = Image.open('valt.jpg')
        img1 = img1.resize((150, 150), Image.Resampling.LANCZOS)
        photo1 = ImageTk.PhotoImage(img1)

        img2 = Image.open('tanjiro.jpg')
        img2 = img2.resize((150, 150), Image.Resampling.LANCZOS)
        photo2 = ImageTk.PhotoImage(img2)

        img3 = Image.open('asp1.jpg')
        img3 = img3.resize((150, 150), Image.Resampling.LANCZOS)
        photo3 = ImageTk.PhotoImage(img3)

        img4 = Image.open('asp2.jpg')
        img4 = img4.resize((150, 150), Image.Resampling.LANCZOS)
        photo4 = ImageTk.PhotoImage(img4)

    except Exception as e:
        messagebox.showerror("Error", f"Error loading images: {e}")
        root.destroy()
        return

    selected_sp_image = tk.IntVar()
    selected_asp_image = tk.IntVar()

    # Create a frame to hold the SP images
    sp_image_frame = tk.Frame(root)
    sp_image_frame.pack(pady=10)

    # Create labels for SP image selection
    sp_labels = []
    for i, photo in enumerate([photo1, photo2], start=1):
        label = tk.Label(sp_image_frame, image=photo)
        label.photo = photo  # Keep a reference to avoid garbage collection
        sp_labels.append(label)
        label.grid(row=0, column=i-1, padx=10, pady=10)

    # Event bindings to select the SP image
    def select_sp_image(event, image_id):
        selected_sp_image.set(image_id)
        for label in sp_labels:
            label.config(bg="light blue")
        event.widget.config(bg="green")

    for i, label in enumerate(sp_labels, start=1):
        label.bind("<Button-1>", lambda event, image_id=i: select_sp_image(event, image_id))

    # Create submit button for SP election
    def on_sp_submit():
        global sp_submitted
        selected = selected_sp_image.get()
        if selected == 1:
            votes['cone'] += 1
        elif selected == 2:
            votes['ctwo'] += 1
        else:
            messagebox.showwarning("Selection Error", "Please select an image before submitting.")
            return

        save_votes(votes)
        beep_sound()
        for label in sp_labels:
            label.unbind("<Button-1>")
        sp_submit_button.config(state='disabled')
        sp_submitted = True
        check_all_submitted()

    sp_submit_button = tk.Button(root, text="Submit", command=on_sp_submit, bg="#90EE90", font=('Helvetica', 12, 'bold'))
    sp_submit_button.pack(pady=10, anchor='e', padx=20)

    # Header label for ASP election
    header_asp_label = tk.Label(root, text="ASP Election", font=('Helvetica', 18, 'bold'), bg='blue', fg='white')
    header_asp_label.pack(pady=10)

    # Create a frame to hold the ASP images
    asp_image_frame = tk.Frame(root)
    asp_image_frame.pack(pady=10)

    # Create labels for ASP image selection
    asp_labels = []
    for i, photo in enumerate([photo3, photo4], start=3):
        label = tk.Label(asp_image_frame, image=photo)
        label.photo = photo  # Keep a reference to avoid garbage collection
        asp_labels.append(label)
        label.grid(row=0, column=i-3, padx=10, pady=10)

    # Event bindings to select the ASP image
    def select_asp_image(event, image_id):
        selected_asp_image.set(image_id)
        for label in asp_labels:
            label.config(bg="light blue")
        event.widget.config(bg="green")

    for i, label in enumerate(asp_labels, start=3):
        label.bind("<Button-1>", lambda event, image_id=i: select_asp_image(event, image_id))

    # Create submit button for ASP election
    def on_asp_submit():
        global asp_submitted
        selected = selected_asp_image.get()
        if selected == 3:
            votes['cthree'] += 1
        elif selected == 4:
            votes['cfour'] += 1
        else:
            messagebox.showwarning("Selection Error", "Please select an image before submitting.")
            return

        save_votes(votes)
        beep_sound()
        for label in asp_labels:
            label.unbind("<Button-1>")
        asp_submit_button.config(state='disabled')
        asp_submitted = True
        check_all_submitted()

    asp_submit_button = tk.Button(root, text="Submit", command=on_asp_submit, bg="#90EE90", font=('Helvetica', 12, 'bold'))
    asp_submit_button.pack(pady=10, anchor='e', padx=20)

def check_all_submitted():
    if sp_submitted and asp_submitted:
        messagebox.showinfo("Thank You", "Thank you for voting!")
        restart_app()

# Initialize the main window
root = tk.Tk()
root.configure(bg='light blue')
root.geometry('360x650')
root.title('Vote App - SP and ASP Election')

# Initialize the app layout
initialize_app()

# Start the main event loop
root.mainloop()
