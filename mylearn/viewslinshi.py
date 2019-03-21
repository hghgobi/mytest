from django.shortcuts import render
from .models import Classes
from django.http import HttpResponse
from .models import Classes,Courses,Homework,Exams,Students,Classnotes,onlinetestgrade,onlinetestlist,Questions,Scores
import json

# Create your views here.
def addclasses(request):
    if request.method =='POST':
        name = request.POST.get('name')
        teach = request.POST.get('teach')
        addclass=Classes.createClass(name,teach)
        classlist=Classes.objects.all()
        return render(request,'index.html',{"classlist":classlist})
    elif request.method =='GET':
        classlist=Classes.objects.all()
        return render(request,'index.html',{"classlist":classlist})


def Homeworkmessages(request):
    if request.method =='POST':
        name = request.POST.get('name')
        
        homeworkmessages = Homework.objects.filter(homeworkstudent__studentname=name)
        if homeworkmessages:
            return render(request,'homework.html',{"homeworkmessages":homeworkmessages})
        else :
            return render(request,'homework3.html')

        
    elif request.method =='GET':
        
        return render(request,'homework2.html')
        
      
def Exammessages(request):
    if request.method =='POST':
        name = request.POST.get('name')
        
        exammessages = Exams.objects.filter(examstudent__studentname=name)
        if exammessages:
            return render(request,'exam.html',{"exammessages":exammessages})
        else:
            return render(request,'exam3.html')
   
    elif request.method =='GET':
        
        return render(request,'exam2.html')    
def Daohang(request):
    return render(request,'index2.html')


def Showquestions(request):
    if request.method == 'GET':
        
        showquestions = Questions.objects.filter(questionid=1)
        context = {'showquestions':showquestions,'score':0}
        return render(request,'questions.html',context)
    if request.method == 'POST':
        questionanswer = request.POST.get('questionanswer')
        name = request.POST.get('studentname')
        scoreid = request.POST.get('questionlist')
        answer = request.POST.get('studentanswer')
        questionid = request.POST.get('questionid')
        questionid=int(questionid)
        score=request.POST.get('score')
        if answer==questionanswer :
            score=int(score)+10
        else:
            pass
        if questionid<9:
            questionid+=1
            showquestions = Questions.objects.filter(questionid=questionid)
            context = {'showquestions':showquestions,'score':score}
            return render(request,'questions.html',context)
        elif questionid==9:
            questionid+=1
            showquestions = Questions.objects.filter(questionid=questionid)
            context = {'showquestions':showquestions,'score':score}
            return render(request,'questions2.html',context)
        else:
            
            addscore = Scores.createscore(name,score,scoreid)

            showscoress=Scores.objects.filter(scoreid=scoreid)
            showscores=showscoress.order_by('-testscore')

            
            return render(request,'questions3.html',{'showscores':showscores,'score':score})


    

            
        
            
def ajax_handle(request):
    dd=9999999999
    name=request.POST.get('name')
    aaa=serializers.serialize("json",Students.objects.all())
    aaa=json.loads(aaa)
    
    return JsonResponse({"aaa":aaa},safe=False)
            
        


    