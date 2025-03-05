import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7559232909:AAGYuqLOWTzU2ftKOWLyNBYwS1wFWw12S3M"  # Убедись, что токен правильный!
bot = telebot.TeleBot(TOKEN)

# Экранированный текст для MarkdownV2 (используем r"" для избежания SyntaxWarning)
SCRIPT = r"""Здравствуйте 😊
*Вас приветствует Emir Cargo*
🔸 наш тариф \- 4$
🔸 срок доставки 7\-10 дней со дня отправки вашей посылки с нашего склада в Китае
🔸 для получения адреса и кода пройдите регистрацию на сайте emir\-cargo\.kz и заполните адрес по инструкции:
*SAMAL* 
[Инструкция](https://www.instagram.com/reel/DB-5EhnCq0W/?igsh=MXMwczhiOXF1aW95NQ==)
🔸 посылки со дня отправки с нашего склада в Китае отслеживаются на нашем сайте emir\-cargo\.kz по инструкции:
[Отслеживание](https://www.instagram.com/reel/C8rQ_3mCilH/?igsh=MW10a3FhNmVpdG45ZQ==)
🔸 подпишитесь на наш канал в телеграм, там новости и график🫶
[Telegram канал](https://t.me/emir_cargo_samal)
*Наш адрес:*
🔸 Мкр Самал: ул\. Мендикулова 98, БЦ Life Town, бутик 13/3а"""

NO_ANSWER_TEXT = r"""📢 В этом скрипте прописаны ответы на 99% вопросов, которые могут возникнуть\. 
❗️ *Перед тем как писать на номер, убедитесь, что ответа здесь действительно нет\.* ❗️

📞 По остальным вопросам можете обращаться по номеру: *87778603560*
"""

# Кнопки
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Нет ответа на мой вопрос"))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, SCRIPT, parse_mode="MarkdownV2", reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "Нет ответа на мой вопрос")
def no_answer(message):
    bot.send_message(
        message.chat.id, 
        NO_ANSWER_TEXT, 
        parse_mode="Markdown", 
        reply_markup=telebot.types.ReplyKeyboardRemove()
    )


print("Бот запущен...")
bot.polling(none_stop=True)
