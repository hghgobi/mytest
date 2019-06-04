from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [path('homework/',views.Homeworkmessages),
               path('class/',views.Classmessages),
                path('exam/',views.Exammessages),
                path('',views.Onlinetestlogin),
                #path('test/rank/',views.Showscores),
                path('logout/',views.Logout),
                path('onlinetest/',views.Showquestions),
                path('ajax_handle/',views.ajax_handle),
                path('test/',views.Testajax),
                path('testlogin/',views.Onlinetestlogin),
                path('indexs/',views.Indexs),
                path('learningnews/',views.Learningnews),
                path('onlinetestrank/',views.Onlinetestrank),
                path('classnotes/<int:notename_pk>',views.Classnotesdetail,name="classnotes"),
                path('classnoteslist',views.Classnoteslist,name="classnoteslists"),
                path('addhomework/',views.Addhomework),
                path('addhomeworklogin/',views.Addhomeworklogin),
                path('addclass/',views.Addclass),
                path('addclasslogin/',views.Addclasslogin),
                path('searchstudentid/',views.Searchstudent_id),
                path('answerstudent/',views.Selectstudent),
                path('zuotu/',views.multiChart),
                path('scerweima/',views.makeQrcode),
                path('ahw/',views.Addhomework2),


]
