import asyncio
import logging

import configurations
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

import routers.router as r
from keybords import inline_ky
from keybords import keyboards

bot = Bot(token = configurations.Settings.bot_token)
dp = Dispatcher()

@dp.message(CommandStart())
async  def start(message: types.Message):
	await message.answer("Hello {}".format(message.from_user.full_name), reply_markup = await keyboards.get_niggas())

async def main():
	dp.include_router(router = r.router)
	await dp.start_polling(bot)

if __name__ == "__main__":
	logging.basicConfig(level = logging.INFO)
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("Shutting down")