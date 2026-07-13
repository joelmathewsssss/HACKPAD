import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

displayio.release_displays()

i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 32
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT, rotation=180)

splash = displayio.Group()
display.root_group = splash

keys_row1 = label.Label(terminalio.FONT, text="PREV | PLAY | NEXT", color=0xFFFFFF, x=10, y=8)
splash.append(keys_row1)

keys_row2 = label.Label(terminalio.FONT, text="[BACK]     [FWD]", color=0xFFFFFF, x=14, y=24)
splash.append(keys_row2)

keyboard.extensions.append(MediaKeys())

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D9, board.D8),
)

encoder_handler.map = (
    ((KC.VOLU, KC.VOLD),),
)

keyboard.matrix = KeysScanner(
    pins=[
        board.D0,
        board.D1,
        board.D2,
        board.D3,
        board.D7,
    ],
    value_when_pressed=False,
)

keyboard.keymap = [[
    KC.MPRV,
    KC.MPLY,
    KC.MNXT,
    KC.LALT(KC.LEFT),
    KC.LALT(KC.RIGHT)
]]

if __name__ == '__main__':
    keyboard.go()