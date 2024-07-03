import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import winsound
import time
import subprocess

# File to store the votes
votes_file = 'votes.txt'

# Function to load votes from file
def load_votes():
    if os.path.exists(votes_file):
        with open(votes_file, 'r') as file:
            lines = file.readlines()
            if len(lines) == 6:
                return {
                    'cone': int(lines[0].strip()),
                    'ctwo': int(lines[1].strip()),
                    'cthree': int(lines[2].strip()),
                    'cfour': int(lines[3].strip()),
                    'cfive': int(lines[4].strip()),
                    'csix': int(lines[5].strip())
                }
    return {'cone': 0, 'ctwo': 0, 'cthree': 0, 'cfour': 0, 'cfive': 0, 'csix': 0}

# Function to save votes to file
def save_votes(votes):
    with open(votes_file, 'w') as file:
        file.write(f"{votes['cone']}\n")
        file.write(f"{votes['ctwo']}\n")
        file.write(f"{votes['cthree']}\n")
        file.write(f"{votes['cfour']}\n")
        file.write(f"{votes['cfive']}\n")
        file.write(f"{votes['csix']}\n")

# Function to play a beep sound
def beep_sound():
    frequency = 2500 
    duration = 1000
    winsound.Beep(frequency, duration)

# Load initial votes
votes = load_votes()

