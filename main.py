import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://vanishvili93-jpg.github.io/tg-webapp/it.html", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Baca", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Baca sekarang", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Baca sekarang", url="https://vanishvili93-jpg.github.io/tg-webapp/it.html")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Topik hari ini", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Ringkasan", callback_data="summary"))
    text = ("📰 *Selamat datang ke Bacaan Harian.*\n\n"
        "Setiap hari pilihan artikel tentang "
        "budaya, pelancongan, masakan, sains "
        "dan teknologi — untuk dibaca dengan "
        "tenang di chat.\n\n"
        "Tekan *Topik hari ini* "
        "untuk bermula.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Budaya — pameran seni", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Masakan — resipi tradisional", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Pelancongan — lima kampung", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Ringkasan", callback_data="summary"))
    text = ("📋 *Topik hari ini*\n\n"
        "Tiga bacaan pilihan untuk hari ini. "
        "Setiap satu lengkap dalam chat.\n\n"
        "*Budaya* — pameran seni: lima "
        "destinasi muzium di Malaysia.\n\n"
        "*Masakan* — resipi tradisional: empat "
        "hidangan klasik warisan Melayu.\n\n"
        "*Pelancongan* — lima kampung tersembunyi "
        "untuk hujung minggu.\n\n"
        "Tekan tajuk untuk membaca artikel penuh.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Topik hari ini", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Ringkasan", callback_data="summary"))
    text = ("🎨 *Pameran seni: lima destinasi "
        "muzium di Malaysia*\n\n"
        "Muzium-muzium membuka musim baru.\n\n"
        "*Kuala Lumpur — Muzium Negara*\n"
        "Pameran retrospektif seni Melayu "
        "moden. Karya-karya jarang dipamerkan "
        "dari koleksi peribadi dan bahan "
        "arkib yang belum pernah diterbitkan.\n\n"
        "*Pulau Pinang — Muzium Seni Pinang*\n"
        "Seni kontemporari dari bakat-bakat "
        "tempatan. Instalasi, video dan "
        "arca dalam dialog dengan warisan "
        "Peranakan.\n\n"
        "*Melaka — Muzium Stadthuys*\n"
        "Sejarah Selat Melaka melalui "
        "peta-peta purba dan artifak "
        "perdagangan. Empat abad dalam "
        "satu bangunan.\n\n"
        "*Kuching — Muzium Sarawak*\n"
        "Budaya Dayak dan warisan Borneo. "
        "Tekstil, ukiran kayu dan "
        "upacara tradisional.\n\n"
        "*Ipoh — Muzium Darul Ridzuan*\n"
        "Perlombongan bijih timah dan "
        "warisan Perak. Fotografi "
        "hitam putih dari era kolonial.\n\n"
        "_Waktu operasi di laman web rasmi._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Topik hari ini", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Ringkasan", callback_data="summary"))
    text = ("🍳 *Resipi tradisional: empat "
        "hidangan klasik Malaysia*\n\n"
        "Masakan Malaysia adalah khazanah "
        "rasa serantau.\n\n"
        "*Nasi Lemak*\n"
        "Nasi yang dimasak dengan santan "
        "dan daun pandan. Disajikan dengan "
        "sambal, ikan bilis, kacang tanah, "
        "timun dan telur rebus. Sarapan "
        "kebangsaan Malaysia.\n\n"
        "*Rendang*\n"
        "Daging lembu dimasak perlahan "
        "dengan rempah, santan, serai "
        "dan lengkuas sehingga kering. "
        "Hidangan perayaan yang penuh "
        "aroma.\n\n"
        "*Char Kuey Teow*\n"
        "Kuey teow digoreng dengan udang, "
        "kerang, taugeh, telur dan kicap. "
        "Api besar, wajan panas. Rasa "
        "jalanan Pulau Pinang.\n\n"
        "*Roti Canai*\n"
        "Doh yang dilipat berkali-kali "
        "sehingga lembut dan rangup. "
        "Disajikan dengan dal atau kari. "
        "Bila-bila masa, siang atau malam.\n\n"
        "_Sukatan mengikut citarasa sendiri._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Topik hari ini", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Ringkasan", callback_data="summary"))
    text = ("🏠 *Lima kampung tersembunyi "
        "untuk hujung minggu*\n\n"
        "*Kampung Kuantan (Selangor)*\n"
        "Terkenal dengan kelip-kelip di "
        "sepanjang Sungai Selangor. Malam "
        "yang tenang dan pemandangan "
        "ajaib semula jadi.\n\n"
        "*Sekeping Serendah (Selangor)*\n"
        "Hutan tropika dan seni bina moden "
        "bersatu. Penginapan unik di "
        "tengah rimba. Udara segar dan "
        "ketenangan mutlak.\n\n"
        "*Kampung Banghuris (Melaka)*\n"
        "Kampung mural di Melaka. Dinding "
        "rumah-rumah dihiasi lukisan "
        "oleh artis tempatan. Seni "
        "dan tradisi bersatu.\n\n"
        "*Sungai Lembing (Pahang)*\n"
        "Bekas lombong bijih timah British. "
        "Lautan awan di puncak bukit pada "
        "waktu subuh. Sejarah dan "
        "keindahan alam.\n\n"
        "*Kampung Bako (Sarawak)*\n"
        "Pintu masuk ke Taman Negara Bako. "
        "Bekantan, hutan bakau dan "
        "pantai tersembunyi. Borneo "
        "pada yang terbaik.\n\n"
        "_Tempah penginapan lebih awal._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Topik hari ini", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glosari", callback_data="glossary"), types.InlineKeyboardButton(text="❓ Soalan lazim", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Hubungi kami", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Tentang kami", callback_data="about"))
    text = ("🏛 *Ringkasan*\n\n"
        "Dari menu ini anda boleh:\n\n"
        "• Baca *topik hari ini* dan artikel kami.\n"
        "• Lihat ruangan: Budaya, "
        "Pelancongan, Masakan, Sains.\n"
        "• Semak glosari dan soalan lazim.\n"
        "• Ketahui tentang kami dan hubungi.\n\n"
        "Untuk edisi penuh gunakan "
        "butang di bawah.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Topik hari ini", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Ringkasan", callback_data="summary"))
    text = ("📖 *Glosari ringkas*\n\n"
        "*Sidang redaksi* — pasukan yang memilih "
        "dan menyediakan artikel.\n\n"
        "*Rencana* — artikel pendapat yang "
        "membuka sesuatu ruangan.\n\n"
        "*Fotojurnalisme* — cerita berita "
        "yang dibina melalui gambar.\n\n"
        "*Kandungan abadi* — teks yang "
        "relevansinya tidak bergantung "
        "pada berita semasa.\n\n"
        "*Wartawan* — jurnalis yang "
        "melapor dari lapangan.\n\n"
        "*Ruangan* — bahagian tetap "
        "tentang topik tertentu.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Topik hari ini", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Ringkasan", callback_data="summary"))
    text = ("❓ *Soalan lazim*\n\n"
        "*Adakah bot ini rasmi?*\n"
        "Bacaan Harian adalah projek "
        "editorial bebas.\n\n"
        "*Berapa kerap dikemas kini?*\n"
        "Pilihan diperbaharui setiap musim.\n\n"
        "*Bagaimana mematikan notifikasi?*\n"
        "Melalui tetapan chat Telegram.\n\n"
        "*Bolehkah saya kongsi artikel?*\n"
        "Ya, menggunakan pilihan kongsi "
        "dalam Telegram.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Ringkasan", callback_data="summary"), types.InlineKeyboardButton(text="🏛 Tentang kami", callback_data="about"))
    text = ("✏️ *Hubungi kami*\n\n"
        "Untuk surat-menyurat editorial:\n"
        "• E-mel: redaksi@bacaanharian.my\n\n"
        "*Penerbit*\n"
        "Bacaan Harian Sdn. Bhd.\n"
        "Jalan Bukit Bintang 55\n"
        "55100 Kuala Lumpur\n"
        "Malaysia\n\n"
        "Maklum balas pembaca pada hari bekerja.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Ringkasan", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Hubungi kami", callback_data="contact"))
    text = ("🏛 *Tentang Bacaan Harian*\n\n"
        "Bacaan Harian adalah projek "
        "editorial bebas yang khusus "
        "untuk budaya, pelancongan, "
        "masakan dan teknologi.\n\n"
        "Sidang redaksi memilih kandungan "
        "berkualiti setiap hari untuk "
        "rehat yang bermaklumat.\n\n"
        "Edisi Telegram ini direka untuk "
        "bacaan selesa dalam chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Topik hari ini", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Selamat datang! Tekan *Topik hari ini* untuk bermula.", parse_mode="Markdown", reply_markup=markup)


print("Bacaan Harian Bot is running...")
bot.infinity_polling()
