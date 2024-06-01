import asyncio
import aiomysql
import logging
import sqlalchemy as sa

from aiogram import Dispatcher, Bot, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from datetime import datetime, timedelta

bot = Bot(token='7079777351:AAHxdvWhAsczZKx9sLTxJzc0k_3UnmLOWic')
dp = Dispatcher()

class Regist(StatesGroup):
    login_usr = State()
    paswrd_usr = State()
    end_state = State()

@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Regist.login_usr)
    await message.answer('Здравствуйте!\nДля входа введите логин')

@dp.message(Regist.login_usr)
async def login_input(message: Message, state: FSMContext):
    await state.update_data(login_usr=message.text)
    await state.set_state(Regist.paswrd_usr)
    await message.answer('Введите пароль')

@dp.message(Regist.paswrd_usr)
async def login_input(message: Message, state: FSMContext):
    await state.update_data(paswrd_usr=message.text)
    await state.set_state(Regist.paswrd_usr)
    data = await state.get_data()
    await state.set_state(Regist.end_state)
    pool = await aiomysql.create_pool(host='localhost', port=3306,
                                      user='root', password='12345DS',
                                      db='database_water_2', autocommit = True)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT count(*) FROM main_page_users WHERE login=%s AND usrpswd=%s", (data["login_usr"], data["paswrd_usr"]))
            (r,) = await cur.fetchone()
            if r == 0:
                await message.answer('Неверный логин или пароль \nВведите /start для повторной попытки входа')
            else:

                #(l,) = await cur.fetchone()
                #await cur.execute("SELECT * FROM main_page_recieve INNER JOIN main_page_emergencies ON main_page_recieve.emergency_id = main_page_emergencies.id")
                await cur.execute("SELECT id FROM main_page_users WHERE login=%s", (data["login_usr"]))
                (l,) = await cur.fetchone()
                #await cur.execute("INSERT INTO main_page_telebot (telebot_id, user_real_id) VALUES (%s, %s)", (str(message.from_user.id), l))
                await cur.execute("UPDATE main_page_users SET tg_id = %s WHERE id = %s", (str(message.from_user.id), l))
                await cur.execute("SELECT tg_id FROM main_page_users WHERE login=%s", (data["login_usr"]))

                (l,) = await cur.fetchone()
                #print(l)
                #await cur.execute("SELECT * FROM main_page_users")
                #l = ()
                #l = await cur.fetchone()
                #print(l)
                await message.answer('Вы вошли\nВведите любое сообщение для старта режима оповещения\nПосле этого в случае аварии вам будут приходить сообщения')
    pool.close()
    await pool.wait_closed()

@dp.message(Regist.end_state)
async def end_input(message: Message, state: FSMContext):
    data = await state.get_data()
    pool = await aiomysql.create_pool(host='localhost', port=3306,
                                      user='root', password='12345DS',
                                      db='database_water_2')
    current_state = await state.get_state()
    if current_state == 'Regist:end_state':
        while True:
            pool = await aiomysql.create_pool(host='localhost', port=3306,
                                              user='root', password='12345DS',
                                              db='database_water_2')
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute("SELECT tg_id FROM main_page_users WHERE login=%s", (data["login_usr"]))
                    (l,) = await cur.fetchone()
                    await cur.execute("SELECT main_page_controllers.controller_name, main_page_recieve.time_right_now, \
main_page_emergencies.em_name FROM main_page_recieve INNER JOIN main_page_emergencies ON main_page_recieve.emergency_id = main_page_emergencies.id \
JOIN main_page_controllers ON main_page_recieve.controller_id = main_page_controllers.id \
JOIN main_page_controllers_users ON main_page_controllers.id = main_page_controllers_users.controller_id \
JOIN main_page_users ON main_page_controllers_users.user_id = main_page_users.id \
WHERE main_page_recieve.emergency_id > 4 AND main_page_users.login = %s ORDER BY main_page_recieve.time_right_now DESC LIMIT 1", (data["login_usr"]))
                    (nam, tim, em) = await cur.fetchone()
                    cur_dat = datetime.now()
                    delta = timedelta(seconds=20)
                    if tim > cur_dat - delta:
                        await bot.send_message(chat_id=l, text=(f'У вас Протечка от контролера {nam}! Тип протечки: {em}'))
                    await asyncio.sleep(5)
            if message.text == 'Стоп':
                break
            pool.close()
            await pool.wait_closed()
    await message.answer('Вы вошли\nТеперь в случае аварии вам будут приходить сообщения')

@dp.message(Command('end'))
async def total_end(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Вы вышли\n Введите \\start для входа в аккаунт')

"""
@dp.message(F.text)
async def cmd_just(bot):
    await message.answer('lol')
"""
"""
async def update_errors(loop):
    pool = await aiomysql.create_pool(host='localhost', port=3306,
                                      user='root', password='12345DS',
                                      db="database_water_2", loop=loop)
    while True:
    #data = await state.get_data()
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
            #await cur.execute("SELECT tg_id FROM main_page_users WHERE login=%s AND usrpswd=%s", (data["login_usr"], data["paswrd_usr"]))
            #(r,) = await cur.fetchone()
            #if r == 0:
                #pass
            #else:
        await asyncio.sleep(loop)
        await bot.send_message(chat_id='590215812', text="lol")
    pool.close()
    await pool.wait_closed()
"""
async def main():
    #dp.include_router(router)

    await dp.start_polling(bot)
    #loop = asyncio.get_event_loop()
    #loop.create_task(update_errors(10))
    #loop.run_until_complete(dp.start_polling())
      # поставим 10 секунд, в качестве теста


if __name__ == '__main__':

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("End")
    #finally:
        #loop.close()