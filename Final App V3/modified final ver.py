import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import time  
import winsound  

def beep_sound():
    frequency = 2500 
    duration = 1000
    winsound.Beep(frequency, duration)

def bep_sound():
    frequency = 4500 
    duration = 2000 
    winsound.Beep(frequency, duration)

# File to store the votes
votes_file = 'votes.txt'

# Function to load votes from file
def load_votes():
    if os.path.exists(votes_file):
        try:
            with open(votes_file, 'r') as file:
                lines = file.readlines()
                if len(lines) == 4:
                    return {
                        'cone': int(lines[0].strip()),
                        'ctwo': int(lines[1].strip()),
                        'cthree': int(lines[2].strip()),
                        'cfour': int(lines[3].strip())
                    }
        except Exception as e:
            messagebox.showerror("Error", f"Error loading votes: {e}")
    return {'cone': 0, 'ctwo': 0, 'cthree': 0, 'cfour': 0}

# Function to save votes to file
def save_votes(votes):
    with open(votes_file, 'w') as file:
        file.write(f"{votes['cone']}\n")
        file.write(f"{votes['ctwo']}\n")
        file.write(f"{votes['cthree']}\n")
        file.write(f"{votes['cfour']}\n")

# Function to open the ending window
def open_ending_window():
    ending_window = tk.Tk()
    ending_window.configure(bg='light blue')
    ending_window.geometry('360x400')
    ending_window.title('Thank You')

    # Thank you message
    thank_you_label = tk.Label(ending_window, text="Thank you for voting", font=('Helvetica', 18, 'bold'), bg='light blue', fg='black')
    thank_you_label.pack(pady=100)

    # Submit button to go back to the intro window
    submit_button = tk.Button(ending_window, text="End", command=lambda: [bep_sound() , ending_window.destroy(), open_intro_window()],
                              bg="#90EE90", font=('Helvetica', 16, 'bold'))
    submit_button.pack(pady=20)

    ending_window.mainloop()

# Function to open ASP election window
def open_asp_window():
    asp_window = tk.Tk()
    asp_window.configure(bg='light blue')
    asp_window.geometry('360x400')
    asp_window.title('Vote App - ASP election')

    # Header label for ASP election
    header_asp_label = tk.Label(asp_window, text="ASP election", font=('Helvetica', 18, 'bold'), bg='blue', fg='white')
    header_asp_label.pack(pady=10)

    # Load and resize images
    try:
        img3 = Image.open('asp1.jpg')
        img3 = img3.resize((150, 150), Image.Resampling.LANCZOS)
        photo3 = ImageTk.PhotoImage(img3)

        img4 = Image.open('asp2.jpg')
        img4 = img4.resize((150, 150), Image.Resampling.LANCZOS)
        photo4 = ImageTk.PhotoImage(img4)

    except Exception as e:
        messagebox.showerror("Error", f"Error loading images: {e}")
        asp_window.destroy()

    # Create a variable to track the selected image
    selected_image = tk.IntVar()

    # Create a frame to hold the images
    image_frame = tk.Frame(asp_window)
    image_frame.pack(pady=10)

    # Create labels for image selection
    label3 = tk.Label(image_frame, image=photo3)
    label3.photo = photo3  # Keep a reference to avoid garbage collection
    label3.grid(row=0, column=0, padx=10)
    label4 = tk.Label(image_frame, image=photo4)
    label4.photo = photo4  # Keep a reference to avoid garbage collection
    label4.grid(row=0, column=1, padx=10)

    # Event bindings to select the image
    def select_image(event, image_id):
        selected_image.set(image_id)
        label3.config(bg="white")
        label4.config(bg="white")
        event.widget.config(bg="green")

    label3.bind("<Button-1>", lambda event: select_image(event, 1))
    label4.bind("<Button-1>", lambda event: select_image(event, 2))

    # Create submit button
    def on_submit():
        if selected_image.get() == 1:
            votes['cthree'] += 1
        elif selected_image.get() == 2:
            votes['cfour'] += 1
        else:
            messagebox.showwarning("Selection Error", "Please select an image before submitting.")
            return

        save_votes(votes)
        beep_sound() 
        asp_window.destroy()
        open_ending_window()

    submit_button = tk.Button(asp_window, text="Submit", command=on_submit, bg="#90EE90", font=('Helvetica', 16, 'bold'))
    submit_button.pack(pady=20)

    asp_window.mainloop()

# Initialize the main window
def voting_app():
    root = tk.Tk()
    root.configure(bg='light blue')
    root.geometry('360x400')
    root.title('Vote App - SP election')

    # Header label for SP election
    header_sp_label = tk.Label(root, text="SP election", font=('Helvetica', 18, 'bold'), bg='red', fg='white')
    header_sp_label.pack(pady=10)

    # Load and resize images
    try:
        img1 = Image.open('valt.jpg')
        img1 = img1.resize((150, 150), Image.Resampling.LANCZOS)
        photo1 = ImageTk.PhotoImage(img1)

        img2 = Image.open('tanjiro.jpg')
        img2 = img2.resize((150, 150), Image.Resampling.LANCZOS)
        photo2 = ImageTk.PhotoImage(img2)

    except Exception as e:
        messagebox.showerror("Error", f"Error loading images: {e}")
        root.destroy()

    # Create a variable to track the selected image
    selected_image = tk.IntVar()

    # Create a frame to hold the images
    image_frame = tk.Frame(root)
    image_frame.pack(pady=10)

    # Create labels for image selection
    label1 = tk.Label(image_frame, image=photo1)
    label1.photo = photo1  # Keep a reference to avoid garbage collection
    label1.grid(row=0, column=0, padx=10)
    label2 = tk.Label(image_frame, image=photo2)
    label2.photo = photo2  # Keep a reference to avoid garbage collection
    label2.grid(row=0, column=1, padx=10)

    # Event bindings to select the image
    def select_image(event, image_id):
        selected_image.set(image_id)
        label1.config(bg="white")
        label2.config(bg="white")
        event.widget.config(bg="green")

    label1.bind("<Button-1>", lambda event: select_image(event, 1))
    label2.bind("<Button-1>", lambda event: select_image(event, 2))

    # Create submit button
    def on_submit():
        if selected_image.get() == 1:
            votes['cone'] += 1
        elif selected_image.get() == 2:
            votes['ctwo'] += 1
        else:
            messagebox.showwarning("Selection Error", "Please select an image before submitting.")
            return

        save_votes(votes)
        beep_sound()  
        root.destroy()
        open_asp_window()

    submit_button = tk.Button(root, text="Submit", command=on_submit, bg="#90EE90", font=('Helvetica', 16, 'bold'))
    submit_button.pack(pady=20)

    root.mainloop()

# Create the intro window
def open_intro_window():
    intro_window = tk.Tk()
    intro_window.title("Voting Application")
    intro_window.geometry("400x400")
    intro_window.configure(bg='#ADD8E6')
    intro_window.resizable(False, False)

    # Create intro label and start button
    intro_label = tk.Label(intro_window, text="Voting Application", font=('Helvetica', 24, 'bold'), bg='#ADD8E6')
    intro_label.pack(pady=100)

    start_button = tk.Button(intro_window, text="Start", command=lambda: [intro_window.destroy(), voting_app()],
                             bg="#90EE90", font=('Helvetica', 16, 'bold'))
    start_button.pack(pady=20)

    intro_window.mainloop()

# Load initial votes
votes = load_votes()
cone = votes['cone']
ctwo = votes['ctwo']
cthree = votes['cthree']
cfour = votes['cfour']

# Run the intro window main loop
open_intro_window()

