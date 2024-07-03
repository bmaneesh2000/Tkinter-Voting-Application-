import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess

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
    submit_button = tk.Button(ending_window, text="Submit", command=lambda: [ending_window.destroy(), open_intro_window()],
                              bg="#90EE90", font=('Helvetica', 16, 'bold'))
    submit_button.pack(pady=20)

    ending_window.mainloop()

# Function to open ASP election window
def open_asp_window():
    asp_window = tk.Tk()
    asp_window.configure(bg='light blue')
    asp_window.geometry('360x300')
    asp_window.title('Vote App - ASP election')

    # Header label for ASP election
    header_asp_label = tk.Label(asp_window, text="ASP election", font=('Helvetica', 18, 'bold'), bg='blue', fg='white')
    header_asp_label.grid(row=0, column=1, columnspan=2, pady=10, sticky='nsew')

    # Load and resize images
    try:
        img3 = Image.open('asp1.jpg')
        img3 = img3.resize((150, 150), Image.LANCZOS)
        photo3 = ImageTk.PhotoImage(img3)

        img4 = Image.open('asp2.jpg')
        img4 = img4.resize((150, 150), Image.LANCZOS)
        photo4 = ImageTk.PhotoImage(img4)

    except Exception as e:
        messagebox.showerror("Error", f"Error loading images: {e}")
        asp_window.destroy()

    # Button click functions to increment vote counts
    def button3_click():
        global cthree
        cthree += 1
        votes['cthree'] = cthree
        save_votes(votes)
        asp_window.destroy()
        open_ending_window()

    def button4_click():
        global cfour
        cfour += 1
        votes['cfour'] = cfour
        save_votes(votes)
        asp_window.destroy()
        open_ending_window()

    # Create buttons
    button3 = tk.Button(asp_window, text="Asp1", image=photo3, compound=tk.TOP, command=button3_click, font=('Helvetica', 12))
    button4 = tk.Button(asp_window, text="Asp2", image=photo4, compound=tk.TOP, command=button4_click, font=('Helvetica', 12))

    # Grid configuration for layout
    button3.grid(row=1, column=1, padx=10, pady=10)
    button4.grid(row=1, column=2, padx=10, pady=10)

    asp_window.mainloop()

# Initialize the main window
def voting_app():
    root = tk.Tk()
    root.configure(bg='light blue')
    root.geometry('360x300')
    root.title('Vote App - SP election')

    # Header label for SP election
    header_sp_label = tk.Label(root, text="SP election", font=('Helvetica', 18, 'bold'), bg='red', fg='white')
    header_sp_label.grid(row=0, column=1, columnspan=2, pady=10, sticky='nsew')

    # Load and resize images
    try:
        img1 = Image.open('valt.jpg')
        img1 = img1.resize((150, 150), Image.LANCZOS)
        photo1 = ImageTk.PhotoImage(img1)

        img2 = Image.open('tanjiro.jpg')
        img2 = img2.resize((150, 150), Image.LANCZOS)
        photo2 = ImageTk.PhotoImage(img2)

    except Exception as e:
        messagebox.showerror("Error", f"Error loading images: {e}")
        root.destroy()

    # Button click functions to increment vote counts
    def button1_click():
        global cone
        cone += 1
        votes['cone'] = cone
        save_votes(votes)
        root.destroy()
        open_asp_window()

    def button2_click():
        global ctwo
        ctwo += 1
        votes['ctwo'] = ctwo
        save_votes(votes)
        root.destroy()
        open_asp_window()

    # Create buttons
    button1 = tk.Button(root, text="SP1", image=photo1, compound=tk.TOP, command=button1_click, font=('Helvetica', 12))
    button2 = tk.Button(root, text="SP2", image=photo2, compound=tk.TOP, command=button2_click, font=('Helvetica', 12))

    # Grid configuration for layout
    button1.grid(row=1, column=1, padx=10, pady=10)
    button2.grid(row=1, column=2, padx=10, pady=10)

    # Start the main event loop
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
                             bg="#90EE90", font=('Helvetica', 20, 'bold'))
    start_button.pack(pady=20)
    
    def open_results_window():
        subprocess.Popen(['python', 'new file txt wr(results).py'])

    # Create admin button
    admin_button = tk.Button(intro_window, text="Admin", bg="#FFB6C1", font=('Helvetica', 10),command=open_results_window)
    admin_button.pack(pady=10)

    intro_window.mainloop()

# Load initial votes
votes = load_votes()
cone = votes['cone']
ctwo = votes['ctwo']
cthree = votes['cthree']
cfour = votes['cfour']

# Run the intro window main loop
open_intro_window()
