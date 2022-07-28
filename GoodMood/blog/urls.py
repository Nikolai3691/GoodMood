from django.conf.urls.static import static

from GoodMood import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('public/<slug:public_slug>/', ShowPublic.as_view(), name='public'),
    path('comment/', Comment.as_view(), name='comment'),
    # path('records/', Records.as_view(), name='records')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound