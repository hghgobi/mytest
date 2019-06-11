from django.shortcuts import render,redirect,get_object_or_404
from .models import Classes
from django.http import HttpResponse,JsonResponse
from .models import Classes,Courses,Homework,Exams,Students,Classnotes,onlinetestgrade,onlinetestlist,Questions,Scores,Searchstudentid,Loginrecord,Classingss,Homeworksum
import json
import random
import numpy as np
from django.core import serializers
from django.contrib import auth
from django.core.paginator import Paginator

from django.contrib.contenttypes.models import ContentType
from comment.models import Comment



from matplotlib.figure import Figure                      
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt

import  datetime

import base64
from io import BytesIO

import mpl_toolkits.axisartist as axisartist
import matplotlib
import math
import time
from django.db.models import Q


import hashlib
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt


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

#coding:utf-8
def Homeworkmessages1(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    homeworkmessages = Homework.objects.filter(homeworkstudent__studentname=teststudent)
    homeworkmessagesum = Homeworksum.objects.filter(student_name__studentname=teststudent)
    summ=len(homeworkmessages)
    sl=[0,0,0,0,0,0,0]
    for i in range(summ) :
        if homeworkmessages[i].homeworkscore=='A+ 很认真' or homeworkmessages[i].homeworkscore=='A+很认真':
            sl[0]+=1
        if homeworkmessages[i].homeworkscore=='A':
            sl[1]+=1
        if homeworkmessages[i].homeworkscore=='B':
            sl[2]+=1
        if homeworkmessages[i].homeworkscore=='C':
            sl[3]+=1
        if homeworkmessages[i].homeworkscore=='D':
            sl[4]+=1
        if homeworkmessages[i].homeworkscore=='作业没交':
            sl[5]+=1
        if homeworkmessages[i].homeworkscore=='作业不认真乱写':
            sl[6]+=1

   
    plt.switch_backend('agg')
    plt.figure(figsize=(3.6,3.6))

    matplotlib.rcParams['font.sans-serif'] = ["SimHei"]
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.barh(range(7), sl, height=0.7, color=['b','g','r','c','y','k','m'], alpha=0.8)
    plt.yticks(range(7), ['A+','A','B','C','D','没交','乱写'])
    plt.xlim(0,50)
    plt.xlabel("累计次数")
    plt.title("作业总体情况")
    for x, y in enumerate(sl):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    sio=BytesIO()
    plt.savefig(sio,format='png')
    data=base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}"/> '''
    plt.close()
    imd=html.format(data)


    return render(request,'homework.html',{'homeworkmessages':homeworkmessages,'homeworkmessagesum':homeworkmessagesum,'imd':imd})


def Homeworkmessages(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    homeworkmessages = Homework.objects.filter(homeworkstudent__studentname=teststudent)
    homeworkmessagesum = Homeworksum.objects.filter(student_name__studentname=teststudent)

    sl=[]
    sl.append(homeworkmessagesum[0].aacount)
    sl.append(homeworkmessagesum[0].acount)
    sl.append(homeworkmessagesum[0].bcount)
    sl.append(homeworkmessagesum[0].ccount)
    sl.append(homeworkmessagesum[0].dcount)
    sl.append(homeworkmessagesum[0].ecount)
    sl.append(homeworkmessagesum[0].fcount)

    plt.switch_backend('agg')
    plt.figure(figsize=(3.6, 3.6))

    matplotlib.rcParams['font.sans-serif'] = ["SimHei"]
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.barh(range(7), sl, height=0.7, color=['b', 'g', 'r', 'c', 'y', 'k', 'm'], alpha=0.8)
    plt.yticks(range(7), ['A+', 'A', 'B', 'C', 'D', '没交', '乱写'])
    plt.xlim(0, 50)
    plt.xlabel("累计次数")
    plt.title("作业总体情况")
    for x, y in enumerate(sl):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}"/> '''
    plt.close()
    imd = html.format(data)

    return render(request, 'homework.html',
                  {'homeworkmessages': homeworkmessages, 'homeworkmessagesum': homeworkmessagesum, 'imd': imd})
