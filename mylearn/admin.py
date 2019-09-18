from django.contrib import admin
from .models import Classes,Courses,Homework,Exams,Students,Classnotes,onlinetestgrade,onlinetestlist,Questions,Scores,Searchstudentid,Loginrecord,Classingss,Homeworksum,TXL,guoguanname,guoguan,rankq,addrankqdetail

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

@admin.register(onlinetestgrade)
class ClassnotesAdmin(admin.ModelAdmin):
	list_display = ['pk','gradename']

@admin.register(onlinetestlist)
class ClassnotesAdmin(admin.ModelAdmin):
	list_display = ['pk','listgrade','listname']

@admin.register(Questions)
class ClassnotesAdmin(admin.ModelAdmin):
	list_display = ['questionid','questiongrade','questiontestlist','questiontext','questionanswer']

@admin.register(Scores)
class ClassnotesAdmin(admin.ModelAdmin):
	list_display = ['scoreupdatetime','scoreid','scorename','testscore','correctpercent','testamount']

@admin.register(Searchstudentid)
class ClassnotesAdmin(admin.ModelAdmin):
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

	
