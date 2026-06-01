import telebot
from telebot import types, apihelper

# Твой новый токен для кликера
TOKEN = "8882275159:AAG3gy_ldYpjcbOvj9qRhzm_a_9fGSn9MmM"

# Настройка прокси для PythonAnywhere
apihelper.proxy = {'https': 'http://proxy.server:3128'}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Твоя ссылка, которая прямо сейчас собирается на GitHub
    web_app = types.WebAppInfo(url="https://tajel19.github.io/leclerc/") 
    
    btn = types.KeyboardButton("🏎 Запустить Leclerc Clicker", web_app=web_app)
    markup.add(btn)
    
    bot.send_message(message.chat.id, 
                     "Привет! Это отдельный тестовый бот-кликер. Нажми на кнопку ниже:", 
                     reply_markup=markup)

if __name__ == '__main__':
    print("Тестовый бот-кликер запущен отдельно от bot.py!")
    bot.polling(none_stop=True)
