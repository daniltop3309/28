from django.http import HttpResponse

def info (reguest, name, age, interests):
    return HttpResponse(f"""Обо мне:<br>
                        ФИО: {name}<br>
                        Возраст: {age}<br>
                        Интересы: {interests}""")

def about(reguest, city, marks, learning):
    return HttpResponse(f"""Дополнительная информация:<br>
                        Город: {city}<br>
                        Успеваемость: {marks}<br>
                        Нравится учиться? {learning}
                        """)

def contact(reguest,github, telegram, phone):
    return HttpResponse(f"""Контакты:<br>
                        Гитхаб: {github}<br>
                        Телеграмм: {telegram}<br>
                        Номер телефона: {phone}
                        """)