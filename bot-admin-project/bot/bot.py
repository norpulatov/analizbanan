from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='YOUR_TOKEN')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Salom, men botman!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
