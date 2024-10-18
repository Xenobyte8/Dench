import asyncio
import logging
from aiogram_dialog import Dialog, Window, setup_dialogs, DialogManager

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dialogs import getMissionDialog
import config
from handlers import router

async def main():
    bot=config.bot
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    dp.include_router(getMissionDialog)
    setup_dialogs(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())