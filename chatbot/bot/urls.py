from django.urls import path
from . import views

urlpatterns = [
    path('bot/', views.home, name='bot-home'),
    # path('bot/answer/', views.get_answer, name='bot-answer')
]