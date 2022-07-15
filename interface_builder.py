import cv2 as cv
from config import *
import numpy as np
import pickle
import os

event = 0
xpos = 0
ypos = 0
prev_x, prev_y = 0, 0

is_dragging = False
current_button_dragged = None

if not os.path.exists("BUTTONS-CONFIG"):
    with open("BUTTONS-CONFIG", 'wb') as first:
        buttons = []
else:
    with open("BUTTONS-CONFIG", 'rb') as buttons_config:
        buttons = pickle.load(buttons_config)


def mouse_event_callback(evt, x, y, *args):
    global event, xpos, ypos, is_dragging, current_button_dragged, buttons
    event = evt
    xpos, ypos = x, y
    print(f"Event {event} at xpos={xpos}|ypos={ypos}")

    """
        OPERATIONS:

        LEFT-MOUSE-CLICK --> MOVE-BUTTON
        LEFT-MOUSE-DOUBLE-CLICK --> CREATE-NEW-BUTTON
        RIGHT-MOUSE-CLICK --> DELETE-BUTTON
    """

    # MOVE-BUTTON
    if event == cv.EVENT_LBUTTONDOWN:
        for button in buttons:
            if button.is_hover(xpos, ypos):
                is_dragging = True
                break

    elif event == 4:
        is_dragging = False
        current_button_dragged = None

    # # CREATE-NEW-BUTTON
    # elif event == cv.EVENT_LBUTTONDBLCLK:
    #     new_button = Button(x=xpos, y=ypos)
    #     buttons.append(new_button)
    #
    # # DELETE-BUTTON
    # elif event == cv.EVENT_RBUTTONDOWN:
    #     for button in buttons:
    #         if button.is_hover(xpos, ypos):
    #             buttons.remove(button)

    with open("BUTTONS-CONFIG", "wb") as buttons_config:
        pickle.dump(buttons, buttons_config)


cv.namedWindow("Interface Builder")
cv.setMouseCallback("Interface Builder", mouse_event_callback)

while True:
    canvas = np.zeros([HEIGHT, WIDTH, 3], dtype=np.uint8)

    cv.line(canvas, (0, ypos), (WIDTH, ypos), COLORS['green'], 2)
    cv.line(canvas, (xpos, 0), (xpos, HEIGHT), COLORS['green'], 2)

    if is_dragging:
        # DRAW A BREAKING LINE TO SHOW COORDINATES
        cv.line(canvas, (0, ypos), (WIDTH, ypos), COLORS['red'], 2)
        cv.line(canvas, (xpos, 0), (xpos, HEIGHT), COLORS['red'], 2)

    # Draw coordinates ar top right
    cv.putText(canvas,f"{xpos},{ypos}",(WIDTH-150,20),cv.FONT_HERSHEY_PLAIN,1,COLORS['red'],2)

    for button in buttons:
        cv.rectangle(canvas, (button.x, button.y), (button.x + button.width, button.y + button.height),
                     BUTTON_COLOR,
                     -1)
        if is_dragging:
            if button.is_hover(xpos, ypos):
                cv.rectangle(canvas, (button.x, button.y), (button.x + button.width, button.y + button.height),
                             COLORS['red'],
                             -1)
                button.x = xpos - (button.width // 2)
                button.y = ypos - (button.height // 2)
                print(f"BUTTON POSITION = X={button.x}|Y={button.y}")

    cv.imshow("Interface Builder", canvas)
    key = cv.waitKey(1)
    prev_x, prev_y = xpos, ypos
    if key == ord("d"):
        break
