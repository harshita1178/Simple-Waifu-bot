import random
from pymongo import ReturnDocument
from pyrogram.enums import ChatMemberStatus
from shivu import user_totals_collection, shivuu
from pyrogram import Client, filters
from pyrogram.types import Message

ADMINS = [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]

IMAGES = [
    "https://files.catbox.moe/q6uj9h.jpg",
    "https://files.catbox.moe/6bisuy.jpg",
    "https://files.catbox.moe/5gvrsf.jpg",
    "https://files.catbox.moe/zr8a3n.jpg",
    "https://files.catbox.moe/ssycf3.jpg",
    "https://files.catbox.moe/bid1jx.jpg"
]

SHAYARI = [
    "Dil ki hasrat zuban pe aane lagi\n\nTune dekha aur zindagi muskurane lagi\n\nYe ishq ki inteha thi ya deewangi meri\n\nHar soorat me soorat teri nazar aane lagi.",
    "Kya mangu khuda se aap ko pane ke baad\n\nKiska karu intezar zindagi me apke ane k bad\n\nKyu pyaar pe jaan lutate hain log,\n\nAaj malum huaa hain aap ko pane ke baad..!!",
    "Tujhe chahte hain Be-Intehan, Par chahna nahi aata..\n\nYe kaisi mohobbat hai, Ki hume kehna nahi aata.\n\nZindagi main aa jao hamari zindagi ban kar,\n\nKe tere bin humain zinda rehna nahi aata.",
    "Kitna pyar hai tumse ye jan lo,\n\nTum hi zindagi ho meri\n\nIs baat ko maan lo….\n\nTumhe dene ko mere paas\n\nKuchh bhi nahi….\n\nBas ek jaan hai,\n\nJab ji chahe maang lo……!!",
    "Teri saadgi ko nihaarne ka dil karta hain,\n\nTamaam umr tere naam karne ka dil karta hai,\n\nEk mukammal shayari hain tu kudrat ki,\n\nTuje ghazal banake juban pe lane ka dil krta h.",
    "Aakhein kholu toh chehra tumhara ho\n\nBand karu toh sapna tumhara ho,\n\nMaar bhi jau toh koyi gam nahi,\n\nAgar kafan ke badle achal tumhara ho.",
    "Un Haseen palo ko yaad kar rahe the,\n\nAasmaan se aapki baat kar rahe the,\n\nSukun mila jab hume hawao Ne bataya,\n\nAap bhi hame yaad kar rahe the.",
    "Hasrat hai sirf tumhe pane ki,\n\naur koi khawahish nahi is Dewane ki,\n\nshikwa mujhe tumse nahi khuda se hai,\n\nkya zarurat thi tumhe itna khuubsurat banane ki..?",
    "Khushbu ki tarah meri har sans main,\n\nPyar apna basane ka wada karo,\n\nRang jitne tumhari mohabbat ke hain,\n\nMere dil me sajane ka wada karo.",
    "Mann Mein Aap K Har Baat Rhegi\n\nBasti Chhoti Hai Mgar Abaad Rhegi\n\nChahey Ham Bhuladey Zamaney Ko\n\nMgar Aapki Yeh Pyari Si Hansi Hmesha Yaad Rhegi."
]

AUTHOR = "\n\n(Written By) (  𝑫𝒐𝒈𝒆𝒔𝒉 𝑩𝒉𝒂𝒊🍷)"

@shivuu.on_message(filters.command("changetime"))
async def change_time(client: Client, message: Message):

    user_id = message.from_user.id
    chat_id = message.chat.id
    member = await shivuu.get_chat_member(chat_id, user_id)

    if member.status not in ADMINS:
        await message.reply_text("You are not an Admin.")
        return

    try:
        args = message.command
        if len(args) != 2:
            await message.reply_text("Please use: /changetime NUMBER")
            return

        new_frequency = int(args[1])
        if new_frequency < 1:
            await message.reply_text("The message frequency must be greater than or equal to 10.")
            return

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
        caption = SHAYARI[index] + AUTHOR
        image = random.choice(IMAGES)

        await message.reply_photo(
            photo=image,
            caption=caption
        )

    except Exception as e:
        await message.reply_text(f"Failed to change {str(e)}")
