import telebot
    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7954242429:AAFgG7-OFT76ztZ_n3i0eGaT-f6Ze2YBr4M")
    
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
@bot.message_handler(commands=['la'])
def send_heh(message):
    bot.reply_to(message,"lalala")
# Запуск бота
bot.polling()
