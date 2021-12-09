from django.http import HttpResponse, HttpResponseNotFound

week_days = {
    'sunday': 'Купить икру Нарядить ёлку Купить подарки',
    'monday': 'Купить билеты в театр Украсить комнату Посмотреть фильм',
    'tuesday': 'Выспаться',
    'wednesday': 'Погулять с собакой',
    'thursday': 'Вынести мусор',
    'friday': 'Купить дом',
    'saturday': 'Выпить чаю',

}


def get_day_week(request, day):
    description = week_days.get(day, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound('Такого дня недели не существует')


def get_day_week_number(request, day):
    return HttpResponse(f'Это {day} день недели')
