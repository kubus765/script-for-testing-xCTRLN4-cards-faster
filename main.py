import cv2
import numpy as np
import pyautogui
import time
import threading

# Load the image you want to find
enter_template = cv2.imread("resources/enter.png", cv2.IMREAD_GRAYSCALE)
scanned_template = cv2.imread("resources/scanned2.png", cv2.IMREAD_GRAYSCALE)

# Define a function to search for the template image and press the enter key
def enter_thread():
    while True:
        # Get the screen resolution
        screen = np.array(pyautogui.screenshot())
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        h, w = enter_template.shape[:2]

        # Search for the template image in the screen image
        result = cv2.matchTemplate(screen_gray, enter_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        y, x = np.unravel_index(result.argmax(), result.shape)
        if result[y, x] > threshold:
            # The template image has been found, press the enter key
            pyautogui.press('enter')
        time.sleep(0.1)

# Define a function to search for the scanned image and press the enter key
def scanned2_thread():
    while True:
        # Get the screen resolution
        screen = np.array(pyautogui.screenshot())
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        h, w = scanned_template.shape[:2]

        # Search for the template image in the screen image
        result = cv2.matchTemplate(screen_gray, scanned_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        y, x = np.unravel_index(result.argmax(), result.shape)
        if result[y, x] > threshold:
            # The template image has been found, press the enter key
            pyautogui.press('enter')
        time.sleep(0.1)

# Define a function to write to the screen
def write_thread():
    while True:
        # Check if the screen is blank
        if pyautogui.locateOnScreen("resources/blank.png", region=(), grayscale=True, confidence=0.9) is not None:
            # The screen is blank, write the desired text and press the tab key
            # Change the string below to input something else
            pyautogui.write('ISA00006-01')
            pyautogui.press('tab')
        time.sleep(0.1)

# Create the threads
enter_thread = threading.Thread(target=enter_thread)
scanned2_thread = threading.Thread(target=scanned2_thread)
write_thread = threading.Thread(target=write_thread)

# Start the threads
enter_thread.start()
scanned2_thread.start()
write_thread.start()

# Wait for the threads to finish
enter_thread.join()
scanned2_thread.join()
write_thread.join()
