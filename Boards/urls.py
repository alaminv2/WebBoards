from django.urls import path
from . import views

app_name = 'app_boards'

urlpatterns = [
    path('', views.homeView, name="home"),
    path('create_board/', views.boardFormView, name="board_form"),
    path('board_topics/<board_id>/', views.boardTopicsView, name="board_topics"),
    path('create_topic/<board_id>/', views.topicFormView, name="topic_form"),
    path('new_topic/<board_id>/', views.newTopicView, name='new_topic')
]