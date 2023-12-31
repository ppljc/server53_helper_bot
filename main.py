# -------------- Импорт локальных функций --------------
from create_bot import dp
from data_base import sqlite_db
from handlers import client, admin, other
from mcrcons import bot_rc

# -------------- Импорт функций Aiogram --------------
from aiogram.utils import executor

# -------------- Функции on_startup и on_shotdown --------------
async def on_startup(_):
	print('Бот вышел в онлайн')
	if sqlite_db.sql_start():
		print('Data base connected OK!')
	if bot_rc.mcrcon_start():
		print('MCRcon connected OK!')
	if other.other_source_StartLogging():
		print('Logger created OK!')
	await admin.admin_source_OnStartUp()

async def on_shotdown(_):
	pass

# -------------- Регистрация всех hadler функций --------------
admin.register_handlers_admin(dp)
#other.register_handlers_other(dp)
client.register_handlers_client(dp)

# -------------- Запуск бота --------------
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# -------------- Комментарии --------------
# Функции должны обзываться таким образом принадлежность_затрагиваемыефункции_КонкретноеНазвание
