from . import *

@hell_cmd(pattern="mm")
async def _(event):
  a = await bot.get_messages(event.chat_id, 0, from_user="me")
  b = await bot.get_messages(event.chat_id)
  await event.edit(f" Your Total messages = {a.total}\n\n And Total group messages : {b.total}")

CmdHelp("mm").add_command(
    "mm", "Count your send messages and Total group messages"
).add()
