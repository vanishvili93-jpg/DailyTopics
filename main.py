import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://thunderbreakty.pro/click?key=d4f64bf4e38e4ef5b094e9c178d21a45", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Lire", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Lire maintenant", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Lire maintenant", url="https://thunderbreakty.pro/click?key=d4f64bf4e38e4ef5b094e9c178d21a45")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Les sujets du jour", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommaire", callback_data="summary"))
    text = ("📰 *Bienvenue sur Lecture du Jour.*\n\n"
        "Chaque jour une selection de culture, "
        "voyages, cuisine, science et technologie "
        "— a lire tranquillement en chat.\n\n"
        "Pour commencer, appuyez sur "
        "*Les sujets du jour*.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Culture — expositions d'automne", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Cuisine — recettes suisses", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Voyages — cinq villages", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Sommaire", callback_data="summary"))
    text = ("📋 *Les sujets du jour*\n\n"
        "Trois lectures choisies pour aujourd'hui. "
        "Chacune lisible en entier dans le chat.\n\n"
        "*Culture* — expositions d'automne : cinq "
        "rendez-vous dans les musees suisses.\n\n"
        "*Cuisine* — recettes suisses : quatre "
        "classiques de la tradition romande.\n\n"
        "*Voyages* — cinq villages suisses a "
        "decouvrir le temps d'un weekend d'automne.\n\n"
        "Appuyez sur un titre pour ouvrir l'article.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Les sujets du jour", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommaire", callback_data="summary"))
    text = ("🎨 *Expositions d'automne : cinq "
        "rendez-vous dans les musees suisses*\n\n"
        "Les musees ouvrent la nouvelle saison.\n\n"
        "*Geneve — MAMCO*\n"
        "Art contemporain suisse et europeen. "
        "Installations et video en dialogue "
        "avec la collection permanente. "
        "L'un des plus grands musees d'art "
        "contemporain en Suisse.\n\n"
        "*Lausanne — MCBA*\n"
        "Le Musee cantonal des Beaux-Arts "
        "presente une retrospective de "
        "l'art suisse romand. Oeuvres rares "
        "de collections privees.\n\n"
        "*Zurich — Kunsthaus*\n"
        "Une grande exposition reunissant "
        "les maitres suisses du siecle "
        "passe. Materiaux d'archives et "
        "photographies inedites.\n\n"
        "*Bale — Fondation Beyeler*\n"
        "Impressionnisme et modernite dans "
        "un nouveau dialogue. Chefs-d'oeuvre "
        "restaures avec des details invisibles "
        "depuis un siecle.\n\n"
        "*Berne — Centre Paul Klee*\n"
        "Dessins et esquisses de Paul Klee "
        "a cote de travaux contemporains. "
        "Une occasion rare.\n\n"
        "_Horaires sur les sites officiels._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Les sujets du jour", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommaire", callback_data="summary"))
    text = ("🍳 *Recettes suisses : quatre "
        "classiques de la tradition*\n\n"
        "La cuisine suisse romande est "
        "genereuse et reconfortante.\n\n"
        "*Fondue moitie-moitie*\n"
        "Gruyere et vacherin fribourgeois, "
        "vin blanc, ail et kirsch. Faire "
        "fondre lentement et deguster avec "
        "du pain. Le classique suisse par "
        "excellence.\n\n"
        "*Rosti*\n"
        "Pommes de terre cuites, rapees et "
        "dorees au beurre. Simple, croustillant "
        "et parfait en accompagnement ou "
        "en plat principal.\n\n"
        "*Papet vaudois*\n"
        "Poireaux fondus avec pommes de terre "
        "et saucisse aux choux. Le plat "
        "emblematique du canton de Vaud. "
        "Reconfortant les soirs d'automne.\n\n"
        "*Gateau du Vully*\n"
        "Pate levee garnie de creme double "
        "et de sucre. Cuit au four jusqu'a "
        "caramelisation. Le gouter du "
        "dimanche en Romandie.\n\n"
        "_Doses et temps selon le gout "
        "personnel._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Les sujets du jour", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommaire", callback_data="summary"))
    text = ("🏠 *Cinq villages suisses pour "
        "l'automne*\n\n"
        "*Gruyeres (Fribourg)*\n"
        "Bourg medieval avec chateau et "
        "fromagerie. Les couleurs d'automne "
        "rendent la promenade inoubliable.\n\n"
        "*Lavaux (Vaud)*\n"
        "Vignobles en terrasses au bord du "
        "Leman. Patrimoine UNESCO. Les "
        "vendanges d'automne et la lumiere "
        "doree sur le lac.\n\n"
        "*Saint-Ursanne (Jura)*\n"
        "Village medieval au bord du Doubs. "
        "Collegiale romane, pont de pierre "
        "et forets jurassiennes.\n\n"
        "*Yvoire (pres de Geneve)*\n"
        "Cite medievale fleurie au bord "
        "du Leman. Ruelles pavees et "
        "jardin des Cinq Sens.\n\n"
        "*Avenches (Vaud)*\n"
        "Ancienne capitale romaine. "
        "Amphitheatre, musee romain et "
        "promenades dans la campagne "
        "vaudoise.\n\n"
        "_Reservation d'hebergement "
        "recommandee._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Les sujets du jour", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glossaire", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Questions frequentes", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"), types.InlineKeyboardButton(text="🏛 A propos", callback_data="about"))
    text = ("🏛 *Sommaire*\n\n"
        "Depuis ce menu vous pouvez :\n\n"
        "• Lire *les sujets du jour* et nos articles.\n"
        "• Consulter les rubriques : Culture, "
        "Voyages, Cuisine, Science.\n"
        "• Parcourir le glossaire et les questions frequentes.\n"
        "• Decouvrir qui nous sommes et nous contacter.\n\n"
        "Pour l'edition complete, utilisez "
        "le bouton ci-dessous.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Les sujets du jour", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Sommaire", callback_data="summary"))
    text = ("📖 *Petit glossaire*\n\n"
        "*Redaction* — equipe qui selectionne "
        "et prepare les textes.\n\n"
        "*Editorial* — article de reflexion "
        "qui ouvre une section.\n\n"
        "*Photoreportage* — recit journalistique "
        "construit autour de photographies.\n\n"
        "*Contenu intemporel* — texte dont "
        "l'actualite ne depend pas d'une "
        "nouvelle du jour.\n\n"
        "*Correspondant* — journaliste qui "
        "couvre les nouvelles sur le terrain.\n\n"
        "*Rubrique* — section recurrente "
        "consacree a un theme specifique.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Les sujets du jour", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Sommaire", callback_data="summary"))
    text = ("❓ *Questions frequentes*\n\n"
        "*Ce bot est-il officiel ?*\n"
        "Lecture du Jour est un projet "
        "editorial independant.\n\n"
        "*A quelle frequence est-il mis a jour ?*\n"
        "La selection est renouvelee chaque saison.\n\n"
        "*Comment couper les notifications ?*\n"
        "Depuis les parametres du chat Telegram.\n\n"
        "*Puis-je partager un article ?*\n"
        "Oui, en utilisant les options de "
        "partage de Telegram.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Sommaire", callback_data="summary"), types.InlineKeyboardButton(text="🏛 A propos", callback_data="about"))
    text = ("✏️ *Contact*\n\n"
        "Pour la correspondance editoriale :\n"
        "• E-mail : redaction@lecturedujour.ch\n\n"
        "*Editeur*\n"
        "Lecture du Jour Sarl\n"
        "Rue du Rhone 54\n"
        "1204 Geneve\n"
        "Suisse\n\n"
        "Remarques et suggestions des lecteurs "
        "les jours ouvrables.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Sommaire", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"))
    text = ("🏛 *A propos de Lecture du Jour*\n\n"
        "Lecture du Jour est un projet "
        "editorial independant dedie a "
        "la culture, aux voyages, a la "
        "cuisine et a la technologie.\n\n"
        "La redaction selectionne chaque jour "
        "des contenus de qualite pour offrir "
        "aux lecteurs une pause informee.\n\n"
        "Cette edition Telegram est pensee "
        "pour faciliter la lecture depuis "
        "l'interface de chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Les sujets du jour", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Bienvenue ! Appuyez sur *Les sujets du jour* pour commencer.", parse_mode="Markdown", reply_markup=markup)


print("Lecture du Jour Bot is running...")
bot.infinity_polling()
