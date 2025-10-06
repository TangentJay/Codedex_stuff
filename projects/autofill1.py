from pywinauto import Application
import time
import pyautogui

# Option: choose app
use_my_app = True   # change to False if you want Notepad instead

if use_my_app:
    app_path = r"E:\Apps\MyProgram\myprogram.exe"
    app = Application().start(app_path)
    window_title = "MyProgram"   # replace with your actual app's title
else:
    app = Application().start("notepad.exe")
    window_title = "Untitled - Notepad"

# Wait for it to load
time.sleep(3)

# Attach to the window by title (or regex)
dlg = app.window(title_re=f".*{window_title}.*")
dlg.set_focus()

# Type into the app
pyautogui.typewrite('John\n')
pyautogui.typewrite('Doe\n')
pyautogui.typewrite('john.doe@example.com\n')
pyautogui.typewrite('SecurePass123\n')
