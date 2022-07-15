import pickle
from tkinter import filedialog


import cv2 as cv
import os
import numpy as np

from config import *
from events import MouseEvent
from widgets import Button

key = 0
mouse_events_list = []
last_event = None
current_mode = None


def mouse_event_callback(event, xpos, ypos, *args):
    global last_event
    new_event = MouseEvent(event, xpos, ypos)
    if event != last_event:
        mouse_events_list.append(new_event)
    else:
        for i in mouse_events_list:
            if i._id == event:
                i.x = xpos
                i.y = ypos
    last_event = event


if not os.path.exists("BUTTONS-CONFIG"):
    with open("BUTTONS-CONFIG", 'wb') as first:
        BUTTONS = []
else:
    with open("BUTTONS-CONFIG", 'rb') as buttons_config:
        BUTTONS = pickle.load(buttons_config)

cv.namedWindow("Canvas")
cv.setMouseCallback("Canvas", mouse_event_callback)


def demo_callback():
    print("""
    Hello this is testing the 
    callback function weather 
    it will throw an exception or not
    """)


def browseFiles():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(
            ("JPG IMAGES", "*.jpg*"),
            ("PNG IMAGES","*.png*")
        )
    )

    print(filename)


while True:
    blank_canvas = np.zeros([HEIGHT, WIDTH, 3], dtype=np.uint8)

    for button in BUTTONS:
        cv.rectangle(blank_canvas, (button.x, button.y), (button.x + button.width, button.y + button.height),
                     BUTTON_COLOR, -1)
        if len(mouse_events_list) > 0:
            current_mouse_event = mouse_events_list[-1]
            if button.is_hover(current_mouse_event.x, current_mouse_event.y):
                # When button is clicked down
                if current_mouse_event._id == cv.EVENT_LBUTTONDOWN:
                    cv.rectangle(blank_canvas, (button.x, button.y),
                                 (button.x + button.width, button.y + button.height),
                                 BUTTON_CLICK_COLOR, -1)

                    if not button.is_down:
                        button.is_down = True
                        print(f"Button {button.signature} has mode={button.mode}")
                        if button.mode:
                            current_mode = button.mode
                        if current_mode == "import":
                            browseFiles()
                        # if callable(button.callback_function):
                        #     button.callback_function.__call__()

                # When button is clicked up
                if current_mouse_event._id == cv.EVENT_LBUTTONUP:
                    cv.rectangle(blank_canvas, (button.x, button.y),
                                 (button.x + button.width, button.y + button.height),
                                 BUTTON_COLOR, -1)
                    button.is_down = False

                # When button is hovered
                if current_mouse_event._id == cv.EVENT_MOUSEMOVE:
                    cv.rectangle(blank_canvas, (button.x, button.y),
                                 (button.x + button.width, button.y + button.height),
                                 BUTTON_HOVER_COLOR, -1)
        # Draw Button Text
        cv.putText(blank_canvas, button.text,
                   (int(button.x + button.width * 0.2), int(button.y + button.height * 0.6)),
                   cv.FONT_HERSHEY_PLAIN, 1,
                   COLORS['white'], 2)

    # Listen for MODES

    # Import Image Mode

    # Draw on Image Mode

    # Save Image Mode

    # Crop Image Mode

    # Rotate Image Mode

    # Blur Image Mode

    # UNDO MODE

    # REDO MODE

    # CUT Image

    # Exit MODE

    # Clear Mode

    # Draw rectangle to who editing area
    cv.rectangle(blank_canvas, EDITING_AREA[0], EDITING_AREA[1], COLORS['blue'], 2)

    key = cv.waitKey(1)
    if key == ord("d"):
        break

    cv.imshow("Canvas", blank_canvas)
