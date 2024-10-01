from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardButton,
                           KeyboardButton, InlineKeyboardButton)


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Find video")],
    [KeyboardButton(text="Help"),
     KeyboardButton(text="More")],
    [KeyboardButton(text="Bye!")]
],
    resize_keyboard=True,
    input_field_placeholder="Choose something")
