from aiogram import Bot,Dispatcher,executor,types
import logging
import wikipedia

wikipedia.set_lang('uz')



API_TOKEN="7803882244:AAGDxhAtX16ohjEFURxuRg1CgRP7yqa34aw"

logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot=bot)


# start komandasi uchun handler
@dp.message_handler(commands="start")
async def start_message(message:types.Message):
    text="Assalomu alaykum 😊\n"
    text+="Wikipedia botiga xush kelibsiz\n"
    text+="Qidirmoqchi bo'lgan ma'lumotni yozing\n"
    text+="Men tezda javob qaytaraman."
    await message.answer(text)



# wikipedia uchun
@dp.message_handler()
async def message_wikipedia(message:types.Message):
    try:
        text=message.text
        answer=wikipedia.summary(text)
        await message.answer(answer)
    except:
        await message.reply("Bunday ma'lumot topilmadi.")

"""
/malumot

 username: dsdsfdsf
 telegram_id: 45454646

"""











if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)