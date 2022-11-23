
from django.contrib import admin
from django.urls import path
from Samir import views

urlpatterns = [
    path('info', views.info, kwargs={"name": "Ганиев Даниль Ранилевич",
                                  "age":16,
                                  "interests":"программирование"}),
    path('about', views.about, kwargs={"city": "Бавлы",
                                       "marks": "ударник",
                                       "learning": "нравится"}),
    path('contact', views.contact, kwargs={"github": "@turbo3009",
                                           "telegram": "https://github.com/daniltop3309",
                                           "phone": "+89370026208"})
]
