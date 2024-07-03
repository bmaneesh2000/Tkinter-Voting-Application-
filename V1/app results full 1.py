import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Initial vote counts
cone = 0
ctwo = 0
cthree = 0
cfour = 0

# Initialize the main window
root = tk.Tk()
root.configure(bg='light blue')
root.geometry('360x600')
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

    img_tie = Image.open('tie.jpg')
    img_tie = img_tie.resize((150, 150), Image.LANCZOS)
    photo_tie = ImageTk.PhotoImage(img_tie)

except Exception as e:
    messagebox.showerror("Error", f"Error loading images: {e}")
    root.destroy()

# Button click functions to increment vote counts
def button1_click():
    global cone
    cone += 1

def button2_click():
    global ctwo
    ctwo += 1

def button3_click():
    global cthree
    cthree += 1

def button4_click():
    global cfour
    cfour += 1

# Function to display results
def show_results():
    results_window = tk.Toplevel(root)
    results_window.configure(bg='light green')
    results_window.title('Election Results')

    # Determine the winners and losers for each election
    votes1 = {'SP1': cone, 'SP2': ctwo}
    winner1_name = max(votes1, key=votes1.get)
    winner1_votes = votes1[winner1_name]
    loser1_name = min(votes1, key=votes1.get)
    loser1_votes = votes1[loser1_name]

    votes2 = {'asp1': cthree, 'asp2': cfour}
    winner2_name = max(votes2, key=votes2.get)
    winner2_votes = votes2[winner2_name]
    loser2_name = min(votes2, key=votes2.get)
    loser2_votes = votes2[loser2_name]

    win_font = ('Helvetica', 20, 'bold')
    table_font = ('Helvetica', 12)

    # Display results for first election
    if cone == ctwo:
        tie_label1 = tk.Label(results_window, text="Election 1 is a tie!", font=('Helvetica', 20, 'bold'))
        tie_label1.pack(pady=10)

        tie_image_label1 = tk.Label(results_window, image=photo_tie)
        tie_image_label1.pack()

        tie_votes_label1 = tk.Label(results_window, text=f"Votes: {cone}", font=table_font)
        tie_votes_label1.pack()

    else:
        winner1_label = tk.Label(results_window, text=f"{winner1_name.upper()} WINS ELECTION 1!", font=win_font)
        winner1_label.pack(pady=10)

        winner1_image_label = tk.Label(results_window, image=(photo1 if winner1_name == 'SP1' else photo2))
        winner1_image_label.pack()
        winner1_votes_label = tk.Label(results_window, text=f"Votes: {winner1_votes}", font=win_font)
        winner1_votes_label.pack(pady=10)

        table_frame1 = ttk.Frame(results_window)
        table_frame1.pack(pady=10)

        tree1 = ttk.Treeview(table_frame1, columns=("candidate", "votes"), show="headings", height=2)
        tree1.heading("candidate", text="Candidate")
        tree1.heading("votes", text="Votes")
        tree1.column("candidate", width=150)
        tree1.column("votes", width=100)

        for name, vote in votes1.items():
            tree1.insert("", "end", values=(name, vote))

        tree1.pack()

    # Display results for second election
    if cthree == cfour:
        tie_label2 = tk.Label(results_window, text="Election 2 is a tie!", font=('Helvetica', 20, 'bold'))
        tie_label2.pack(pady=10)

        tie_image_label2 = tk.Label(results_window, image=photo_tie)
        tie_image_label2.pack()

        tie_votes_label2 = tk.Label(results_window, text=f"Votes: {cthree}", font=table_font)
        tie_votes_label2.pack()

    else:
        winner2_label = tk.Label(results_window, text=f"{winner2_name.upper()} WINS ELECTION 2!", font=win_font)
        winner2_label.pack(pady=10)

        winner2_image_label = tk.Label(results_window, image=(photo3 if winner2_name == 'asp1' else photo4))
        winner2_image_label.pack()
        winner2_votes_label = tk.Label(results_window, text=f"Votes: {winner2_votes}", font=win_font)
        winner2_votes_label.pack(pady=10)

        table_frame2 = ttk.Frame(results_window)
        table_frame2.pack(pady=10)

        tree2 = ttk.Treeview(table_frame2, columns=("candidate", "votes"), show="headings", height=2)
        tree2.heading("candidate", text="Candidate")
        tree2.heading("votes", text="Votes")
        tree2.column("candidate", width=150)
        tree2.column("votes", width=100)

        for name, vote in votes2.items():
            tree2.insert("", "end", values=(name, vote))

        tree2.pack()

    # Adjust the size of the results window based on content
    results_window.update_idletasks()
    width = results_window.winfo_reqwidth()
    height = results_window.winfo_reqheight()
    x = (results_window.winfo_screenwidth() // 2) - (width // 2)
    y = (results_window.winfo_screenheight() // 2) - (height // 2)
    results_window.geometry(f'{width}x{height}+{x}+{y}')

# Create buttons
button1 = tk.Button(root, text="SP1", image=photo1, compound=tk.TOP, command=button1_click, font=('Helvetica', 12))
button2 = tk.Button(root, text="SP2", image=photo2, compound=tk.TOP, command=button2_click, font=('Helvetica', 12))
button3 = tk.Button(root, text="Asp1", image=photo3, compound=tk.TOP, command=button3_click, font=('Helvetica', 12))
button4 = tk.Button(root, text="Asp2", image=photo4, compound=tk.TOP, command=button4_click, font=('Helvetica', 12))
results_button = tk.Button(root, text="Results", command=show_results, bg="#FFC0CB", font=('Helvetica', 12, 'bold'))

# Grid configuration for layout
button1.grid(row=1, column=1, padx=10, pady=10)
button2.grid(row=1, column=2, padx=10, pady=10)
button3.grid(row=4, column=1, padx=10, pady=10)
button4.grid(row=4, column=2, padx=10, pady=10)
results_button.grid(row=5, column=2, pady=10, padx=10, sticky='se')

# Start the main event loop
root.mainloop() 