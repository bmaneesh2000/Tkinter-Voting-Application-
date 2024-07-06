import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# File to store the votes
votes_file = 'votes.txt'

# Function to load votes from file
def load_votes():
    if os.path.exists(votes_file):
        with open(votes_file, 'r') as file:
            lines = file.readlines()
            if len(lines) == 6:  # Adjust this number if more candidates are added
                return {
                    'SP1': int(lines[0].strip()),
                    'SP2': int(lines[1].strip()),
                    'SP3': int(lines[2].strip()),
                    'ASP1': int(lines[3].strip()),
                    'ASP2': int(lines[4].strip()),
                    'ASP3': int(lines[5].strip())
                }
    return {'SP1': 0, 'SP2': 0, 'SP3': 0, 'ASP1': 0, 'ASP2': 0, 'ASP3': 0}  # Adjust default values if more candidates are added

# Load initial votes
votes = load_votes()
votes1 = {'SP1': votes['SP1'], 'SP2': votes['SP2'], 'SP3': votes['SP3']}
votes2 = {'ASP1': votes['ASP1'], 'ASP2': votes['ASP2'], 'ASP3': votes['ASP3']}

# Function to check password
def check_password():
    password = 'admin'  # Set your password here
    
    # Create a new window for password input
    password_window = tk.Toplevel(root)
    password_window.title('Enter Password')
    password_window.geometry('300x150')
    password_window.resizable(False, False)
    
    # Center the password window on the screen
    window_width = password_window.winfo_reqwidth()
    window_height = password_window.winfo_reqheight()
    position_right = int(password_window.winfo_screenwidth()/2 - window_width/2)
    position_down = int(password_window.winfo_screenheight()/2 - window_height/2)
    password_window.geometry("+{}+{}".format(position_right, position_down))
    
    # Label and entry for password input
    password_label = ttk.Label(password_window, text="Enter password:")
    password_label.pack(pady=10)
    
    password_entry = ttk.Entry(password_window, show='*')
    password_entry.pack()
    
    # Function to validate password
    def validate_password():
        entered_password = password_entry.get()
        if entered_password == password:
            password_window.destroy()
            root.deiconify()
        else:
            messagebox.showerror("Incorrect Password", "Incorrect password. Please try again.")
            password_entry.delete(0, tk.END)
    
    # Validate button
    validate_button = ttk.Button(password_window, text="Validate", command=validate_password)
    validate_button.pack(pady=10)
    
    # Bind enter key to validate password
    password_window.bind('<Return>', lambda event: validate_password())
    
    # Focus on entry field
    password_entry.focus_set()
    
    # Hide the main root window until password is validated
    root.withdraw()

# Initialize the main window
root = tk.Tk()
root.configure(bg='light green')
root.geometry('500x600')
root.title('Election Results')

# Call function to check password
check_password()

# Create a notebook (tab control)
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill='both', expand=True)

# Fonts
win_font = ('Helvetica', 20, 'bold')
table_font = ('Helvetica', 12)

# Function to load and resize images
def load_images():
    try:
        img1 = Image.open('valt.jpg')
        img1 = img1.resize((150, 150), Image.LANCZOS)
        photo1 = ImageTk.PhotoImage(img1)

        img2 = Image.open('tanjiro.jpg')
        img2 = img2.resize((150, 150), Image.LANCZOS)
        photo2 = ImageTk.PhotoImage(img2)

        img3 = Image.open('sp3.jpg')
        img3 = img3.resize((150, 150), Image.LANCZOS)
        photo3 = ImageTk.PhotoImage(img3)

        img4 = Image.open('asp1.jpg')
        img4 = img4.resize((150, 150), Image.LANCZOS)
        photo4 = ImageTk.PhotoImage(img4)

        img5 = Image.open('asp2.jpg')
        img5 = img5.resize((150, 150), Image.LANCZOS)
        photo5 = ImageTk.PhotoImage(img5)

        # Add ASP3 image if available
        img6 = Image.open('asp3.jpg')
        img6 = img6.resize((150, 150), Image.LANCZOS)
        photo6 = ImageTk.PhotoImage(img6)

        tie_img = Image.open('tie.jpg')
        tie_img = tie_img.resize((150, 150), Image.LANCZOS)
        tie_photo = ImageTk.PhotoImage(tie_img)

        return photo1, photo2, photo3, photo4, photo5, photo6, tie_photo

    except Exception as e:
        messagebox.showerror("Error", f"Error loading images: {e}")
        root.destroy()

