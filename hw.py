from aiogram import Bot, Dispatcher, executor, types
import random
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

num = random.randint(1,3) 

@dp.message_handler(commands='start')
async def start (message:types.Message):
    await message.answer(f"Привет! Начинаем игру отгадай цуфру\nЯ уже загадал число введите свое число:)")

@dp.message_handler(text='1')
async def start (message:types.Message):
    if num == 1:
        await message.reply('Правильно вы огадали')
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    elif num != 1:
        await message.reply('Не правильно вы огадали')
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")   

@dp.message_handler(text='2')
async def start (message:types.Message):
    if num == 2:
        await message.reply('Правильно вы огадали')
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    elif num != 2:
        await message.reply('Не правильно вы огадали')
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg") 

@dp.message_handler(text='3')
async def start (message:types.Message):
    if num == 3:
        await message.reply('Правильно вы огадали')
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    elif num != 3:
        await message.reply('Не правильно вы огадали')
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg") 
        
executor.start_polling(dp)