from django.shortcuts import render,redirect
from .models import Classes
from django.http import HttpResponse,JsonResponse
from .models import Classes,Courses,Homework,Exams,Students,Classnotes,onlinetestgrade,onlinetestlist,Questions,Scores
import json
import random
import numpy as np
from django.core import serializers
from django.contrib import auth

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
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    homeworkmessages = Homework.objects.filter(homeworkstudent__studentname=teststudent)
    return render(request,'homework.html',{'homeworkmessages':homeworkmessages})

    
      
def Exammessages(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    
    exammessages = Exams.objects.filter(examstudent__studentname=teststudent)
    return render(request,'exam.html',{'exammessages':exammessages}) 


def Daohang(request):
    return render(request,'index2.html')

def Onlinetestlogin(request):
    teststudent=request.session.get("teststudent")
    if  teststudent:
        return redirect('../indexs')


    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if not  pwd.isdigit():
            return render(request,'questionsindex.html',{'errors':'学号错误！'})


        teststudent=Students.objects.filter(studentname=user,studentid=pwd)

        if teststudent:
            request.session["teststudent"]=user
            return redirect('../indexs')
        else:
            return render(request,'questionsindex.html',{'errors':'姓名或学号错误，请重新输入！'})
      
    return render(request,'questionsindex.html')

def Indexs(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    classnotes=Classnotes.objects.all()

    return render(request,'base.html',{'classnotes':classnotes})
def Classnoteslist(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    classnotes=Classnotes.objects.all()
    return render(request,'classnoteslist.html',{'classnotes':classnotes})




def Logout(request):
    request.session.flush()
    return redirect("../")


def Learningnews(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    homeworkmessages = Homework.objects.filter(homeworkstudent__studentname=teststudent)
    exammessages = Exams.objects.filter(examstudent__studentname=teststudent)
    return render(request,'learningnews.html',{'homeworkmessages':homeworkmessages,'exammessages':exammessages})
def Classnotesdetail(request,notename_pk):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    classnotesdetail=Classnotes.objects.filter(id=notename_pk)
    return render(request,'classnotes.html',{'classnotesdetail':classnotesdetail})







    


    
    

    

def Showquestions(request):
    if request.method == 'GET':
        
        teststudent=request.session.get("teststudent")
        if not teststudent:
            return redirect('../testlogin')
        lengths=Questions.objects.all()
        n=len(lengths)
        
        listids=range(1,n)
        listidss=random.sample(listids,n-1)
        a=listidss[0]
        del listidss[0]

        showquestions = Questions.objects.filter(questionid=a)
        context = {'showquestions':showquestions,'score':0,'questionids':1,'listidss':listidss,'teststudent':teststudent,'correctamount':0,'testall':0,'scorelinshi':0}
        return render(request,'questions.html',context)
    if request.method == 'POST':
        questionanswer = request.POST.get('questionanswer')
        name = request.POST.get('studentname')
        scoreid = request.POST.get('questionlist')
        answer = request.POST.get('studentanswer')
        questionids = request.POST.get('questionids')
        questionids=int(questionids)
        score=request.POST.get('score')
        listidss=request.POST.get('listidss')
        timeover=request.POST.get('timeover')
        teststudent=request.POST.get('teststudent')
        correctamount=request.POST.get('correctamount')
        testall=request.POST.get('testall')
        scorelinshi = request.POST.get('scorelinshi')
        listidss=list(eval(listidss))#将html传来的‘list’字符串转化为list
        correctamount=int(correctamount)
        testall=int(testall)


        a=listidss[0]
        del listidss[0]

        


        if answer==questionanswer :
            score=int(score)+10
            correctamount=int(correctamount)+1
        else:
            pass

        #if questionids<9:
        if timeover=='':
            testall=int(testall)+1
            questionids+=1
            scorelinshi = int(float(score)*(correctamount/testall))
            showquestions = Questions.objects.filter(questionid=a)
            context = {'showquestions':showquestions,'score':score,'questionids':questionids,'listidss':listidss,'teststudent':teststudent,'correctamount':correctamount,'testall':testall,'scorelinshi':scorelinshi}
            return render(request,'questions.html',context)
        #elif questionids==9:
            #questionids+=1
            #showquestions = Questions.objects.filter(questionid=a)
            #context = {'showquestions':showquestions,'score':score,'questionids':questionids}
           # return render(request,'questions2.html',context)
        else:
            if testall==0:
                testall+=1
            correctpercent = correctamount/testall

            score=int(float(score)*(correctamount/testall))
            addscore = Scores.createscore(teststudent,score,scoreid,correctpercent,testall)

            showscoress=Scores.objects.filter(scoreid=scoreid)
            showscores=showscoress.order_by('-testscore')

            
            return render(request,'questions3.html',{'showscores':showscores,'score':score,'correctpercent':correctpercent,'testall':testall})

def Onlinetestrank(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    testrank=Scores.objects.all()
    testranks=testrank.order_by('-testscore')
    return render(request,'onlinetestrank.html',{'testranks':testranks})



def Testajax(request):
    return render(request,'test.html')


    

def ajax_handle(request):
    
    
    aaa=serializers.serialize("json",Students.objects.filter(pk=1))
    aaa=json.loads(aaa)
   
    
    return JsonResponse(aaa,safe=False)
    

            
        
            

            
        


    