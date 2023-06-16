import requests,random
from bs4 import BeautifulSoup as bs

@hell_cmd(pattern="hq")
async def hurray(e):
    a = requests.get("https://www.brainyquote.com/topics/hackers-quotes")
    bt = bs(a.content, "html.parser",from_encoding="utf-8")
    out = random.choice(bt.find_all("div","clearfix"))
    mt = ""
    mt += out.findNext().text
    mt += "\n\n**" + out.findNext().findNext().text + "**"
    await eor(e, mt)
    
CmdHelp("hq").add_command(
    "hqoute", "This command give you hackers qoute!"
).add()
   