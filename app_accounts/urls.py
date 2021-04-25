from django.urls import path
from . import views

app_name = 'app_accounts'

urlpatterns = [
    path('signup/', views.signupView, name='signup'),
]
