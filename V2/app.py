import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

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

# Load initial votes
votes = load_votes()
cone = votes['cone']
ctwo = votes['ctwo']
cthree = votes['cthree']
cfour = votes['cfour']

# Initialize the main window
root = tk.Tk()
root.configure(bg='light blue')
root.geometry('360x550')
root.title('Vote App')

# Header label for SP election
header_sp_label = tk.Label(root, text="SP election", font=('Helvetica', 18, 'bold'), bg='red', fg='white')
header_sp_label.grid(row=0, column=1, columnspan=2, pady=10, sticky='nsew')

# Header label for ASP election
header_asp_label = tk.Label(root, text="ASP election", font=('Helvetica', 18, 'bold'), bg='blue', fg='white')
header_asp_label.grid(row=3, column=1, columnspan=2, pady=10, sticky='nsew')

# Load and resize images
try:
    img1 = Image.open('valt.jpg')
    img1 = img1.resize((150, 150), Image.LANCZOS)
    photo1 = ImageTk.PhotoImage(img1)

    img2 = Image.open('tanjiro.jpg')
    img2 = img2.resize((150, 150), Image.LANCZOS)
    photo2 = ImageTk.PhotoImage(img2)

    img3 = Image.open('asp1.jpg')
    img3 = img3.resize((150, 150), Image.LANCZOS)
    photo3 = ImageTk.PhotoImage(img3)

    img4 = Image.open('asp2.jpg')
    img4 = img4.resize((150, 150), Image.LANCZOS)
    photo4 = ImageTk.PhotoImage(img4)

except Exception as e:
    messagebox.showerror("Error", f"Error loading images: {e}")
    root.destroy()

# Button click functions to increment vote counts
def button1_click():
    global cone
    cone += 1
    votes['cone'] = cone
    save_votes(votes)

def button2_click():
    global ctwo
    ctwo += 1
    votes['ctwo'] = ctwo
    save_votes(votes)

def button3_click():
    global cthree
    cthree += 1
    votes['cthree'] = cthree
    save_votes(votes)

def button4_click():
    global cfour
    cfour += 1
    votes['cfour'] = cfour
    save_votes(votes)

# Create buttons
button1 = tk.Button(root, text="SP1", image=photo1, compound=tk.TOP, command=button1_click, font=('Helvetica', 12))
button2 = tk.Button(root, text="SP2", image=photo2, compound=tk.TOP, command=button2_click, font=('Helvetica', 12))
button3 = tk.Button(root, text="Asp1", image=photo3, compound=tk.TOP, command=button3_click, font=('Helvetica', 12))
button4 = tk.Button(root, text="Asp2", image=photo4, compound=tk.TOP, command=button4_click, font=('Helvetica', 12))

# Grid configuration for layout
button1.grid(row=1, column=1, padx=10, pady=10)
button2.grid(row=1, column=2, padx=10, pady=10)
button3.grid(row=4, column=1, padx=10, pady=10)
button4.grid(row=4, column=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
