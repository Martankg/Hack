from os import name
from django.contrib import admin
from django.urls import path
from main.views import home, sendMessage
from django.conf.urls.static import static
from fox.settings import STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('sendMessage/', sendMessage, name="sendMessage"),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


