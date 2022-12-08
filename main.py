from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cread import TOKEN
from key_buttons import tele_button, button, back
from menu import main_menu_keyboard, course_menu_keyboard


def record(update: Update, context: CallbackContext):
    text = update.message.text
    if text[:6] == 'Запись':
        print(text)
        context.bot.send_message(
            chat_id='-570723292',
            text=text
        )

def on_click(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="""
1. напишате сооющение "Запись: " и ваше ФИО.
2. ваш номер телефона.
3.выберите удобное вам время.
        """
    )

def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id = update.effective_chat.id,
        sticker = 'CAACAgIAAxkBAAEGba5jc3zpnZwXjXEb-meoeAABlWc1ILEAApcTAAKJkuFLs20pHm-iqMwrBA'
    )
    update.message.reply_text(
        f"Добро Пожаловать {update.effective_user.username}",
        reply_markup=main_menu_keyboard()
    )

ABOUT = tele_button[0]
COURSE_MENU = tele_button[1]
BACK = back[0]
PYTHON = button[0]
LOCATION = tele_button[2]
RECORD = button[3]


def resive_course_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите курс',
        reply_markup=course_menu_keyboard()
    )

def about(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Образовательное учреждение в котором люди любого возраста за короткие сроки могут получить качественное образование в сфере IT. Основная концепция OGOGO академии это дарить знания вместе с эмоциями, развивая не только технические навыки, но и личные качества наших студентов. Целью компании является взращивание новых конкурентоспособных IT специалистов для мирового рынка компьютерных технологий.',
        reply_markup=main_menu_keyboard()
    )

def nazad(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Вы вернулись в главное меню',
        reply_markup=main_menu_keyboard()
    )

def location(update: Update, context: CallbackContext):
    msg = context.bot.send_message(
            update.effective_chat.id,
            text = 'Location Of OGOGO'
        )
    update.message.reply_location(
        #42.873605195923126, 74.6199937538582
        longitude=74.6199937538582,
        latitude=42.873605195923126,
        reply_to_message_id=msg.message_id
    )

def python_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='python_mentor'),
        
    ],
    [InlineKeyboardButton('Lesson', callback_data='python_lesson'),],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )

def button(update: Update, context: CallbackContext):
    keyboard = [
    [
        InlineKeyboardButton('Mentor', callback_data='python_mentor'),
        
    ],
    [InlineKeyboardButton('Lesson', callback_data='python_lesson'),],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    if query.data == 'python_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/ilias.jpg', 'rb'),
            caption = """
name: Ilias
age: 16
expierence: 6 years
work place: Google, Microsoft, Facebook, Oazis
            """,
            reply_markup=reply_murkup
        )
        

    if query.data == 'python_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = "16000 som per month"
        )

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_MENU),
    resive_course_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    nazad
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    location
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RECORD),
    on_click
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    record
))

updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()