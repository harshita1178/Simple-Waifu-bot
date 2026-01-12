import random
import asyncio
from pymongo import ReturnDocument
from pyrogram.enums import ChatMemberStatus
from shivu import user_totals_collection, shivuu
from pyrogram import Client, filters
from pyrogram.types import Message

ADMINS = [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]

ERROR_IMAGE = "https://files.catbox.moe/wh3x8a.jpg"

IMAGES = [
    "https://files.catbox.moe/q6uj9h.jpg",
    "https://files.catbox.moe/6bisuy.jpg",
    "https://files.catbox.moe/5gvrsf.jpg",
    "https://files.catbox.moe/zr8a3n.jpg",
    "https://files.catbox.moe/ssycf3.jpg",
    "https://files.catbox.moe/bid1jx.jpg"
]

SHAYARI = [
    "Dil ki hasrat zuban pe aane lagi\nTune dekha aur zindagi muskurane lagi\nHar soorat me soorat teri nazar aane lagi.",

    "Kya mangu khuda se aap ko pane ke baad\nKiska karu intezar apke ane ke baad\nAaj malum hua pyaar kya hota hai.",

    "Tujhe chahte hain Be-Intehan\nPar kehna nahi aata\nTere bin zinda rehna nahi aata.",

    "Kitna pyar hai tumse ye jaan lo\nTum hi zindagi ho meri maan lo\nBas ek jaan hai, jab chahe maang lo.",

    "Teri saadgi ko nihaarne ka dil karta hai\nTamaam umr tere naam karne ka dil karta hai\nTu ek mukammal shayari hai.",

    "Aankhein kholu toh chehra tumhara ho\nBand karu toh sapna tumhara ho\nKafan ke badle aanchal tumhara ho.",

    "Un haseen palo ko yaad kar rahe the\nAasmaan se aapki baat kar rahe the\nAap bhi hume yaad kar rahe the.",

    "Hasrat hai sirf tumhe pane ki\nKoi khwahish nahi is deewane ki\nTum itne khoobsurat kyun ho?",

    "Khushbu ki tarah meri har saans mein\nPyar apna basane ka wada karo\nDil mein sajane ka wada karo.",

    "Mann mein aap ki har baat rahegi\nBasti chhoti hai magar abaad rahegi\nAapki hansi hamesha yaad rahegi."
]

@shivuu.on_message(filters.command("changetime", case_sensitive=False))
async def change_time(client: Client, message: Message):

    user_id = message.from_user.id
    chat_id = message.chat.id
    member = await shivuu.get_chat_member(chat_id, user_id)

    if member.status not in ADMINS:
        msg = await message.reply_text("You are not an Admin.")
        await asyncio.sleep(10)
        await msg.delete()
        return

    args = message.command
    if len(args) != 2:
        msg = await message.reply_photo(
            photo=ERROR_IMAGE,
            caption="❌ **Wrong Usage**\n\nPlease use: `/changetime <number>` ♥️"
        )
        await asyncio.sleep(10)
        await msg.delete()
        return

    try:
        new_frequency = int(args[1])
        if new_frequency < 1:
            raise ValueError

        data = await user_totals_collection.find_one_and_update(
            {"chat_id": str(chat_id)},
            {
                "$set": {"message_frequency": new_frequency},
                "$inc": {"shayari_index": 1}
            },
            upsert=True,
            return_document=ReturnDocument.AFTER
        )

        index = data.get("shayari_index", 0) % len(SHAYARI)

        caption = f"""❝ {SHAYARI[index]} ❞

(Written By) ( 𝑫𝒐𝒈𝒆𝒔𝒉 𝑩𝒉𝒂𝒊 🍷 )"""

        msg = await message.reply_photo(
            photo=random.choice(IMAGES),
            caption=caption
        )

        await asyncio.sleep(10)
        await msg.delete()

    except:
        msg = await message.reply_photo(
            photo=ERROR_IMAGE,
            caption="❌ **Invalid Command**\n\nPlease use: `/changetime <number>` ♥️"
        )
        await asyncio.sleep(10)
        await msg.delete()
