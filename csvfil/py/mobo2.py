# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:47:40 2024

@author: TANGENT J
"""

import tkinter as tk
from tkinter import messagebox
import time
import random

class MotherboardLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Motherboard Learning Program")
        self.root.geometry("400x300")

        self.questions = [
            {
                "question": "Which port is used to connect a PS/2 keyboard or mouse to the motherboard?",
                "options": [
                    "PS/2 Port",
                    "DVI-D Port",
                    "HDMI Port",
                    "USB Port"
                ],
                "correct_answer": 1,
                "explanation": "The correct answer is the PS/2 Port. It's used for legacy keyboards or mice."
            },
            {
                "question": "Which port is used to connect a monitor with a DVI cable?",
                "options": [
                    "D-Sub Port",
                    "DVI-D Port",
                    "HDMI Port",
                    "USB Port"
                ],
                "correct_answer": 2,
                "explanation": "The correct answer is the DVI-D Port. It's used for connecting monitors with DVI cables."
            },
            # Add more questions here...
        ]

        self.current_question = 0
        self.correct_answers = 0
        self.total_questions = len(self.questions)

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=350)
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", command=lambda idx=i: self.check_answer(idx))
            button.pack(fill=tk.X, padx=20, pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(self.root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)

        self.ask_question()

    def ask_question(self):
        if self.current_question < self.total_questions:
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]
            random.shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
        else:
            self.show_results()

    def check_answer(self, idx):
        question_data = self.questions[self.current_question]
        if idx + 1 == question_data["correct_answer"]:
            messagebox.showinfo("Correct", "Correct answer!")
            self.correct_answers += 1
        else:
            messagebox.showinfo("Incorrect", "Incorrect answer!")
        self.current_question += 1
        self.ask_question()

    def next_question(self):
        if self.current_question < self.total_questions:
            self.ask_question()
        else:
            self.show_results()

    def show_results(self):
        messagebox.showinfo("Results", f"You got {self.correct_answers} out of {self.total_questions} questions correct.")
        self.root.destroy()

def start_game(num_questions):
    root = tk.Tk()
    app = MotherboardLearningApp(root)
    root.mainloop()

# Main GUI for selecting the number of questions
def main():
    root = tk.Tk()
    root.title("Motherboard Learning Program")
    root.geometry("300x200")

    num_questions_label = tk.Label(root, text="Select the number of questions:")
    num_questions_label.pack(pady=10)

    num_questions_var = tk.IntVar(value=5)
    num_questions_entry = tk.Entry(root, textvariable=num_questions_var)
    num_questions_entry.pack()

    start_button = tk.Button(root, text="Start Game", command=lambda: start_game(num_questions_var.get()))
    start_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
