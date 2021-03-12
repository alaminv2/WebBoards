from django.urls import path
from . import views

app_name = 'app_boards'

urlpatterns = [
    path('', views.homeView, name="home"),
    path('create_board/', views.boardFormView, name="board_form"),
    path('board/<board_id>/', views.topicsOfBoardView, name="board"),
    path('create_topic/', views.topicFormView, name="topic_form"),

]