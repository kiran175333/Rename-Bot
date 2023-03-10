from pyrogram import Client, filters 
from helper.database import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**πΆπππ ππ π πππππππ ππ πππ.\n\nπ΄π‘πππππ:- \n\n`/set_caption {filename}\n\n/set_caption {filesize}\n\n/set_caption {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**YOUR CAPTION SUCCESSFULLY SAVED β**")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("π**Sorry! No Caption Found...**π")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**YOUR CAPTION SUCCESSFULLY DELETED β**")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Your Caption:-**\n\n`{caption}`")
    else:
       await message.reply_text("π**Sorry! No Caption Found...**π")
