import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("WEB_APP_URL", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Read", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Read now", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Read now", url="https://vanishvili93-jpg.github.io/tg-webapp/it.html")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📰 *Welcome to Daily Read India.*\n\n"
        "Every day a curated selection of "
        "culture, travel, cuisine, science "
        "and technology — to read at your "
        "own pace in chat.\n\n"
        "Tap *Today's picks* to begin.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Culture — monsoon exhibitions", callback_data="culture"),
        types.InlineKeyboardButton(text="🍛 Cuisine — regional thalis", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Travel — five hidden villages", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📋 *Today's picks*\n\n"
        "Three stories selected for today. "
        "Each one complete in chat.\n\n"
        "*Culture* — monsoon exhibitions: five "
        "must-visit shows at Indian museums.\n\n"
        "*Cuisine* — regional thalis: four "
        "classic preparations from across India.\n\n"
        "*Travel* — five hidden villages to "
        "discover on a long weekend.\n\n"
        "Tap a title to read the full story.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🎨 *Monsoon exhibitions: five "
        "must-visit shows in India*\n\n"
        "Museums open the new season.\n\n"
        "*Delhi — National Museum*\n"
        "A major retrospective of Mughal "
        "miniature paintings. Rare works "
        "from private collections and "
        "unpublished archival material.\n\n"
        "*Mumbai — CSMVS*\n"
        "Chhatrapati Shivaji Maharaj Vastu "
        "Sangrahalaya presents contemporary "
        "Indian art alongside ancient "
        "sculptures. Old meets new.\n\n"
        "*Kolkata — Indian Museum*\n"
        "The oldest museum in Asia. A new "
        "wing dedicated to Bengal Renaissance "
        "art and rare manuscripts from "
        "the 19th century.\n\n"
        "*Jaipur — Albert Hall Museum*\n"
        "Rajasthani textiles, pottery and "
        "jewellery spanning five centuries. "
        "Restored galleries with natural "
        "light.\n\n"
        "*Chennai — Government Museum*\n"
        "Bronze gallery with Chola dynasty "
        "masterpieces. Nataraja and Parvati "
        "in forms rarely seen outside "
        "temple walls.\n\n"
        "_Check museum websites for timings._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🍛 *Regional thalis: four classic "
        "preparations from across India*\n\n"
        "Indian cuisine is a universe of "
        "regional flavours.\n\n"
        "*Gujarati Thali*\n"
        "Sweet, sour and spicy in one plate. "
        "Dal, kadhi, shak, rotli, rice, "
        "pickle and a gulab jamun to finish. "
        "Balanced and vegetarian.\n\n"
        "*South Indian Meals*\n"
        "Rice, sambar, rasam, kootu, poriyal, "
        "appalam and payasam on a banana leaf. "
        "Eaten with the right hand. "
        "Simple and complete.\n\n"
        "*Rajasthani Thali*\n"
        "Dal baati churma, gatte ki sabzi, "
        "ker sangri and bajra roti. Desert "
        "cuisine built for preservation "
        "and bold flavour.\n\n"
        "*Bengali Thali*\n"
        "Shukto, dal, begun bhaja, "
        "maacher jhol, chutney and "
        "mishti doi. A sequence from "
        "bitter to sweet. Designed "
        "to be eaten in order.\n\n"
        "_Adjust spice levels to your "
        "own taste._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🏠 *Five hidden villages for "
        "a long weekend*\n\n"
        "*Mawlynnong (Meghalaya)*\n"
        "Asia's cleanest village. Living "
        "root bridges, bamboo dustbins "
        "and mist rolling through the "
        "Khasi Hills.\n\n"
        "*Malana (Himachal Pradesh)*\n"
        "An ancient village above the "
        "Parvati Valley. Stone houses, "
        "its own parliament and traditions "
        "unchanged for centuries.\n\n"
        "*Zuluk (Sikkim)*\n"
        "A former Silk Route stop at "
        "10,000 feet. Thirty-two hairpin "
        "turns and a view of Kanchenjunga "
        "at sunrise.\n\n"
        "*Gandikota (Andhra Pradesh)*\n"
        "India's Grand Canyon. The Pennar "
        "river cuts through red gorges. "
        "A ruined fort and almost no "
        "tourists.\n\n"
        "*Khimsar (Rajasthan)*\n"
        "A desert village with a 500-year-old "
        "fort. Camel rides, sand dunes and "
        "the silence of the Thar.\n\n"
        "_Book transport in advance for "
        "remote villages._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glossary", callback_data="glossary"), types.InlineKeyboardButton(text="❓ FAQ", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))
    text = ("🏛 *Summary*\n\n"
        "From this menu you can:\n\n"
        "• Read *today's picks* and our stories.\n"
        "• Browse sections: Culture, Travel, "
        "Cuisine, Science.\n"
        "• Check the glossary and FAQ.\n"
        "• Learn about us and get in touch.\n\n"
        "For the full edition, use the "
        "button below.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📖 *A short glossary*\n\n"
        "*Newsroom* — the team that selects "
        "and prepares stories.\n\n"
        "*Editorial* — an opinion piece that "
        "opens a section.\n\n"
        "*Photojournalism* — storytelling "
        "built around photographs.\n\n"
        "*Evergreen content* — stories whose "
        "relevance does not depend on the "
        "news of the day.\n\n"
        "*Correspondent* — a journalist "
        "reporting from the field.\n\n"
        "*Column* — a recurring section "
        "dedicated to a specific topic.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("❓ *Frequently asked questions*\n\n"
        "*Is this bot official?*\n"
        "Daily Read India is an independent "
        "editorial project.\n\n"
        "*How often is it updated?*\n"
        "The selection is refreshed seasonally.\n\n"
        "*How do I mute notifications?*\n"
        "From Telegram chat settings.\n\n"
        "*Can I share a story?*\n"
        "Yes, using Telegram sharing options.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))
    text = ("✏️ *Contact*\n\n"
        "For editorial correspondence:\n"
        "• E-mail: hello@dailyreadindia.in\n\n"
        "*Publisher*\n"
        "Daily Read India Pvt. Ltd.\n"
        "Connaught Place\n"
        "New Delhi 110001\n"
        "India\n\n"
        "Reader feedback on working days.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"))
    text = ("🏛 *About Daily Read India*\n\n"
        "Daily Read India is an independent "
        "editorial project dedicated to "
        "culture, travel, cuisine and "
        "technology.\n\n"
        "The editorial team selects quality "
        "content every day for an informed "
        "break from the daily routine.\n\n"
        "This Telegram edition is designed "
        "for comfortable reading in chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Welcome! Tap *Today's picks* to begin.", parse_mode="Markdown", reply_markup=markup)


print("Daily Read India Bot is running...")
bot.infinity_polling()