# Load images
photo1, photo2, photo3, photo4, photo5, photo6, tie_photo = load_images()

# Determine the winners and losers for each election
winner1_name = max(votes1, key=votes1.get)
winner1_votes = votes1[winner1_name]
loser1_name = min(votes1, key=votes1.get)
loser1_votes = votes1[loser1_name]

winner2_name = max(votes2, key=votes2.get)
winner2_votes = votes2[winner2_name]
loser2_name = min(votes2, key=votes2.get)
loser2_votes = votes2[loser2_name]

# Function to check if any two candidates have equal votes
def check_tie(votes):
    values = list(votes.values())
    max_votes = max(values)
    tied_candidates = [candidate for candidate, vote in votes.items() if vote == max_votes]
    return tied_candidates

# Create page 1 for election 1 results
page1 = ttk.Frame(notebook)
notebook.add(page1, text='Election 1')

tied_candidates1 = check_tie(votes1)
if len(tied_candidates1) > 1:
    tie_label1 = tk.Label(page1, text="Election 1 is a tie between:", font=win_font)
    tie_label1.pack(pady=10)

    for candidate in tied_candidates1:
        if candidate == 'SP1':
            tie_image_label1 = tk.Label(page1, image=photo1)
        elif candidate == 'SP2':
            tie_image_label1 = tk.Label(page1, image=photo2)
        elif candidate == 'SP3':
            tie_image_label1 = tk.Label(page1, image=photo3)
        tie_image_label1.pack()

        tie_votes_label1 = tk.Label(page1, text=f"{candidate}: {votes1[candidate]} votes", font=table_font)
        tie_votes_label1.pack()

else:
    winner1_label = tk.Label(page1, text=f"{winner1_name.upper()} WINS ELECTION 1!", font=win_font)
    winner1_label.pack(pady=10)

    winner1_image_label = tk.Label(page1, image=(photo1 if winner1_name == 'SP1' else photo2 if winner1_name == 'SP2' else photo3))
    winner1_image_label.pack()

    winner1_votes_label = tk.Label(page1, text=f"Votes: {winner1_votes}", font=win_font)
    winner1_votes_label.pack(pady=10)

    table_frame1 = ttk.Frame(page1)
    table_frame1.pack(pady=10)

    tree1 = ttk.Treeview(table_frame1, columns=("candidate", "votes"), show="headings", height=3)
    tree1.heading("candidate", text="Candidate")
    tree1.heading("votes", text="Votes")
    tree1.column("candidate", width=150)
    tree1.column("votes", width=100)

    for name, vote in votes1.items():
        tree1.insert("", "end", values=(name, vote))

    tree1.pack()

# Create page 2 for election 2 results
page2 = ttk.Frame(notebook)
notebook.add(page2, text='Election 2')

tied_candidates2 = check_tie(votes2)
if len(tied_candidates2) > 1:
    tie_label2 = tk.Label(page2, text="Election 2 is a tie between:", font=win_font)
    tie_label2.pack(pady=10)

    for candidate in tied_candidates2:
        if candidate == 'ASP1':
            tie_image_label2 = tk.Label(page2, image=photo4)
        elif candidate == 'ASP2':
            tie_image_label2 = tk.Label(page2, image=photo5)
        elif candidate == 'ASP3':
            tie_image_label2 = tk.Label(page2, image=photo6)
        tie_image_label2.pack()

        tie_votes_label2 = tk.Label(page2, text=f"{candidate}: {votes2[candidate]} votes", font=table_font)
        tie_votes_label2.pack()

else:
    winner2_label = tk.Label(page2, text=f"{winner2_name.upper()} WINS ELECTION 2!", font=win_font)
    winner2_label.pack(pady=10)

    winner2_image_label = tk.Label(page2, image=(photo4 if winner2_name == 'ASP1' else photo5 if winner2_name == 'ASP2' else photo6))
    winner2_image_label.pack()

    winner2_votes_label = tk.Label(page2, text=f"Votes: {winner2_votes}", font=win_font)
    winner2_votes_label.pack(pady=10)

    table_frame2 = ttk.Frame(page2)
    table_frame2.pack(pady=10)

    tree2 = ttk.Treeview(table_frame2, columns=("candidate", "votes"), show="headings", height=3)
    tree2.heading("candidate", text="Candidate")
    tree2.heading("votes", text="Votes")
    tree2.column("candidate", width=150)
    tree2.column("votes", width=100)

    for name, vote in votes2.items():
        tree2.insert("", "end", values=(name, vote))

    tree2.pack()

# Run the main loop
root.mainloop()
