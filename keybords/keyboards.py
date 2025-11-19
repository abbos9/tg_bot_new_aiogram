from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(
	keyboard = [
		[KeyboardButton(text = "Nigga", )],
		[KeyboardButton(text = "Muhammad Yunus"), KeyboardButton(text = "Said")],
	], resize_keyboard = True, input_field_placeholder = "choose your favorite option",
)

niggas = [
	{
		"id": 1,
		"name": "Yunus",
	},
	{
		"id": 2,
		"name": "Saidabbos",
	},
	{
		"id": 3,
		"name": "Saidalo",
	}
]

async def get_niggas():
	keyboard = ReplyKeyboardBuilder()
	for nigga in niggas:
		keyboard.add(KeyboardButton(text = nigga["name"]))
	return keyboard.adjust(2).as_markup()