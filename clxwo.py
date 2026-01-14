import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Mini Crossword Puzzle")

# The answer we're looking for
answer = "OOSODE"

# Instructions
label = tk.Label(window, text="Fill in the word! Clue: ALL THAT IS", font=("Arial", 14))
label.pack(pady=10)

# Frame to hold the letter boxes
box_frame = tk.Frame(window)
box_frame.pack(pady=10)

# Create 6 entry boxes (one for each letter)
entries = []
for i in range(6):
    entry = tk.Entry(box_frame, width=3, font=("Arial", 24), justify="center")
    entry.grid(row=0, column=i, padx=5)
    entries.append(entry)
    
    # Limit to 1 character and auto-move to next box
    def limit_char(event, index=i):
        if len(entries[index].get()) >= 1:
            entries[index].delete(1, tk.END)  # Keep only first character
            if index < 5:  # Move to next box
                entries[index + 1].focus()
    
    entry.bind("<KeyRelease>", limit_char)

# Function to check the answer
def check_answer():
    # Get all the letters from the boxes
    user_answer = ""
    for entry in entries:
        user_answer += entry.get().upper()
    
    # Check if it matches
    if user_answer == answer:
        messagebox.showinfo("Result", "🎉 Correct! You solved it!")
    else:
        messagebox.showwarning("Result", "Try again! Keep going!")

# Check button
check_button = tk.Button(window, text="Check Answer", command=check_answer, 
                         font=("Arial", 12), bg="lightblue")
check_button.pack(pady=10)

# Clear button
def clear_boxes():
    for entry in entries:
        entry.delete(0, tk.END)
    entries[0].focus()

clear_button = tk.Button(window, text="Clear", command=clear_boxes, 
                         font=("Arial", 12))
clear_button.pack(pady=5)

# Start with focus on first box
entries[0].focus()

# Run the window
window.mainloop()