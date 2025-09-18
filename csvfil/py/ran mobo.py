# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:12:45 2024

@author: TANGENT J
"""

import random

def generate_random_questions(num_questions):
    questions = []
    # Generate random questions for each step
    for _ in range(num_questions):
        question = {}
        question["question"] = "Sample question?"
        question["options"] = ["A. Option A", "B. Option B", "C. Option C", "D. Option D"]
        question["correct_answer"] = random.choice(["A", "B", "C", "D"])
        questions.append(question)
    return questions

def display_ports(questions):
    print("\nStep 1: Identify the Rear Panel Ports:")
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question['question']}")
        for option in question['options']:
            print(option)
        print()

def display_functionality(questions):
    print("\nStep 2: Understand the Functionality of Each Port:")
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question['question']}")
        for option in question['options']:
            print(option)
        print()

def display_connection(questions):
    print("\nStep 3: Learn How to Connect Devices:")
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question['question']}")
        for option in question['options']:
            print(option)
        print()

def main():
    num_questions = 20
    # Generate random questions for each step
    ports_questions = generate_random_questions(num_questions)
    functionality_questions = generate_random_questions(num_questions)
    connection_questions = generate_random_questions(num_questions)

    print("Welcome to the Gigabyte GA-Z97X-Gaming 7 Motherboard Learning Program!\n")

    display_ports(ports_questions)
    display_functionality(functionality_questions)
    display_connection(connection_questions)

if __name__ == "__main__":
    main()
