from pywinauto import Application
import time
import pyautogui

# Full path to the exe on your external SSD
app_path = r"E:\Apps\MyProgram\myprogram.exe"

# Start the app
app = Application().start(app_path)


# Wait for it to load
time.sleep(3)

# Bring the app window to the front
# (replace "MyProgram" with the actual window title)
dlg = app.window(title_re=".*MyProgram.*")
dlg.set_focus()

# Type into the app
pyautogui.typewrite('John\n')
pyautogui.typewrite('Doe\n')
pyautogui.typewrite('john.doe@example.com\n')
pyautogui.typewrite('SecurePass123\n')
