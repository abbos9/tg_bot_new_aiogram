from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

start_ky = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = "who is blue ?", callback_data = "_is"),
			InlineKeyboardButton(text = "AM I Boy ?", callback_data = "am_I"),
		],
	]
)

async def yes_or_no_ky() -> InlineKeyboardMarkup:
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = "✅ Ha", callback_data = f"yes"),
				InlineKeyboardButton(text = "❌ Yo‘q", callback_data = f"no")
			]
		]
	)
	return markup

async def only_inline_search_ky() -> InlineKeyboardMarkup:
	markup = InlineKeyboardMarkup(
		inline_keyboard = [
			[
				InlineKeyboardButton(text = "🔍 Qidirish", web_app = WebAppInfo(url = "https://www.youtube.com/")),
			],
		]
	)
	return markup
