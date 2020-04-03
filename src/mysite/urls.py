# mysite/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    
    #chat app
    path('', RedirectView.as_view(url = 'chat/'), name='home'),
    path('chat/', include('chat.urls', namespace='chat')),
]