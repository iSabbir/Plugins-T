import io
import os
import textwrap

from PIL import Image
from telethon import events

from TelethonHell.DB.gvar_sql import addgvar, gvarstat
from . import *


class STICKER:
    def __init__(self):
        self.emoji = "🍀"
        self.pack = 1


Sticker = STICKER()


def get_string(key):
    if key == "sts_10":
        return "Invalid input. Please reply to a sticker message."
    elif key == "com_1":
        return "Resizing sticker..."
    else:
        return "Unknown string key."


@hell_cmd(pattern="tiny$")
async def ultiny(event):
    reply = await event.get_reply_message()

    if not (reply and reply.media):
        await event.reply(get_string("sts_10"))
        return

    xx = await event.reply(get_string("com_1"))

    ik = await reply.download_media()
    im1 = Image.open("HellConfig/resources/pics/black.jpg")

    if ik.endswith(".tgs"):
        await con.animated_sticker(ik, "json.json")
        with open("json.json") as json_file:
            jsn = json_file.read()

        jsn = jsn.replace("512", "2000")

        with open("json.json", "w") as json_file:
            json_file.write(jsn)

        await con.animated_sticker("json.json", "ult.tgs")
        file = "ult.tgs"
        os.remove("json.json")

    elif ik.endswith((".gif", ".webm", ".mp4")):
        with Image.open(ik) as im:
            z, d = im.size

            if z == d:
                xxx, yyy = 200, 200
            else:
                t = z + d
                a = z / t
                b = d / t
                aa = (a * 100) - 50
                bb = (b * 100) - 50
                xxx = 200 + 5 * aa
                yyy = 200 + 5 * bb

            k = im.resize((int(xxx), int(yyy)))
            k.save("k.png", format="PNG", optimize=True)

        with Image.open("k.png") as im2:
            back_im = im1.copy()
            back_im.paste(im2, (150, 0))
            back_im.save("o.webp", "WEBP", quality=95)

        file = "o.webp"
        os.remove("k.png")

    else:
        with Image.open(ik) as im:
            z, d = im.size

            if z == d:
                xxx, yyy = 200, 200
            else:
                t = z + d
                a = z / t
                b = d / t
                aa = (a * 100) - 50
                bb = (b * 100) - 50
                xxx = 200 + 5 * aa
                yyy = 200 + 5 * bb

            k = im.resize((int(xxx), int(yyy)))
            k.save("k.png", format="PNG", optimize=True)

        with Image.open("k.png") as im2:
            back_im = im1.copy()
            back_im.paste(im2, (150, 0))
            back_im.save("o.webp", "WEBP", quality=95)

        file = "o.webp"
        os.remove("k.png")

    if os.path.exists(file):
        await event.client.send_file(
            event.chat_id, file, reply_to=event.reply_to_msg_id
        )
        os.remove(file)

    await xx.delete()
    os.remove(ik)


CmdHelp("tiny").add_command(
    "tiny", "<Reply to Stickers>", "This command makes stickers tiny!"
).add()
