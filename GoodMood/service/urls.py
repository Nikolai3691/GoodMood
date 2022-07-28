from django.conf.urls.static import static

from GoodMood import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('', Services.as_view(), name='services'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound