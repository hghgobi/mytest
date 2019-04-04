from django.contrib import admin
from .models import Classes,Courses,Homework,Exams,Students,Classnotes,onlinetestgrade,onlinetestlist,Questions,Scores,Searchstudentid
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


@admin.register(Exams)
class ExamsAdmin(admin.ModelAdmin):
	list_display = ['examtime','examname','examstudent','examscore']

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
	list_display = ['studentid','studentclass','studentname']

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
	
