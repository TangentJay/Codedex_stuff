# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:53:02 2024

@author: TANGENT J
"""

import time

def display_step(step_number, step_description):
    print(f"\nStep {step_number}: {step_description}")
    input("Press Enter to continue...")

def display_ports():
    print("\nStep 1: Identify the Rear Panel Ports:")
    print("1. PS/2 Keyboard/Mouse Port: This port is used to connect a PS/2 keyboard or mouse to the motherboard. It's a legacy port but still supported on many motherboards for compatibility with older peripherals.")
    input("Press Enter to take the quiz...")
    quiz_ports()

def display_functionality():
    print("\nStep 2: Understand the Functionality of Each Port:")
    print("PS/2 Port: Connects a keyboard or mouse.")
    input("Press Enter to take the quiz...")
    quiz_functionality()

def display_connection():
    print("\nStep 3: Learn How to Connect Devices:")
    print("Keyboard/Mouse: Use the PS/2 port for legacy keyboards or mice.")
    input("Press Enter to take the quiz...")
    quiz_connection()

def display_conclusion():
    print("\nConclusion:")
    print("Understanding the ports on your motherboard is essential for building and configuring your computer. Knowing how to connect various devices will allow you to effectively utilize your hardware for different purposes, whether it's gaming, productivity, or multimedia consumption.")

def quiz_ports():
    print("\nQuiz: Rear Panel Ports")
    print("What is the purpose of the PS/2 Keyboard/Mouse Port?")
    print("A. Connects a keyboard or mouse.")
    print("B. Connects a monitor.")
    print("C. Connects a printer.")
    print("D. Connects a USB device.")
    answer = input("Enter your answer (A/B/C/D): ")
    if answer.lower() == "a":
        print("Correct! PS/2 port is indeed used to connect a keyboard or mouse.")
    else:
        print("Incorrect. The correct answer is A. PS/2 port is used to connect a keyboard or mouse.")

def quiz_functionality():
    print("\nQuiz: Port Functionality")
    print("What does the PS/2 port connect?")
    print("A. Monitor")
    print("B. Keyboard or Mouse")
    print("C. USB device")
    print("D. Printer")
    answer = input("Enter your answer (A/B/C/D): ")
    if answer.lower() == "b":
        print("Correct! PS/2 port connects a keyboard or mouse.")
    else:
        print("Incorrect. The correct answer is B. PS/2 port connects a keyboard or mouse.")

def quiz_connection():
    print("\nQuiz: Connecting Devices")
    print("How should you connect a monitor to your computer?")
    print("A. Use the USB port.")
    print("B. Use the HDMI port.")
    print("C. Use the Ethernet port.")
    print("D. Use the PS/2 port.")
    answer = input("Enter your answer (A/B/C/D): ")
    if answer.lower() == "b":
        print("Correct! You should use the HDMI port to connect a monitor to your computer.")
    else:
        print("Incorrect. The correct answer is B. You should use the HDMI port to connect a monitor to your computer.")

def main():
    print("Welcome to the Gigabyte GA-Z97X-Gaming 7 Motherboard Learning Program!")

    display_step(1, "Identify the Rear Panel Ports")
    display_ports()

    display_step(2, "Understand the Functionality of Each Port")
    display_functionality()

    display_step(3, "Learn How to Connect Devices")
    display_connection()

    display_conclusion()

if __name__ == "__main__":
    main()
