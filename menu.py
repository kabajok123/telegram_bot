import telegram
from key_buttons import tele_button, button, back

def main_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(tele_button[0]),],
        [telegram.KeyboardButton(tele_button[1]),],
        [telegram.KeyboardButton(tele_button[2]),],
    ])
    
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def course_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(button[0]),],
        [telegram.KeyboardButton(button[1]),],
        [telegram.KeyboardButton(button[2]),],
        [telegram.KeyboardButton(back[0]),],
    ])

    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )