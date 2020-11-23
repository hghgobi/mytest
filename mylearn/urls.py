from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [path('homework/',views.Homeworkmessages),
               path('class/',views.Classmessages),
                path('exam/',views.Exammessages),
                # path('',views.Onlinetestlogin),
                #path('test/rank/',views.Showscores),
                path('logout/',views.Logout),
                path('onlinetest/',views.Showquestions),
                path('ajax_handle/',views.ajax_handle),
                path('test/',views.Testajax),
                path('testlogin/',views.Onlinetestlogin),
               path('login/', views.Login0,name="login"),
               path('testlogin0/', views.Onlinetestlogin0),
               path('testlogin1/', views.Datilogin,name='testlogin1'),
                path('',views.Indexs),
                path('indexs0/',views.Indexs0),
                path('learningnews/',views.Learningnews),
                path('onlinetestrank/',views.Onlinetestrank),
               path('classnotes/<int:notename_pk>', views.Classnotesdetail, name="classnotes"),
                path('classnotes0/<int:notename_pk>',views.Classnotesdetail0,name="classnotes0"),
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
               path('xhlyibu/', views.Addxhl0,name='xhlyibu'),
               path('xhlzc/', views.Addxhl2),
               path('txlyibu/', views.Addtxl2,name='txlyibu'),
               path('dt/', views.Datiget),
               path('dtp/', views.Datipost, name='dtp'),
               path('dtmanage/', views.Datimanage),
               path('dtcount/', views.Daticount, name='dtcount'),
               path('dtstart/', views.Datistart, name='dtstart'),
               path('dtend/', views.Datiend, name='dtend'),
              path('dttongji/', views.Datitongji, name='dttongji'),
               path('cs', views.CS),
               path('classnotes/',views.Classnewslist,name="classnotes"),
               path('classnotes0/', views.Classnewslist0, name="classnotes0"),
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
               path('fangcheng2/', views.FC2),
               path('wktest/<int:id0>/<int:id1>', views.Showwkqs1),
               path('zkfx/<int:id0>/<int:id1>', views.zkfx),
               path('zkfxname/', views.zkfxname),
               path('wktest1/<int:id0>/<int:id1>', views.Showwkqs2),
               path('wktest2/<int:id0>/<int:id1>', views.Showwkqs3),
               path('jiefc/<int:id0>/<int:id1>', views.Jfc),
               #path('xhltest1/<int:id0>/<int:id1>', views.Jfc0),
             path('wktest/', views.Testresult,name="wktest"),
              path('zkfxnametg/<int:id0>/<int:id1>/<int:bj>', views.zkfxnametg),

               path('wrong/', views.showqserror,name="wrong"),
               path('yuxiname/<int:id0>/<int:id1>', views.yuxiname),
               path('yuxiname0/<int:id0>/<int:id1>', views.yuxiname0),
               path('addnames/<int:id0>/<int:id1>', views.Addnames),
               path('addnames0/<int:id0>/<int:id1>', views.Addnames0),
               path('loginrecord/', views.Zuji),
               path('teacherms/', views.leavems),
               path('addteacherms/', views.addteacherms),
               path('jsq/', views.inputms),
               path('xxqs/', views.xxtest),
               path('xxtest/<int:id0>/<int:id1>', views.xxtest2),
               path('xxtest2/<int:id0>/<int:id1>', views.xxtest22),
               path('getpic/', views.getpic),
               path('Xx/', views.Xxdatasearch),
               path('addqs/<int:yunsuan>', views.addqs2),
               path('ranktest/', views.xxtest23),
               path('ranktestresults/', views.rankmss),
               path('addqs/<int:yunsuan>', views.addqs2),
               path('111/', views.Xhltestms),
               path('kz/<int:code>', views.Kz),
               path('kzgetms/', views.Kzgetms),
               path('kzgeturl/<int:id0>', views.Kzurl),
               path('kz666/', views.Kzurl2),
               path('killcuoti/', views.Killcuoti),
               path('pxr/', views.rankpaixu),
               path('flower/', views.Showflowerms),
               path('flower2/', views.Showflowerms2),
               path('addflower/', views.Addflowers),
               path('rankget/<int:id0>/<int:id1>/<int:bj>', views.Rankget),
               path('hwmanage/', views.Hwmanage),
               path('<int:time>', views.Hwshow),
               path('<int:time>/<int:stuid>', views.Hwchange),
               path('hwadd/<int:time>/<int:clas>', views.Hwaddnames),
               path('gethwms/', views.Gethwms),





               ]
