import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.methods import SendRichMessage

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    rich_payload = {
        "chat_id": message.chat.id,
        "rich_message": {
        "blocks": [{
                "type": "heading",
                "level": 1,
                "size": 1, # smaller the size bigger the text
                "text": "Hi! I format everything you send me."
        }]
        }
    }
    method = SendRichMessage(**rich_payload)
    await bot.session.make_request(bot, method)

@dp.message()
async def echo_message(message: types.Message):
    # format text
    rich_payload = {
        "chat_id": message.chat.id,
        "rich_message": {
            "level": 1, 
            "size": 10,
            "markdown": message.text
        }
    }
    method = SendRichMessage(**rich_payload)
    await bot.session.make_request(bot, method)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
