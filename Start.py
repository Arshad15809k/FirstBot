from pyrogram import Client, Filters


@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    helptxt = f"Hello Bro Your Bot Is 100% Working"
    await message.reply_text(helptxt)
