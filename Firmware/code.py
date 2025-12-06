from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (4, 3, 2, 1)
keyboard.row_pins = ()
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.extensions.append(MediaKeys())

rgb = RGB(
    pixel_pin=6,
    num_pixels=4,
    order=(1, 0, 2),
)
keyboard.extensions.append(rgb)

encoders = EncoderHandler()
keyboard.modules.append(encoders)

encoders.pins = [
    (29, 28, None),
    (27, 26, None),
]

encoders.map = [
    ((KC.AUDIO_VOL_UP,), (KC.AUDIO_VOL_DOWN,)),
    ((KC.MEDIA_FAST_FORWARD,), (KC.MEDIA_REWIND,)),
]

keyboard.keymap = [
    [
        KC.MEDIA_NEXT_TRACK,
        KC.MEDIA_PREV_TRACK,
        KC.MEDIA_PLAY_PAUSE,
        KC.AUDIO_MUTE,
    ]
]

if __name__ == '__main__':
    keyboard.go()
