from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from crud_functions import get_all_products

api = '8117805314:AAHoef2Rs_1HbI5dUaNZxqk78fQAd7FcmT0'
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

reply_kb = ReplyKeyboardMarkup(resize_keyboard = True)
reply_button = KeyboardButton(text = 'Рассчитать')
reply_button2 = KeyboardButton(text = 'Информация')
reply_button3 = KeyboardButton(text = 'Купить')
reply_kb.add(reply_button)
reply_kb.add(reply_button2)
reply_kb.add(reply_button3)

kb = InlineKeyboardMarkup(resize_keyboard = True)
inline_button = InlineKeyboardButton(text='Product1', callback_data='product_buying')
inline_button2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
inline_button3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
inline_button4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb.add(inline_button)
kb.add(inline_button2)
kb.add(inline_button3)
kb.add(inline_button4)

images = [
    "1.png",
    "2.png",
    "3.png",
    "4.png"
]

product = get_all_products()

@dp.message_handler(commands='start')
async def starter(message):
    await message.answer('Привет', reply_markup= reply_kb)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    product_list = get_all_products()
    if product_list:
        for product, img_path in zip(product_list, images):
            title, description, price = product[1], product[2], product[3]
            product_info = f'Навзвание: {title} | Описание: {description} | Цена: {price}'
            with open(img_path, 'rb') as img:
                await message.answer_photo(img, caption=product_info)
    await message.answer('Выберите пролукт для покупки', reply_markup= kb)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт')
    await call.answer()

@dp.message_handler()
async def all_text(message):
    await message.answer('Введите команду /start')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)