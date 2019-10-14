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
                path('ahw/',views.Addhomework2),
                
                path('zyph/',views.Homeworkrank),
                path('zuotu1/',views.Zuotu1),
                path('zuotu2/',views.Zuotu2,name='zuotu2'),
                path('hwg/',views.homeworkg),
                # path('wx/',views.weixin_main,name='weixin_main'),
                path('tzccnu/',views.Addtxl),
               path('tzccnu22/', views.Addtxl2),
               path('txlyibu/', views.Addtxl22,name='txlyibu'),
               path('cs', views.CS),
               path('classnotes/',views.Classnewslist),
               path('jcgg/<int:idd>',views.Guoguan,name="guoguan"),
               path('addgg/',views.addguoguan),
               path('jcgglist/',views.guoguanlist),
               path('rankqa/',views.Rankq),
               path('rankqb/',views.RankqB),
               path('addrankq/',views.addrankq),
                path('addrankqb/',views.addrankqb),
                path('rankqpic/<int:iddd>',views.Guoguanpic),
               path('badhwms/', views.badhomeworkms),
               path('badhwms/<int:time0>', views.badhomeworkmsshow),
               path('addhwbad/', views.addhwbad),
               path('xiugaihwms/', views.xiugaihwms),
               path('homeworwbadmss/', views.badhomeworkms2),
               path('fangcheng/', views.FC),
               path('wktest/<int:id0>/<int:id1>', views.Showwkqs),
               path('yuxiname/<int:id0>/<int:id1>', views.yuxiname),
               path('addnames/<int:id0>/<int:id1>', views.Addnames),
               path('loginrecord/', views.Zuji),
               path('teacherms/', views.leavems),
               path('addteacherms/', views.addteacherms),
               path('jsq/', views.inputms),
               path('xxqs/', views.xxtest),
               path('xxtest/', views.xxtest2),
               path('getpic/', views.getpic),




               ]
