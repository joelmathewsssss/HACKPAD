import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.pixel import Pixel
from kmk.modules.oled import Oled, OledDisplayMode
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()

# ----- Pin setup -----
KEY_PINS = [board.D3, board.D4, board.D2, board.D1, board.D0]  # Adjust to your wiring

keyboard.matrix = KeysScanner(
    pins=KEY_PINS,
    value_when_pressed=False,
)

# ----- Macros -----
macros = Macros()
keyboard.modules.append(macros)

# ----- Encoder -----
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = ((board.D9, board.D8, board.D7),)  # example pins (A, B, optional Switch)
encoder.map = ((KC.VOLD, KC.VOLU, KC.MUTE),)     # rotate left, rotate right, press encoder

# ----- Pixel (WS2812 / SK6812) -----
pixel = Pixel(pin=board.D6, num_pixels=1, rgb_order=(1, 0, 2))  # G,R,B
keyboard.modules.append(pixel)
pixel.set_brightness(0.2)
pixel.set_pixel(0, (255, 0, 0))  # start red

# ----- OLED -----
oled = Oled(
    i2c=board.I2C(),
    address=0x3C,               # typical SSD1306 address
    display_mode=OledDisplayMode.TXT,
    flip=False,
    invert=False
)
keyboard.modules.append(oled)

oled.set_lines("MacroPad", "by KMK", "", "")

# ----- Keymap -----
keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.MACRO("Hello world!"),
        KC.Macro(Press(KC.LGUI), Tap(KC.S), Release(KC.LGUI)),
    ]
]

# ----- Go -----
if __name__ == '__main__':
    keyboard.go()
