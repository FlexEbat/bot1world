import logging
from aiogram import Bot, Dispatcher, executor, types, exceptions
from aiogram.dispatcher import Dispatcher, filters, FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from typing import Optional
from asyncio import sleep
import random
import os
import sys

try:
    if os.path.exists('token'):
        bot = Bot(token=open('token', 'r').read(), parse_mode="HTML")
        dp = Dispatcher(bot)
    else:
        token = input('Телеграмм токен>> ')
        open('token', 'w').write(str(token))
        bot = Bot(token=open('token', 'r').read(), parse_mode="HTML")
        dp = Dispatcher(bot)
except exceptions.ValidationError:
    os.remove('token')
    sys.exit('Неверный токен.')
    input('')

logging.basicConfig(level=logging.INFO)

itogs = ['У вас вульвит.', 'У вас бартолинит.', 'У вас бактериальный вагиноз.', 'У вас неспецифический вагинит.', 
    'У вас неспецифический кольпит.', 'У вас вагинальный кандидоз.', 'У вас трихомонадный вагинит.', 'У вас эндоцервицит.', 'У вас эндометрит.', 'У вас аднексит.',
    'У вас вульвит, бартолинит, бактериальный вагиноз, неспецифический вагинит и кольпит, вагинальный кандидоз, трихомонадный вагинит, эндоцервицит, эндометрит, аднексит.']

comments = ["В общем вам пизда.", "Зато вы секси.", "Член прикольный кста.", "Я видел это в Центре Парижа.", "Мне знакомо это влагалище...", "У меня лучше.",
    "Ого пизда", "Лох", "Лол"]

#--------------------------------Клавиатура--------------------------------
start = InlineKeyboardMarkup().add(InlineKeyboardButton('🔎 Начать осмотр влагалища', callback_data='start_vlagalishe'))
restart = InlineKeyboardMarkup().add(InlineKeyboardButton('🔎 Начать повторный осмотр влагалища', callback_data='start_vlagalishe'))
#--------------------------------Клавиатура--------------------------------

def get_rand_element(list_) -> str:
    return random.choice(list_)

async def wait():
    await sleep(random.randint(1, 5))

@dp.callback_query_handler(lambda c: c.data == 'start_vlagalishe')
async def wow(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    await bot.send_message(callback_query.from_user.id, "<b>Начинаем осмотр влагалища...</b>")
    await wait()

    await bot.send_message(callback_query.from_user.id, "<b>Определение состояния тазового дна...</b>")
    await wait()
    
    await bot.send_message(callback_query.from_user.id, "<b>Прощупывание области расположения больших вестибулярных желез...</b>")
    await wait()

    await bot.send_message(callback_query.from_user.id, "<b>Прощупывание уретры...</b>")
    await wait()
    await bot.send_message(callback_query.from_user.id, get_rand_element(['Когда целку потерял друг?', 'Ух пизда...']))

    await bot.send_message(callback_query.from_user.id, "<b>Определение состояния влагалища...</b>")
    await wait()
    await bot.send_message(callback_query.from_user.id, get_rand_element(['😳', 'Ух пизда...', '*хочу ебаться*']))

    await bot.send_message(callback_query.from_user.id, "<b>Исследование влагалищной части шейки матки...</b>")
    await wait()
    await bot.send_message(callback_query.from_user.id, get_rand_element(['ой блять что это', 'Мама вылезай бля']))

    await bot.send_message(callback_query.from_user.id, "<b>Исследование придаток матки...</b>")
    await wait()

    await bot.send_message(callback_query.from_user.id, "<b>Исследование околоматочной клетчатки...</b>")
    await wait()

    await bot.send_message(callback_query.from_user.id, "<b>Исследование наличия патологических процессов в малом тазу...</b>")
    await wait()
    await bot.send_message(callback_query.from_user.id, get_rand_element(['Сметана']))

    await bot.send_message(callback_query.from_user.id, '<b>Подводим итоги...</b>')
    await wait()

    await bot.send_message(callback_query.from_user.id, f'{str(get_rand_element(itogs))}\n\n{str(get_rand_element(comments))}')
    await bot.send_message(callback_query.from_user.id, f'<b>С вас {str(random.randint(1, 30))}т. рублей.</b>')
    await bot.send_message(callback_query.from_user.id, '<b>Спасибо за терпение!</b>')
    

@dp.message_handler()
async def none(message: types.Message):
    if message.text == '/start':
        await message.reply(f'<b>Здравствуйте!</b>\n\n<b>Я - бот, который может провести осмотр вашего влагалища. by mamintank</b>', reply_markup=start)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)