from aiogram.filters import Command

from aiogram import F, Router, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

class Registration(StatesGroup):
	full_name = State()
	phone_number = State()

@router.message(Command("register"))
async def register(message: types.Message, state: FSMContext):
	await state.set_state(Registration.full_name)
	await message.answer("Write your full name")

@router.message(Registration.full_name)
async def full_name(message: types.Message, state: FSMContext):
	await state.update_data(full_name = message.text)
	await state.set_state(Registration.phone_number)
	await message.answer("Write your phone number")

@router.message(Registration.phone_number)
async def phone_number(message: types.Message, state: FSMContext):
	await state.update_data(phone_number = message.text)
	data = await state.get_data()
	await message.answer("Registered\n full name {}, and your phone number {}".format(data["full_name"], data["phone_number"]))
	await state.clear()

@router.callback_query(F.data == "_is")
async def _is(callback: types.CallbackQuery):
	await callback.answer("Muhammad Yunus")

@router.callback_query(F.data == "am_I")
async def _is(callback: types.CallbackQuery):
	await callback.message.answer("{} is".format(callback.from_user.full_name))
	await callback.answer()