def initialize_app():
    global root, selected_sp_image, selected_asp_image, sp_labels, asp_labels, submit_button

    root = tk.Tk()
    root.configure(bg='light blue')
    root.title('Vote App - SP and ASP Election')

    # Maximize the window on startup
    root.state('zoomed')
    root.resizable(False, False) 

    # Header label for SP election
    header_sp_label = tk.Label(root, text="SP Election", font=('Helvetica', 18, 'bold'), bg='red', fg='white')
    header_sp_label.pack(pady=10)

    # Load and resize images to 180x180
    try:
        img1 = Image.open('valt.jpg')
        img1 = img1.resize((180, 180), Image.LANCZOS)
        photo1 = ImageTk.PhotoImage(img1)

        img2 = Image.open('tanjiro.jpg')
        img2 = img2.resize((180, 180), Image.LANCZOS)
        photo2 = ImageTk.PhotoImage(img2)

        img3 = Image.open('sp3.jpg')
        img3 = img3.resize((180, 180), Image.LANCZOS)
        photo3 = ImageTk.PhotoImage(img3)

        img4 = Image.open('asp1.jpg')
        img4 = img4.resize((180, 180), Image.LANCZOS)
        photo4 = ImageTk.PhotoImage(img4)

        img5 = Image.open('asp2.jpg')
        img5 = img5.resize((180, 180), Image.LANCZOS)
        photo5 = ImageTk.PhotoImage(img5)

        img6 = Image.open('asp3.jpg')
        img6 = img6.resize((180, 180), Image.LANCZOS)
        photo6 = ImageTk.PhotoImage(img6)

    except Exception as e:
        messagebox.showerror("Error", f"Error loading images: {e}")
        root.destroy()
        return

    selected_sp_image = tk.IntVar()
    selected_asp_image = tk.IntVar()

    # Create a frame to hold the SP images
    sp_image_frame = tk.Frame(root)
    sp_image_frame.pack(pady=10)

    # Create labels for SP image selection with increased spacing
    sp_labels = []
    sp_names = ["Valt", "Tanjiro", "SP3"]
    for i, (photo, name) in enumerate(zip([photo1, photo2, photo3], sp_names), start=1):
        label_frame = tk.Frame(sp_image_frame, bg='white')  # Frame for white background
        label_frame.grid(row=0, column=i-1, padx=20, pady=20)

        label = tk.Label(label_frame, image=photo)
        label.photo = photo  
        label.pack()

        # Add a label for image name beneath the image with white background
        name_label = tk.Label(label_frame, text=name, font=('Helvetica', 12), bg='white')
        name_label.pack(pady=(5,0))  # Add some padding to separate the image and text

        sp_labels.append(label)

    # Event bindings to select the SP image
    def select_sp_image(event, image_id):
        selected_sp_image.set(image_id)
        for label in sp_labels:
            label.config(bg="light blue")
        event.widget.config(bg="green")

    for i, label in enumerate(sp_labels, start=1):
        label.bind("<Button-1>", lambda event, image_id=i: select_sp_image(event, image_id))

    # Header label for ASP election
    header_asp_label = tk.Label(root, text="ASP Election", font=('Helvetica', 18, 'bold'), bg='blue', fg='white')
    header_asp_label.pack(pady=10)

    # Create a frame to hold the ASP images
    asp_image_frame = tk.Frame(root)
    asp_image_frame.pack(pady=10)

    # Create labels for ASP image selection with increased spacing
    asp_labels = []
    asp_names = ["ASP1", "ASP2", "ASP3"]
    for i, (photo, name) in enumerate(zip([photo4, photo5, photo6], asp_names), start=4):
        label_frame = tk.Frame(asp_image_frame, bg='white')  # Frame for white background
        label_frame.grid(row=0, column=i-4, padx=20, pady=20)

        label = tk.Label(label_frame, image=photo)
        label.photo = photo  
        label.pack()

        # Add a label for image name beneath the image with white background
        name_label = tk.Label(label_frame, text=name, font=('Helvetica', 12), bg='white')
        name_label.pack(pady=(5,0))  # Add some padding to separate the image and text

        asp_labels.append(label)

    # Event bindings to select the ASP image
    def select_asp_image(event, image_id):
        selected_asp_image.set(image_id)
        for label in asp_labels:
            label.config(bg="light blue")
        event.widget.config(bg="green")

    for i, label in enumerate(asp_labels, start=4):
        label.bind("<Button-1>", lambda event, image_id=i: select_asp_image(event, image_id))

    # Create a single submit button for both elections
    def on_submit():
        sp_selected = selected_sp_image.get()
        asp_selected = selected_asp_image.get()
        if sp_selected == 1:
            votes['cone'] += 1
        elif sp_selected == 2:
            votes['ctwo'] += 1
        elif sp_selected == 3:
            votes['cthree'] += 1
        else:
            messagebox.showwarning("Selection Error", "Please select an SP image before submitting.")
            return

        if asp_selected == 4:
            votes['cfour'] += 1
        elif asp_selected == 5:
            votes['cfive'] += 1
        elif asp_selected == 6:
            votes['csix'] += 1
        else:
            messagebox.showwarning("Selection Error", "Please select an ASP image before submitting.")
            return

        save_votes(votes)
        for label in sp_labels:
            label.unbind("<Button-1>")
        for label in asp_labels:
            label.unbind("<Button-1>")
        submit_button.config(state='disabled')
        show_message_window()

    submit_button = tk.Button(root, text="Submit", command=on_submit, bg="#90EE90", font=('Helvetica', 12, 'bold'))
    submit_button.place(relx=0.5, rely=0.95, anchor='s')  # Adjust rely to move the button higher up

    root.mainloop()

def show_message_window():
    global message_window

    message_window = tk.Toplevel()
    message_window.geometry('300x170')
    message_window.title('Thank You!')
    message_window.configure(bg='light blue')

    message_label = tk.Label(message_window, text="Thanks for voting!", font=('Helvetica', 16, 'bold'), bg='light blue')
    message_label.pack(pady=10)

    ok_button = tk.Button(message_window, text="OK", command=close_message_window, bg="#90EE90", font=('Helvetica', 12, 'bold'), width=10)

    ok_button.pack(pady=20)

    admin_button = tk.Button(message_window, text="Admin", command=open_results_window, bg="#00FFFF", font=('Helvetica', 9,'bold'))
    admin_button.pack(pady=10)

    beep_sound()

def open_results_window():
    message_window.destroy()
    root.destroy()
    subprocess.Popen(['python', 'result.py'])


def close_message_window():
    message_window.destroy()
    restart_app()

def restart_app():
    root.destroy()
    time.sleep(4)
    initialize_app()

# Initialize the application
initialize_app()
