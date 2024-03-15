import telebot

from info import (
   character_mapping,
   images_info,
   incorrect_answer,
   not_media,
   questions,
   range_number1,
   range_number2,
   sorry,
   start_message,
   )

token = '6442534302:AAEN8cebwVk_IMk-RgLmpUL6nCjCxh8GGOo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def bot_start_message(message):
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['questionnaire'])
def start_questionnaire(message):
    id = message.chat.id
    current_questions = questions.copy()
    points = 0
    ask_question(id, message, current_questions, points)


def ask_question(chat_id, message, remaining_questions, current_points):
    if len(remaining_questions) > 0:
        question = remaining_questions[0]
        bot.send_message(chat_id, question['question'])
        options = question['options']
        for choice_number, answers in options.items():
            bot.send_message(chat_id, f"{choice_number}. {answers['text']}")
        bot.register_next_step_handler(
            message, process_answer, remaining_questions, current_points)
    else:
        character = ''
        for rank_points, char in character_mapping.items():
            if rank_points[0] <= current_points <= rank_points[1]:
                character = char
                break

        result = {
            'points': current_points,
            'character': character,
        }
        if result['character'] in images_info:
            images_path = images_info[result['character']]
        photo = open(images_path, 'rb')
        bot.send_photo(chat_id, photo, f"""Анкета завершена!
                       Твой результат - {result['points']}.
                       Ты {result['character']}!""")


def process_answer(message, remaining_questions, current_points):
    try:
        chat_id = message.chat.id
        answer = message.text
        if answer.isdigit() and range_number1 <= int(answer) <= range_number2:
            current_points += remaining_questions[0]['options'][int(
                answer)]['points']
            remaining_questions.pop(0)
            ask_question(chat_id, message, remaining_questions, current_points)
        else:
            bot.send_message(chat_id, incorrect_answer)
            ask_question(chat_id, message, remaining_questions, current_points)
    except Exception:
        bot.send_message(chat_id, not_media)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, sorry)


bot.polling()
