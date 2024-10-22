# Бот, который помогает людям сортировать отходы. 
# Подсказывает, какие предметы можно выбрасывать в обычную урну, 
# а какие стоит отдавать на переработку.
import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, '''\
        Привет, я бот, который рассказывает советы по экологии
        Мои команды:
        /sort <наименование мусора для утилизации>
        /time <наименование предмета>\
        '''
        )

@bot.message_handler(commands=['sort'])
def sort_item(message):
    key = telebot.util.extract_arguments(message.text)
    list_utils = [
        'телевизор',
        'батарейки',
        'пылесос',
        'аккумуляторы',
        'шины',
        'бытовая техника',
        'нефтепродукты',
        'градусник',
        'медицинские отходы'
        ]
    if key in list_utils:
        bot.send_message(message.chat.id, f'{key} необходимо отдать на перероботку.')
    else:
        bot.send_message(message.chat.id, f'{key} можно выбросить в обычную урну.') 

@bot.message_handler(commands=['time'])
def time_item(message):
    key =  telebot.util.extract_arguments(message.text)
    decompose_items = {
        'пластиковая бутылка': '450 лет',
        'стеклянная бутылка': '1-2 миллиона лет',
        'бумага': '2-5 лет',
        'картон': '1-3 года',
        'книга': '50-100 лет',
        'журнал': '10-50 лет',
        'резиновая покрышка': '50-80 лет',
        'батарейки': '1-5 лет',
        'аккумуляторы': '5-10 лет',
        'Телевизор': '100-500 лет',
        'пылесос': '100-500 лет',
        'нефтепродукты': '100-500 лет',
        'градусник': '100-500 лет',
        'медицинские отходы': '100-500 лет',
        'банановая кожура': '2-5 недель',
        'полиэтиленовый пакет': '10-20 лет',
        }
    if key in decompose_items:
        bot.send_message(message.chat.id, f'Время разложения: {key} - {decompose_items[key]}')
    else:
        bot.send_message(message.chat.id, f'Время разложения: {key} неизвесто')

bot.infinity_polling()