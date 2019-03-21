from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('homework/',views.Homeworkmessages),
                path('exam/',views.Exammessages),
                path('',views.Indexs),
                #path('test/rank/',views.Showscores),
                path('onlinetest/',views.Showquestions),
                path('ajax_handle/',views.ajax_handle),
                path('test/',views.Testajax),
                path('testlogin/',views.Onlinetestlogin),
                path('indexs/',views.Indexs),
                path('learningnews/',views.Learningnews),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