def Homeworkrank(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')

    msag=Homeworksum.objects.all()
    summ=len(msag)
    rank={}
    
    for a in range(summ):
        rank[msag[a].student_name]=msag[a].aacount

    rank=sorted(rank.items(), key=lambda e:e[1], reverse=False)

    scores=[]
    names=[]
    for i in rank:
        names.append(i[0])
        scores.append(i[1])
    scores=scores[40:]
    names=names[40:]


    plt.switch_backend('agg')
    plt.figure(figsize=(4,13))

    matplotlib.rcParams['font.sans-serif'] = ["SimHei"]
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.barh(range(len(scores)), scores, height=0.7, color='r', alpha=0.8)
    plt.yticks(range(len(scores)), names)
    plt.xlabel("累计次数")
    plt.title("作业A+排行榜")
    for x, y in enumerate(scores):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    sio=BytesIO()
    plt.savefig(sio,format='png')
    data=base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}"/> '''
    plt.close()
    imd=html.format(data)

    rank1={}
    
    for a1 in range(summ):
        rank1[msag[a1].student_name]=msag[a1].acount

    rank1=sorted(rank1.items(), key=lambda e:e[1], reverse=False)

    scores1=[]
    names1=[]
    for i1 in rank1:
        names1.append(i1[0])
        scores1.append(i1[1])
    scores1=scores1[17:]
    names1=names1[17:]


    plt.switch_backend('agg')
    plt.figure(figsize=(4,16))

    matplotlib.rcParams['font.sans-serif'] = ["SimHei"]
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.barh(range(len(scores1)), scores1, height=0.7, color='b', alpha=0.8)
    plt.yticks(range(len(scores1)), names1)
    plt.xlabel("累计次数")
    plt.title("作业A排行榜")
    for x1, y1 in enumerate(scores1):
        plt.text(y1 + 0.2, x1 - 0.1, '%s' % y1)
    sio1=BytesIO()
    plt.savefig(sio1,format='png')
    data1=base64.encodebytes(sio1.getvalue()).decode()
    html1 = ''' <img src="data:image/png;base64,{}"/> '''
    plt.close()
    imdd=html1.format(data1)


    # stlist=[6,20,16,1,32,27,9,19,22,5,3,10,17,15,12,14,2,4,31,13,18,24,25,11,8,7,56,60,54,70,53,68,63,66,58,77,67,47,52,71,65,48,61,59,64,49,51,50,78,55,62,23,28,75,57,72,73,82,69,81,26]
    # examranks={}
    # for i in stlist :
    #     stname = Students.objects.filter(pk=i)
    #     name=stname[0].studentname
    #     examrank=Exams.objects.filter(examstudent__studentname=name)
    #     sunns=len(examrank)
    #     scoresss=0
    #     for i in range(sunns):
    #         scoresss+=int(examrank[i].examscore)
    #     examranks[name]=int(scoresss/sunns)
    # examranks=sorted(examranks.items(), key=lambda e:e[1], reverse=False)
    #
    # scores3=[]
    # names3=[]
    # for iii in examranks:
    #     names3.append(iii[0])
    #     scores3.append(iii[1])
    # scores3=scores3[20:]
    # names3=names3[20:]
    #
    #
    # plt.switch_backend('agg')
    # plt.figure(figsize=(4,13))
    #
    # matplotlib.rcParams['font.sans-serif'] = ["SimHei"]
    # matplotlib.rcParams['axes.unicode_minus'] = False
    # plt.barh(range(len(scores3)), scores3, height=0.7, color='b', alpha=0.8)
    # plt.yticks(range(len(scores3)), names3)
    # plt.xlabel("平均分")
    # plt.title("考试平均分排行榜")
    # for x3, y3 in enumerate(scores3):
    #     plt.text(y3 + 0.2, x3 - 0.1, '%s' % y3)
    # sio3=BytesIO()
    # plt.savefig(sio3,format='png')
    # data3=base64.encodebytes(sio3.getvalue()).decode()
    # html3 = ''' <img src="data:image/png;base64,{}"/> '''
    # plt.close()
    # imd3=html3.format(data3)


    return render(request,'zuoyepaihang.html',{'imd':imd,'imdd':imdd})

        

