import telebot
import os

from segmentation import segmentation

token='5945863355:AAGGTTUlRDQhXXqWI1CiR9EkGVXI7pof69E'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет! Я - телеграм бот для сегментации картинок. Пока что я умею искать машины, так что пришли мне любую фотографию, и я определю автомобиль на ней")


@bot.message_handler(content_types=['photo'])

def handle_change_photo(message):
    "Получаем картинку"
    try:
        raw = message.photo[2].file_id
        input = raw+".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(input,'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id,"Фото принято, обрабатываю") 

    except Exception as e:
        bot.reply_to(message, e)



    "Преобразуем (вызываем функцию из импортируемого модуля)"
    output = raw+"1.jpg"
    segmentation(input, output)


    "Отправляем картинку пользователю"
    try:
        input = open(input, 'rb')
        output = open(output, 'rb')
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(input), telebot.types.InputMediaPhoto(output)])
        bot.send_message(message.chat.id,"Я сделяль!!!")
        input.close()
        output.close()

    except Exception as e:
        bot.reply_to(message, e)



    os.remove('c:/Users/Aila/OOP project/'+str(raw+".jpg"))
    os.remove('c:/Users/Aila/OOP project/'+str(raw+"1.jpg"))


bot.infinity_polling()