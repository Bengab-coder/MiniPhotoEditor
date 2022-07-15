from widgets import Button

COLORS = {
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
    "red": (0, 0, 255),
    "yellow": (0, 255, 255),
    "yellow90": (0, 180, 200),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "blue90": (200, 0, 0),
    "blue-click": (255, 50, 50),
    "click":(50,25,5),
}

# Define window size
WIDTH, HEIGHT = 1020, 640

# Some constants

LINE_THICKNESS = 2
CUT_LINE_COLOR = COLORS['red']

BUTTON_COLOR = COLORS['blue']
BUTTON_HOVER_COLOR = COLORS['blue90']
BUTTON_CLICK_COLOR = COLORS["click"]
BUTTON_TEXT_COLOR = COLORS["white"]
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 40

COORDINATES_LINES_THICKNESS = 1
COORDINATES_LINES_COLOR = COLORS['green']
COORDINATES_LINES_MOVE_COLOR = COLORS['red']

EDITING_AREA = [
    [20, 70],
    [1000, 570]
]

buttons_config_dict = [
    {
        'text': "Clear",
        'mode': 'clear'
    },
    {
        'text': 'Import',
        'mode': 'import'
    },
    {
        'text': "Save",
        'mode': 'save'
    },
    {
        'text': "Cut",
        'mode': 'cut'
    },
    {
        'text': 'Paste',
        'mode': 'paste'
    },
    {
        'text': "Copy",
        'mode': 'copy'
    }
]
