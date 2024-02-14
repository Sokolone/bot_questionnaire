import json
start_message = 'Спасибо что включили меня!'

questions = [
    {
        "question": "Какой цвет тебе нравится больше всего?",
        "options": {
            1: {"text": "Красный", "points": 3},
            2: {"text": "Синий", "points": 2},
            3: {"text": "Зеленый", "points": 1},
            4: {"text": "Желтый", "points": 0}
        }
    },
    {
        "question": "Какое занятие тебе интереснее всего?",
        "options": {
            1: {"text": "Рисование", "points": 3},
            2: {"text": "Спорт", "points": 2},
            3: {"text": "Чтение", "points": 1},
            4: {"text": "Игра на музыкальном инструменте", "points": 0}
        }
    },
    {
        "question": "Какое животное тебе нравится больше всего?",
        "options": {
            1: {"text": "Собака", "points": 3},
            2: {"text": "Кошка", "points": 2},
            3: {"text": "Енот", "points": 1},
            4: {"text": "Лиса", "points": 0}
        }
    },
    {
        "question": "Какое время года ты предпочитаешь?",
        "options": {
            1: {"text": "Лето", "points": 3},
            2: {"text": "Весна", "points": 2},
            3: {"text": "Осень", "points": 1},
            4: {"text": "Зима", "points": 0}
        }
    },
    {
        "question": "Какая погода тебе нравится больше всего?",
        "options": {
            1: {"text": "Солнечная", "points": 3},
            2: {"text": "Дождливая", "points": 2},
            3: {"text": "Ветреная", "points": 1},
            4: {"text": "Снежная", "points": 0}
        }
    }
]


def write(data, file_name):
    file_for_json = open(file_name, 'w', encoding='utf8')
    json.dump(data, file_for_json)
    file_for_json.close()


def read(file_name):
    """функция возвращает данные из json"""
    file_for_json = open(file_name, 'r', encoding='utf8')
    data = json.load(file_for_json)
    file_for_json.close()
    return data
