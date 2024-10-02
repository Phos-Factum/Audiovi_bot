from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command

import app.keyboards as kboard

# Router as a proxy
router = Router()


# Commands


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Hello! I am a Audiovi bot! \nWhat do you want?",
                         reply_markup=kboard.menu)


@router.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer(text="Choose menu item:", reply_markup=kboard.menu)


@router.message(Command("more"))
async def cmd_more(message: Message):
    await message.answer(text="- You can find here an info about us and \
contacts -", reply_markup=kboard.more)


@router.message(Command("help"))
async def cmd_help(message: Message):
    with open("misc/help_cmds.md", "r", encoding="UTF-8") as file:
        help_text = file.read()
    await message.answer(help_text)


@router.message(F.text == "Help")
async def help(message: Message):
    with open("misc/help_cmds.md", "r", encoding="UTF-8") as file:
        help_text = file.read()
    await message.answer(help_text)


@router.message(Command("bye"))
async def cmd_bye(message: Message):
    await message.answer("Thanks for your requests! I will wait for you soon.\
  \nType /start command to use bot.", reply_markup=ReplyKeyboardRemove())


# Filters


@router.message(F.text == "More")
async def f_text_more(message: Message):
    await message.answer(text="- You can find here an info about us and \
contacts -", reply_markup=kboard.more)


@router.message(F.text == "Bye!")
async def f_text_bye(message: Message):
    await message.answer("Thanks for your requests! I will wait for you soon.\
  \nType /start command to use bot.", reply_markup=ReplyKeyboardRemove())


# @router.callback_query(F.data == "close_keyboard")
# async def close_keyboard(callback: CallbackQuery):
#    await callback.answer("")
#    await callback.message.delete()
#    await callback.message.edit_reply_markup(reply_markup=ReplyKeyboardRemove())
