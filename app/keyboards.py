from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           KeyboardButton, InlineKeyboardButton)


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Find video")],
    [KeyboardButton(text="Help"),
     KeyboardButton(text="More")],
    [KeyboardButton(text="Bye!")]
],
    resize_keyboard=True,
    input_field_placeholder="Choose something")

more = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Contacts", callback_data="contacts")],
    [InlineKeyboardButton(text="About us", callback_data="about_us")],
    [InlineKeyboardButton(text="Back", callback_data="close_keyboard")]
])
