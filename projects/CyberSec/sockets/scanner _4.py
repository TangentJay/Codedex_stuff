import socket
from tkinter import *

def low_tier_scanner_gui():
    
    results_text.delete(1.0, END)

    # To get users inputs
    host = host_entry.get() or '127.0.0.1'
    start = int(start_entry.get())
    stop = int(end_entry.get())

    results_text.insert(END, f"Scanning host {host}, ports {start}~{stop}\n")
    results_text.insert(END, "-" * 40 + "\n")

    offen_portz = []
    totalScanned = 0

    for port in range(start, stop + 1):
        status_label.config(text=f"Scanning port {port}...")
        root.update()  

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)  # change for speed

        try:
            sock.connect((host, port))
            results_text.insert(END, f"Port {port} is OPEN\n")
            offen_portz.append(port)
        except:
            pass  
        finally:
            sock.close()

        totalScanned += 1

    # Show summary
    results_text.insert(END, "-" * 20 + "\n")
    results_text.insert(END, f"Total ports scanned: {totalScanned}\n")
    if offen_portz:
        results_text.insert(END, f"Number of open ports: {len(offen_portz)}\n")
        results_text.insert(END, f"Open ports: {offen_portz}\n")
    else:
        results_text.insert(END, "No open ports found\n")

    status_label.config(text="Scan finished!")

# --- Tkinter GUI setup ---
root = Tk()
root.title("Low Tier Port Scanner")
root.geometry("550x400")

# Title
Label(root, text="EZ SCAN 1.0", font=("Arial", 14, "bold")).pack(pady=10)

# Input frame
input_frame = Frame(root)
input_frame.pack(pady=10)

# Host
Label(input_frame, text="Host:").grid(row=0, column=0, padx=5)
host_entry = Entry(input_frame, width=15)
host_entry.insert(0, "127.0.0.1")
host_entry.grid(row=0, column=1, padx=5)

# Start port
Label(input_frame, text="Start:").grid(row=0, column=2, padx=5)
start_entry = Entry(input_frame, width=8)
start_entry.insert(0, "42")
start_entry.grid(row=0, column=3, padx=5)

# End port
Label(input_frame, text="End:").grid(row=0, column=4, padx=5)
end_entry = Entry(input_frame, width=8)
end_entry.insert(0, "69")
end_entry.grid(row=0, column=5, padx=5)

# Scan button
Button(root, text="~Start Scan~", command=low_tier_scanner_gui,
       bg="lightgreen", font=("Arial", 12, "bold")).pack(pady=10)

# Status label
status_label = Label(root, text="LETZDUIT", fg="Pink")
status_label.pack()

# Results text area
Label(root, text="Results:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
results_text = Text(root, width=65, height=15, bg="gray", fg="black", font=("Consolas", 10))
results_text.pack(pady=5)

# Clear button
Button(root, text="Clear", command=lambda: results_text.delete(1.0, END),
       bg="orange").pack(pady=5)

root.mainloop()
