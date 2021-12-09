from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

zodiac = {"aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
          "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
          "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
          "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
          "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
          "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
          "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
          "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
          "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
          "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
          "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
          "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
          }


def get_sign_zodiak(request, sign_zodiak: str):
    description = zodiac.get(sign_zodiak, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f'{sign_zodiak} не является знаком зодика')


def get_sign_zodiak_number(request, sign_zodiak: int):
    description = list(zodiac)
    if sign_zodiak > len(description):
        return HttpResponseNotFound(f'{sign_zodiak} не является знаком зодика')
    name_sign_zodiak = description[sign_zodiak - 1]
    redirect_url = reverse('horoscope_name', args=[name_sign_zodiak])
    return HttpResponseRedirect(redirect_url)


def index(request):
    zodiacs = list(zodiac)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)
