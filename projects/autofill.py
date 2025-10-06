import pyautogui
import time

# Give you a few seconds to switch to the target program
print('Switch to your target window (e.g., Notepad) in 5 seconds...')
time.sleep(2)

# Info to auto-fill
first_name = 'billy'
last_name = 'bob'
email = 'bobbilly892347836@yahoo.com'
password = 'Somethingjsd12345'

# Type them out
pyautogui.typewrite(first_name + '\n')  # \n = Enter
pyautogui.typewrite(last_name + '\n')
pyautogui.typewrite(email + '\n')
pyautogui.typewrite(password + '\n')