def Classmessages(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    classmessages = Classingss.objects.filter(classstudent__studentname=teststudent)
    return render(request,'class.html',{'classmessages':classmessages})

    
      
def Exammessages(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    
    exammessages = Exams.objects.filter(examstudent__studentname=teststudent)
    sunn=len(exammessages)
    dates,scores=[],[]
    for i in range(sunn):
        
        #date=datetime.strptime(exammessages[i].examtime,'"%Y.%m.%d"')
        dates.append(exammessages[i].examtime)
        scores.append(exammessages[i].examscore)
    dates.reverse()
    scores.reverse()
    plt.switch_backend('agg')
    fig=plt.figure(figsize=(3.8,3.8))

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.plot(dates,scores,c='red')
    plt.title("总体情况")
    fig.autofmt_xdate()
    plt.ylim(0,120)

    plt.ylabel("分数")
    plt.tick_params(axis='both',which='major',labelsize=8)
    sio=BytesIO()
        
    plt.savefig(sio,format='png')
    data=base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}"/> '''
    plt.close()
    imd=html.format(data)

  

    return render(request,'exam.html',{'exammessages':exammessages,'imd':imd}) 


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
def Searchstudent_id(request):
    if request.method =='GET':
        return render(request,'searchstudentid.html')
    if request.method =='POST':
        phone = request.POST.get('phone')
        if not  phone.isdigit():
            return render(request,'searchstudentid.html',{'errorss':'信息不存在或手机号输错！请重新输入！'})

        
        studentids= Searchstudentid.objects.filter(phone=phone)
        if studentids :
            return render(request,'searchstudentid.html',{'studentids':studentids})
        else:
            errorss='信息不存在或手机号输错！请重新输入！'
            return render(request,'searchstudentid.html',{'errorss':errorss})
        


def Indexs(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    loginrecord=get_object_or_404(Loginrecord,loginuser=teststudent)

    loginrecord.logincount =int(loginrecord.logincount)+1
    loginrecord.save()
    notes_all_list = Classnotes.objects.all()
    paginator = Paginator(notes_all_list,6)
    page_num = request.GET.get('page',1)
    page_of_notes = paginator.get_page(page_num)
    currentr_page_num = page_of_notes.number
    page_range = list(range(max(currentr_page_num - 2,1),currentr_page_num)) + \
                 list(range(currentr_page_num,min(currentr_page_num + 2,paginator.num_pages)+1))

    return render(request,'base.html',{'page_of_notes':page_of_notes,'page_range':page_range})
def Classnoteslist(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    
    notes_all_list = Classnotes.objects.all()
    paginator = Paginator(notes_all_list,6)
    page_num = request.GET.get('page',1)
    page_of_notes = paginator.get_page(page_num)

    return render(request,'classnoteslist.html',{'page_of_notes':page_of_notes})




def Logout(request):
    request.session.flush()
    return redirect("../")


def Learningnews(request):
    teststudent=request.session.get("teststudent")
    user=teststudent
    if not teststudent:
        return redirect('../testlogin')
    homeworkmessages = Homework.objects.filter(homeworkstudent__studentname=teststudent)
    exammessages = Exams.objects.filter(examstudent__studentname=teststudent)
    return render(request,'learningnews.html',{'homeworkmessages':homeworkmessages,'exammessages':exammessages})
def Classnotesdetail(request,notename_pk):
    teststudent=request.session.get("teststudent")
    notename_pk=notename_pk
    user=teststudent
    if not teststudent:
        return redirect('../testlogin')
    classnotesdetail=Classnotes.objects.filter(id=notename_pk)
    classnotes=get_object_or_404(Classnotes,id=notename_pk)
   
    classnotes.readed_num += 1
    classnotes.save()

    notes_content_type = ContentType.objects.get_for_model(classnotes)
    comments = Comment.objects.filter(content_type=notes_content_type, object_id=notename_pk)
  
    response = render(request,'classnotes.html',{'classnotesdetail':classnotesdetail,'comments':comments,'user':user,'notename_pk':notename_pk})
   
    return response







    


    
    

    

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

def Addhomeworklogin(request):
    addhomeworkadmin=request.session.get("addhomeworkadmin")
    if  addhomeworkadmin:
        return redirect('../addhomework')


    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        addhomeworkadmin=Students.objects.filter(studentname=user,studentid=pwd)

        if addhomeworkadmin:
            request.session["addhomeworkadmin"]=user
            return redirect('../addhomework')
        else:
            return render(request,'addhomeworkindex.html',{'errors':'错误，请重新输入！'})
      
    return render(request,'addhomeworkindex.html')
def Addhomework(request):
    addhomeworkadmin=request.session.get("addhomeworkadmin")
    if not addhomeworkadmin:
        return redirect('../addhomeworklogin')
    if request.method == 'GET':
        return render(request,'addhomework.html')
        


    idd=request.POST.get('idd')
    idd=int(idd)
    score=request.POST.get('score')
    namesss=Students.objects.filter(pk=idd)
    namessss=namesss[0]

    homeworksum=get_object_or_404(Homeworksum,student_name=namessss)
    if score == 'A+':
        homeworksum.aacount=int(homeworksum.aacount)+1
    elif score == 'A':
        homeworksum.acount=int(homeworksum.acount)+1
    elif score == 'B':
        homeworksum.bcount=int(homeworksum.bcount)+1
    elif score == 'C':
        homeworksum.ccount=int(homeworksum.ccount)+1
    elif score == 'D':
        homeworksum.dcount=int(homeworksum.dcount)+1
    elif score == '作业不认真乱写':
        homeworksum.ecount=int(homeworksum.ecount)+1
    elif score == '作业没交':
        homeworksum.fcount=int(homeworksum.fcount)+1
    homeworksum.save()

    homeworkname='作业'
    Homework.createhomework(idd,score,homeworkname)
    return render(request,'addhomework.html')
def Addclasslogin(request):
    addclassadmin=request.session.get("addclassadmin")
    if  addclassadmin:
        return redirect('../addclass')


    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        addclassadmin=Students.objects.filter(studentname=user,studentid=pwd)

        if addclassadmin:
            request.session["addclassadmin"]=user
            return redirect('../addclass')
        else:
            return render(request,'addclassindex.html',{'errors':'错误，请重新输入！'})
      
    return render(request,'addclassindex.html')

def Addclass(request):
    addclassadmin=request.session.get("addclassadmin")
    if not addclassadmin:
        return redirect('../addclasslogin')
    if request.method == 'GET':
        return render(request,'addclass.html')
        


    idd=request.POST.get('idd')
    idd=int(idd)
    score=request.POST.get('score')
    classname='课堂情况'
    Classingss.createclass(idd,score,classname)
    return render(request,'addclass.html')


def Selectstudent(request):
    if request.method == 'GET':
        return render(request,'answerstudent.html')
        
    else :
        ab = request.POST.get('student')
        if ab=='A':
            studentlista=[72,57,75,23,28,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,25,27,31,32,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,63,64,65,66,67,68,70,71,77,78]
        if ab=='AA':
            studentlista=[6,8,1,10,49,3,17,9,20,52,11,2,16,19,70,4,58,47,53]

        if ab=='B':
            studentlista=[21,26,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,69,73,74,76,79,80,81,82,83,84,86,87,88,89,90]
        if ab=='BB':
            studentlista=[82,30,73,35,26,37,69,36,34,33,29,21,81,38,87]


        n=len(studentlista)

        liststudent=random.sample(studentlista,n)
        liststudent=random.sample(liststudent,n)

        idd=liststudent[0]
        idd=int(idd)
        answerstudent=Students.objects.filter(pk=idd)
        return render(request,'answerstudent.html',{'answerstudent':answerstudent})
        
        

def Testajax(request):
    return render(request,'test.html')


    

def ajax_handle(request):
    
    
    aaa=serializers.serialize("json",Students.objects.filter(pk=1))
    aaa=json.loads(aaa)
   
    
    return JsonResponse(aaa,safe=False)
 
def Addhomework2(request):
    
    idd=request.POST.get('idd')
    idd=int(idd)
    score=request.POST.get('score')
    namesss=Students.objects.filter(pk=idd)
    namessss=namesss[0]

    homeworksum=get_object_or_404(Homeworksum,student_name=namessss)
    if score == 'A+':
        homeworksum.aacount=int(homeworksum.aacount)+1
    elif score == 'A':
        homeworksum.acount=int(homeworksum.acount)+1
    elif score == 'B':
        homeworksum.bcount=int(homeworksum.bcount)+1
    elif score == 'C':
        homeworksum.ccount=int(homeworksum.ccount)+1
    elif score == 'D':
        homeworksum.dcount=int(homeworksum.dcount)+1
    elif score == '作业不认真乱写':
        homeworksum.ecount=int(homeworksum.ecount)+1
    elif score == '作业没交':
        homeworksum.fcount=int(homeworksum.fcount)+1
    homeworksum.save()

    homeworkname='作业'
    Homework.createhomework(idd,score,homeworkname) 
    return HttpResponse('成功！')





def Zuotu2(request):
    userr='作图网站登录次数'

    loginrecord=get_object_or_404(Loginrecord,loginuser=userr)

    loginrecord.logincount =int(loginrecord.logincount)+1
    loginrecord.save()

    k=request.POST.get('k')
    b=request.POST.get('b')
    aa=request.POST.get('aa')
    bb=request.POST.get('bb')
    cc=request.POST.get('cc')
    kk=request.POST.get('kk')
    xz1=request.POST.get('xz1')
    xz2=request.POST.get('xz2')
    xz3=request.POST.get('xz3')
    xx1=request.POST.get('xx1')
    xx2=request.POST.get('xx2')
    xx3=request.POST.get('xx3')

    data = {}
    
      
       
    if xz1=='1'and xz2=='2' and xz3=='3' :
        data['message'] = '不能同时画3种函数图象'
        data['status']="errors"
        return JsonResponse(data)


    elif xz1=='1'and xz2=='2' :
       

        if k and b and aa and bb and cc:
            k=float(k)
            b=float(b)
            aa=float(aa)
            bb=float(bb)
            cc=float(cc)
            c=abs(k)+abs(b)
            plt.switch_backend('agg')
            fig=plt.figure(figsize=(3.5,3.8))
            ax=axisartist.Subplot(fig,111)
            fig.add_axes(ax)
            #ax.axis["bottom"]=ax.new_floating_axis(0,0)
            #ax.axis["left"]=ax.new_floating_axis(1,0)
            ax.axis["bottom"].set_axisline_style("-|>",size=1.5)
            ax.axis["left"].set_axisline_style("->",size=1.5)
            #ax.axis["top"].set_visible(False)
            #ax.axis["right"].set_visible(False)
            plt.grid()
            if xx1 and xx2 and xx3:
                xx1=float(xx1)
                xx2=float(xx2)
                xx3=float(xx3)
                x_values=np.arange(xx1,xx2,xx3)
            elif xx1 and xx2 :
                xx1=float(xx1)
                xx2=float(xx2)
                x_values=np.arange(xx1,xx2,0.2)
            elif xx3:
               
                xx3=float(xx3)
                x_values=np.arange(-c,c,xx3)

            else:
                x_values=np.arange(-c,c,0.1)
            y_values=[x*k+b for x in x_values]
            y_values1=[aa*pow(x,2)+bb*x+cc for x in x_values]
            

            plt.plot(x_values,y_values,color='m')
            plt.plot(x_values,y_values1,color='r')
            

            sio=BytesIO()
            plt.savefig(sio,format='png')
            dat=base64.encodebytes(sio.getvalue()).decode()
            html = ''' <img src="data:image/png;base64,{}"/> '''
            plt.close()
            imd=html.format(dat)
            data['imd'] =imd
            data['status']="SUCCESS"
        else:
            data['message'] = '输入类型错误！'
            data['status']="errors"

        return JsonResponse(data)

            

    elif xz1=='1'and xz3=='3' :
        if aa == '' or bb=='' or cc=='' or kk=='':
            data['message'] = '输入类型错误(不能留空，可用0代替）！'
            data['status']="errors"
        else:
            k=float(k)
            b=float(b)
            kk=float(kk)
            dd=abs(k)+abs(b)
            plt.switch_backend('agg')
            fig=plt.figure(figsize=(3.5,5))
            ax=axisartist.Subplot(fig,111)
            fig.add_axes(ax)
            #ax.axis["bottom"]=ax.new_floating_axis(0,0)
            #ax.axis["left"]=ax.new_floating_axis(1,0)
            ax.axis["bottom"].set_axisline_style("-|>",size=1.5)
            ax.axis["left"].set_axisline_style("->",size=1.5)
            #ax.axis["top"].set_visible(False)
            #ax.axis["right"].set_visible(False)
            plt.grid()
            if xx1 and xx2 and xx3:
                xx1=float(xx1)
                xx2=float(xx2)
                xx3=float(xx3)
                x_values=np.arange(xx1,xx2,xx3)
            if xx1 and xx2 :
                xx1=float(xx1)
                xx2=float(xx2)
                x_values=np.arange(xx1,xx2,0.2)
            if xx3:
               
                xx3=float(xx3)
                x_values=np.arange(-dd,dd,xx3)

            else:
                x_values=np.arange(-dd,dd,0.1)

                
            y_values=[x*k+b for x in x_values]
            
            y_values1=[kk/x for x in x_values]

            plt.plot(x_values,y_values,color='b')
            plt.plot(x_values,y_values1,color='r')
            sio=BytesIO()
            plt.savefig(sio,format='png')
            dat=base64.encodebytes(sio.getvalue()).decode()
            html = ''' <img src="data:image/png;base64,{}"/> '''
            plt.close()
            imd=html.format(dat)
            data['imd'] =imd
            data['status']="SUCCESS"
        return JsonResponse(data)
            

    elif xz2=='2' and xz3=='3':
        if kk == '' or aa=='' or bb=='' or cc=='':
            data['message'] = '输入类型错误！'
            data['status']="errors"
        else:
            kk=float(kk)
            aa=float(aa)
            bb=float(bb)
            cc=float(cc)
            
            ee=abs(5*kk)
            plt.switch_backend('agg')
            fig=plt.figure(figsize=(3.5,3.8))
            ax=axisartist.Subplot(fig,111)
            fig.add_axes(ax)
            #ax.axis["bottom"]=ax.new_floating_axis(0,0)
            #ax.axis["left"]=ax.new_floating_axis(1,0)
            ax.axis["bottom"].set_axisline_style("-|>",size=1.5)
            ax.axis["left"].set_axisline_style("->",size=1.5)
            #ax.axis["top"].set_visible(False)
            #ax.axis["right"].set_visible(False)
            plt.grid()
            if xx1 and xx2 and xx3:
                xx1=float(xx1)
                xx2=float(xx2)
                xx3=float(xx3)
                x_values=np.arange(xx1,xx2,xx3)
            elif xx1 and xx2 :
                xx1=float(xx1)
                xx2=float(xx2)
                x_values=np.arange(xx1,xx2,0.2)
            elif xx3:
               
                xx3=float(xx3)
                x_values=np.arange(-ee,ee,xx3)

            else:
                x_values=np.arange(-ee,ee,0.1)



            y_values=[kk/x for x in x_values]
            y_values1=[aa*pow(x,2)+bb*x+cc for x in x_values]

            plt.plot(x_values,y_values,'r',x_values,y_values1,'b')
            #plt.plot(x_values,y_values1,color='b')
            sio=BytesIO()
            plt.savefig(sio,format='png')
            dat=base64.encodebytes(sio.getvalue()).decode()
            html = ''' <img src="data:image/png;base64,{}"/> '''
            plt.close()
            imd=html.format(dat)
            data['imd'] =imd
            data['status']="SUCCESS"
        return JsonResponse(data)
           

    elif xz1=='1':
        if k == '' or b=='':
            data['message'] = '输入类型错误！'
            data['status']="errors"
        else:
            k=float(k)
            b=float(b)
           
            c=abs(k)+abs(b)
            plt.switch_backend('agg')
            fig=plt.figure(figsize=(3.5,3.8))
            ax=axisartist.Subplot(fig,111)
            fig.add_axes(ax)
            #ax.axis["bottom"]=ax.new_floating_axis(0,0)
            #ax.axis["left"]=ax.new_floating_axis(1,0)
            ax.axis["bottom"].set_axisline_style("-|>",size=1.5)
            ax.axis["left"].set_axisline_style("->",size=1.5)
            #ax.axis["top"].set_visible(False)
            #ax.axis["right"].set_visible(False)
            plt.grid()
            if xx1 and xx2 :
                xx1=float(xx1)
                xx2=float(xx2)
                if xx3 :
                    xx3=float(xx3)
                    x_values=np.arange(xx1,xx2,xx3)
                else:
                    x_values=np.arange(xx1,xx2,0.2) 
            
            elif xx3:
               
                xx3=float(xx3)
                x_values=np.arange(-c,c,xx3)

            else:
                x_values=np.arange(-c,c,0.1)

            y_values=[x*k+b for x in x_values]
            
            

            plt.plot(x_values,y_values,color='m')
            
            

            sio=BytesIO()
            plt.savefig(sio,format='png')
            dat=base64.encodebytes(sio.getvalue()).decode()
            html = ''' <img src="data:image/png;base64,{}"/> '''
            plt.close()
            imd=html.format(dat)
            data['imd'] =imd
            data['status']="SUCCESS"
        return JsonResponse(data)
            

    elif xz3=='3' :
        if  kk=='':
            data['message'] = '输入类型错误(不能留空，可用0代替）！'
            data['status']="errors"
        else:
           
            kk=float(kk)
            dd=abs(kk)*10
            plt.switch_backend('agg')
            fig=plt.figure(figsize=(3.5,5))
            ax=axisartist.Subplot(fig,111)
            fig.add_axes(ax)
            #ax.axis["bottom"]=ax.new_floating_axis(0,0)
            #ax.axis["left"]=ax.new_floating_axis(1,0)
            ax.axis["bottom"].set_axisline_style("-|>",size=1.5)
            ax.axis["left"].set_axisline_style("->",size=1.5)
            #ax.axis["top"].set_visible(False)
            #ax.axis["right"].set_visible(False)
            plt.grid()
            if xx1 and xx2 and xx3:
                xx1=float(xx1)
                xx2=float(xx2)
                xx3=float(xx3)
                x_values=np.arange(xx1,xx2,xx3)
            elif xx1 and xx2 :
                xx1=float(xx1)
                xx2=float(xx2)
                x_values=np.arange(xx1,xx2,0.2)
            elif xx3:
               
                xx3=float(xx3)
                x_values=np.arange(-dd,dd,xx3)

            else:
                x_values=np.arange(-dd,dd,0.1)
            
                
            
            
            y_values=[kk/x for x in x_values]

            plt.plot(x_values,y_values,color='b')
            
            sio=BytesIO()
            plt.savefig(sio,format='png')
            dat=base64.encodebytes(sio.getvalue()).decode()
            html = ''' <img src="data:image/png;base64,{}"/> '''
            plt.close()
            imd=html.format(dat)
            data['imd'] =imd
            data['status']="SUCCESS"
        return JsonResponse(data)
            

    elif xz2=='2' :
        if  aa=='' or bb=='' or cc=='':
            data['message'] = '输入类型错误！'
            data['status']="errors"
        else:
            
            aa=float(aa)
            bb=float(bb)
            cc=float(cc)
            
            ee=abs(aa)+abs(bb)+abs(cc)
            plt.switch_backend('agg')
            fig=plt.figure(figsize=(3.5,3.8))
            ax=axisartist.Subplot(fig,111)
            fig.add_axes(ax)
            #ax.axis["bottom"]=ax.new_floating_axis(0,0)
            #ax.axis["left"]=ax.new_floating_axis(1,0)
            ax.axis["bottom"].set_axisline_style("-|>",size=1.5)
            ax.axis["left"].set_axisline_style("->",size=1.5)
            #ax.axis["top"].set_visible(False)
            #ax.axis["right"].set_visible(False)
            plt.grid()
            if xx1 and xx2 and xx3:
                xx1=float(xx1)
                xx2=float(xx2)
                xx3=float(xx3)
                x_values=np.arange(xx1,xx2,xx3)
            elif xx1 and xx2 :
                xx1=float(xx1)
                xx2=float(xx2)
                x_values=np.arange(xx1,xx2,0.2)
            elif xx3:
               
                xx3=float(xx3)
                x_values=np.arange(-ee,ee,xx3)

            else:
                x_values=np.arange(-ee,ee,0.1)
           

            
            y_values=[aa*pow(x,2)+bb*x+cc for x in x_values]

            plt.plot(x_values,y_values,'r')
            #plt.plot(x_values,y_values1,color='b')
            sio=BytesIO()
            plt.savefig(sio,format='png')
            dat=base64.encodebytes(sio.getvalue()).decode()
            html = ''' <img src="data:image/png;base64,{}"/> '''
            plt.close()
            imd=html.format(dat)
            data['imd'] =imd
            data['status']="SUCCESS"
        return JsonResponse(data)
            
    else:
        data['message'] = '不能为空'
        data['status']="errors"
        return JsonResponse(data)


         


def Zuotu1(request):

    return render(request,'zuotu1.html')
        
        
def homeworkg(request):
    now=datetime.datetime.now()
    start=now-datetime.timedelta(hours=168,minutes=0,seconds=0)
    homewmaa=Homework.objects.filter(Q(homeworktime__gt=start)&Q(homeworkscore='A+'))
    # homewmaa = Homework.objects.filter(Q(homeworktime__in=[-1:])

    homewma = Homework.objects.filter(Q(homeworktime__gt=start) & Q(homeworkscore='A'))
    now=now.strftime('%Y-%m-%d %H:%M:%S')
    start=start.strftime('%Y-%m-%d %H:%M:%S')

    return render(request,'homeworkg.html',{'homewmaa':homewmaa,'homewma':homewma,'now':now,'start':start})


            
        


@csrf_exempt
def weixin_main(request):
    if request.method=='GET':
        signature = str(request.GET.get('signature',None))
        timestamp =str(request.GET.get('timestamp',None))
        nonce = str(request.GET.get('nonce',None))
        echostr= str(request.GET.get('echostr',None))

        token = 'hghgobi7727'

        hashlist = [token,timestamp,nonce]
        hashlist.sort()
        hashstr = ''
        for i in hashlist:
            hashstr+=i
        hashstr = hashlib.sha1(hashstr.encode(encoding="UTF-8")).hexdigest()
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("error")
    else:
        othercontent = "999"
        return HttpResponse(othercontent)