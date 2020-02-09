from django.contrib import admin
from .models import Lasttime, Rankxhl, Xxqs22,Xxqs23,Xxqs24, Xxqs2,Wktestlimit0,Yuxiname0,Yuxitestcount0,Newnames0,Classnotes0,XHL,Classes,Courses,Homework,Exams,Students,Classnotes,onlinetestgrade,onlinetestlist,Questions,Scores,Searchstudentid,Loginrecord,Classingss,Homeworksum,TXL,guoguanname,guoguan,rankq,addrankqdetail,badhomework,Wkqs,Yuxiname,Newnames,Yuxitestcount,Leavems,Xxqs,Wkqs2,Wktestlimit,Testrm,Wkqs3,Wkqs4,Xxdata

# Register your models here.
@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
	list_display = ['pk','classname','teachername']

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
	list_display = ['pk','coursename']

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
	list_display = ['homeworktime','homeworkname','homeworkstudent','homeworkscore']
@admin.register(Classingss)
class ClassingssAdmin(admin.ModelAdmin):
	list_display = ['classtime','classname','classstudent','classscore']


@admin.register(Exams)
class ExamsAdmin(admin.ModelAdmin):
	list_display = ['examtime','examname','examstudent','examscore']

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
	list_display = ['pk','studentid','studentclass','studentname']

@admin.register(Classnotes)
class ClassnotesAdmin(admin.ModelAdmin):
	list_display = ['pk','notetime','notename','noteupdatetime','readed_num']
@admin.register(Classnotes0)
class Classnotes0Admin(admin.ModelAdmin):
	list_display = ['pk','notetime','notename','noteupdatetime','readed_num']

@admin.register(onlinetestgrade)
class onlinetestgradeAdmin(admin.ModelAdmin):
	list_display = ['pk','gradename']

@admin.register(onlinetestlist)
class onlinetestlistAdmin(admin.ModelAdmin):
	list_display = ['pk','listgrade','listname']

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
	list_display = ['questionid','questiongrade','questiontestlist','questiontext','questionanswer']

@admin.register(Wkqs)
class WkqsAdmin(admin.ModelAdmin):
	list_display = ['wrongcount','zid','jid','category','questiontext','questionanswer']
@admin.register(Wkqs2)
class Wkqs2Admin(admin.ModelAdmin):
	list_display = ['wrongcount','zid','jid','category','questiontext','questionanswer1','questionanswer2']

@admin.register(Wkqs3)
class Wkqs3Admin(admin.ModelAdmin):
	list_display = ['wrongcount','zid','jid','category','questiontext','questionanswer1','questionanswer2','questionanswer3']

@admin.register(Wkqs4)
class Wkqs4Admin(admin.ModelAdmin):
	list_display = ['questiontext','questionanswer1','questionanswer2','zid','jid']

@admin.register(Testrm)
class TestrmAdmin(admin.ModelAdmin):
	list_display = ['zid','jid','testrm']

@admin.register(Wktestlimit)
class WktestlimitAdmin(admin.ModelAdmin):
	list_display = ['zid','jid','limit','chances']

@admin.register(Wktestlimit0)
class Wktestlimit0Admin(admin.ModelAdmin):
	list_display = ['zid','jid','limit','chances']
@admin.register(Yuxiname)
class YuxinameAdmin(admin.ModelAdmin):
	list_display = ['zid','jid','name','time','ornot','count','costtime']

@admin.register(Yuxiname0)
class Yuxiname0Admin(admin.ModelAdmin):
	list_display = ['zid','jid','name','time','ornot','count','costtime']

@admin.register(Yuxitestcount)
class YuxitestcontAdmin(admin.ModelAdmin):
	list_display = ['zid','jid','name','time','count','seconds']

@admin.register(Yuxitestcount0)
class Yuxitestcont0Admin(admin.ModelAdmin):
	list_display = ['zid','jid','name','time','count','seconds']

@admin.register(Scores)
class ScoresAdmin(admin.ModelAdmin):
	list_display = ['scoreupdatetime','scoreid','scorename','testscore','correctpercent','testamount']

@admin.register(Searchstudentid)
class SearchstudentidAdmin(admin.ModelAdmin):
	list_display = ['phone','student','studentid']
@admin.register(Loginrecord)
class LogintimeAdmin(admin.ModelAdmin):
	list_display = ('lastlogintime','loginuser','logincount')

@admin.register(Homeworksum)
class HomeworksumAdmin(admin.ModelAdmin):
	list_display = ('pk','lasttime','student_name','aacount','acount','bcount','ccount','dcount','ecount','fcount')

@admin.register(TXL)
class TXLAdmin(admin.ModelAdmin):
	list_display = ('pk','addtime','name','company','major','gdtime','phone1','phone2')
@admin.register(guoguan)
class guoguanAdmin(admin.ModelAdmin):
	list_display = ('guoguan_name','student_name','ornot','time')
@admin.register(guoguanname)
class guoguannameAdmin(admin.ModelAdmin):
	list_display = ('idd','name')
@admin.register(rankq)
class rankqAdmin(admin.ModelAdmin):
	list_display = ('fenlei','student_name','score','time')

@admin.register(addrankqdetail)
class addrankqdetailAdmin(admin.ModelAdmin):
	list_display = ('name','detail','time')


@admin.register(badhomework)
class badhomeworkAdmin(admin.ModelAdmin):
	list_display = ('time0','name','stu_id','student_name','ornot','time')

@admin.register(Newnames)
class NewnamesAdmin(admin.ModelAdmin):
	list_display = ('zid','jid','name')

@admin.register(Newnames0)
class Newnames0Admin(admin.ModelAdmin):
	list_display = ('zid','jid','name')

@admin.register(Leavems)
class LeavemsAdmin(admin.ModelAdmin):
	list_display = ('name','time','category','ornot','text')

@admin.register(Xxqs)
class XxqsAdmin(admin.ModelAdmin):
	list_display = ('id1','id2','num0','num1','yunsuan','answer','ornot')

@admin.register(Xxqs2)
class Xxqs2Admin(admin.ModelAdmin):
	list_display = ('pk','num0','num1','yunsuan','answer','ornot')

@admin.register(Xxqs22)
class Xxqs22Admin(admin.ModelAdmin):
	list_display = ('pk','num0','num1','yunsuan','answer','ornot')

@admin.register(Xxqs23)
class Xxqs23Admin(admin.ModelAdmin):
	list_display = ('pk','num0','num1','yunsuan','answer','ornot')

@admin.register(Xxqs24)
class Xxqs24Admin(admin.ModelAdmin):
	list_display = ('pk','num0','num1','yunsuan','answer','ornot')

@admin.register(Xxdata)
class XxdataAdmin(admin.ModelAdmin):
	list_display = ('category','name','kaoqin','kaohui','shijia','bingjia','hunjia','sangjia','chanjia','hulijia','summ')

@admin.register(XHL)
class XHLAdmin(admin.ModelAdmin):
	list_display = ('pk','classs','name','phone','addtime')

@admin.register(Rankxhl)
class RankxhlAdmin(admin.ModelAdmin):
	list_display = ('pk','name','costtime','time')

@admin.register(Lasttime)
class LasttimeAdmin(admin.ModelAdmin):
	list_display = ('pk','name','costtime','time')