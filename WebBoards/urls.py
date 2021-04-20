from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Boards.urls')),
    path('accounts/', include('app_accounts.urls')),
]
