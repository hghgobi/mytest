from django.shortcuts import render,redirect,get_object_or_404
from .models import Classes
from django.http import HttpResponse,JsonResponse
from .models import Classes,Courses,Homework,Exams,Students,rankq,Classnotes,onlinetestgrade,onlinetestlist,Questions,Scores,Searchstudentid,Loginrecord,Classingss,Homeworksum,TXL,guoguan,guoguanname,addrankqdetail,badhomework,Wkqs,Yuxiname,Newnames,Yuxitestcount,Leavems,Xxqs
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
from random import shuffle
import cv2


import hashlib
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from wechatpy import parse_message,create_reply
from wechatpy.replies import TextReply
from wechatpy import WeChatClient
from wechatpy.exceptions import InvalidSignatureException

from wechatpy.utils import check_signature
from wechatpy.pay import logger



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
    fig=plt.figure(figsize=(3.3,3.3))

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.plot(dates,scores,c='red')
    plt.title("总体情况")
    fig.autofmt_xdate(rotation = 85)
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
        phone = request.POST.get('phone')
        # pwd = request.POST.get('pwd')
        if not  phone.isdigit():
            return render(request,'questionsindex.html',{'errors':'手机号类型错误！'})
        # teststudent = Searchstudentid.objects.filter(phone=phone)
        try:
            teststudent = get_object_or_404(Searchstudentid,phone=phone)
        except:
            return render(request, 'questionsindex.html', {'errors': '手机号错误，或不存在！请微信群联系数学老师。'})
        user = teststudent.student
        print(teststudent)
        # teststudent=Students.objects.filter(studentname=user,studentid=pwd)

        if teststudent:
            request.session["teststudent"]=user
            return redirect('../indexs')
        else:
            return render(request,'questionsindex.html',{'errors':'手机号错误，或不存在！请微信群联系数学老师。'})
      
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
    try:
        n='未读'
        m=get_object_or_404(Leavems,name=teststudent,ornot=n)
        m.ornot = '已读'
        m.save()
        return redirect('../teacherms')
    # notes_all_list = Classnotes.objects.all()
    # paginator = Paginator(notes_all_list,6)
    # page_num = request.GET.get('page',1)
    # page_of_notes = paginator.get_page(page_num)
    # currentr_page_num = page_of_notes.number
    # page_range = list(range(max(currentr_page_num - 2,1),currentr_page_num)) + \
    #              list(range(currentr_page_num,min(currentr_page_num + 2,paginator.num_pages)+1))
    except:
        return render(request, 'base3.html')



def Classnewslist(request):
    teststudent=request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')

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

def Showwkqs(request,id0,id1):
    id0 = id0
    id1 = id1
    if request.method == 'GET':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../../testlogin')
        if Newnames.objects.filter(zid = id0,jid = id1,name = teststudent):
            try:
                count =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)
                nnn = count.count+1
                Yuxitestcount.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                Yuxitestcount.addyxcount(id0, id1,teststudent,nnn)
            except:
                Yuxitestcount.addyxcount(zid=id0, jid=id1, name=teststudent, count=1)

            qs = Wkqs.objects.filter(zid=id0 ,jid = id1)
            qslist = []
            for i in qs:
                qslist.append(i.pk)
            shuffle(qslist)
            qslist = qslist[:10]
            a = qslist[0]
            ts = len(qslist)
            wk = a
            del qslist[0]
            # showquestionss = get_object_or_404(Wkqs, pk=a)
            # if showquestionss.category == 0:
            showquestions = Wkqs.objects.filter(pk=a)
            mss = '''<a><font color="green">请开始你的表演！</font></a>'''
            context = {'qslist': qslist, 'showquestions': showquestions, 'ts': ts, 'yzts': 1,
                       'correctamount': 0,'mss':mss,'wk':wk}

            return render(request, 'showwkqs2.html', context)

            # else:
            #     showquestions = Wkqs.objects.filter(pk=a)
            #     context = {'qslist': qslist, 'showquestions': showquestions, 'ts': ts, 'yzts': 1,
            #                'correctamount': 0}
            #     return render(request, 'showwkqs2.html', context)
        else:
            ms = '已通过本节预习测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

    if request.method == 'POST':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../testlogin')
        questionanswer = request.POST.get('questionanswer')
        studentanswer = request.POST.get('studentanswer')
        qslist=request.POST.get('qslist')
        correctamount=request.POST.get('correctamount')
        ts = request.POST.get('ts')
        yzts=request.POST.get('yzts')
        correctamount=int(correctamount)
        wk = request.POST.get('wk')
        ts = int(ts)
        yzts = int(yzts)
        if studentanswer:
            studentanswer=studentanswer.replace(" ", "")
            studentanswer=studentanswer.replace("。",".")
            studentanswer = studentanswer.replace("，", ".")
            studentanswer = studentanswer.replace(",", ".")
        else:
            pass
        print(studentanswer)

        if studentanswer==questionanswer:
            correctamount+=1
            mss ='''<a><font color="blue">恭喜你上一题答对了！</font></a>'''

        else:
            wrong = get_object_or_404(Wkqs,pk=wk)
            wrong.wrongcount+=1
            wrong.save()

            mss='''<a><font color="red">真可惜上一题没答对！</font></a>'''

        if yzts==ts:
            if correctamount>=ts-1:
                ornot = "已通过本节预习测试"
                ms = "恭喜你通过预习测试！请前往预习别的内容！"
                counts =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)
                nnnn = counts.count

                Yuxiname.addyxname(id0, id1,teststudent,ornot,nnnn)
                try:
                    Newnames.objects.filter(zid=id0,jid=id1,name=teststudent).delete()
                except:
                    pass

            else:
                ms = "预习测试不通过，请再看一遍微课，然后再次测试，祝你成功！"


            return render(request,'yuxi.html',{'ms':ms})
        yzts+=1

        qslist=list(eval(qslist))#将html传来的‘list’字符串转化为list
        a=qslist[0]
        wk = a
        del qslist[0]
        # showquestionss = get_object_or_404(Wkqs,pk=a)
        showquestions = Wkqs.objects.filter(pk=a)
        #
        # if showquestionss.category==0:
        #     context = {'qslist': qslist, 'showquestions': showquestions, 'ts': ts, 'yzts': yzts,
        #                'correctamount': correctamount, 'mss': mss}
        #     return render(request, 'showwkqs.html', context)
        #
        # else:
        context = {'qslist': qslist, 'showquestions': showquestions, 'ts': ts, 'yzts': yzts,
                   'correctamount': correctamount, 'mss': mss,'wk':wk}
        return render(request, 'showwkqs2.html', context)

def yuxiname(request,id0,id1):
    id0 = id0
    id1 = id1
    ms = Yuxiname.objects.filter(zid=id0,jid=id1)
    mss = Newnames.objects.filter(zid=id0,jid=id1)
    n = len(mss)
    return render(request,'yuxiname.html',{'ms':ms,'id0':id0,'id1':id1,'mss':mss,'n':n})
def Zuji(request):
    ms = Loginrecord.objects.all()
    return render(request,'zuji.html',{'ms':ms})
def Addnames(request,id0,id1):
    zid = id0
    jid = id1
    nameid = [20,16,32,27,9,19,22,5,10,17,15,12,14,31,13,18,24,25,11,8,7,56,60,54,53,68,63,66,58,77,67,47,52,71,65,48,61,59,64,49,51,50,55,62,23,75,57,72,26,69,73,29]
    for i in range(len(nameid)):
        id = nameid[i]
        try:

            names =Students.objects.filter(pk = id)
            name = names[0]
            Newnames.addname(zid=zid, jid=jid, name=name)
        except:
            pass
    return HttpResponse("成功！")


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
    aaa = request.POST.get('aaa')
    hhh = request.POST.get('hhh')
    kkk = request.POST.get('kkk')
    xz1=request.POST.get('xz1')
    xz2=request.POST.get('xz2')
    xz3=request.POST.get('xz3')
    xx1=request.POST.get('xx1')
    xx2=request.POST.get('xx2')
    xx3=request.POST.get('xx3')
    xz4 = request.POST.get('xz4')

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
        if k == '' or b=='' or kk=='':
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
            elif xx1 and xx2 :
                xx1=float(xx1)
                xx2=float(xx2)
                x_values=np.arange(xx1,xx2,1)
            elif xx3:
               
                xx3=float(xx3)
                x_values=np.arange(-dd,dd,xx3)

            else:
                x_values=np.arange(-dd,dd,1)

                
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
            hhh = -1 * (bb / (2 * aa))
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
                x_values=np.arange(xx1,xx2,1)
            elif xx3:
               
                xx3=float(xx3)
                x_values=np.arange(-ee,ee,xx3)

            else:
                x_values=np.arange(-ee,ee,1)



            y_values=[kk/x for x in x_values]
            y_values1=[aa*pow(x,2)+bb*x+cc for x in x_values]
            plt.vlines(hhh, min(y_values1) - 5, max(y_values1) + 3, colors="b", linestyles="dashed")


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
                x_values=np.arange(xx1,xx2,1)
            elif xx3:
               
                xx3=float(xx3)
                x_values=np.arange(-dd,dd,xx3)

            else:
                x_values=np.arange(-dd,dd,1)
            
                
            
            
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
            hhh= -1 * (bb / (2 * aa))
            ee=-1*(bb/(2*aa))+7
            ee1 = -1 * (bb / (2 * aa)) - 6
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
                x_values=np.arange(xx1,xx2,1)
            elif xx3:
               
                xx3=float(xx3)
                x_values=np.arange(ee1,ee,xx3)

            else:
                x_values=np.arange(ee1,ee,1)
           

            
            y_values=[aa*pow(x,2)+bb*x+cc for x in x_values]

            plt.plot(x_values,y_values,'r')
            plt.vlines(hhh, min(y_values) - 5, max(y_values) + 3, colors="b", linestyles="dashed")
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

    elif xz4 == '4':
        if aaa == '' or hhh == '' or kkk == '':
            data['message'] = '输入类型错误！'
            data['status'] = "errors"
        else:

            aaa = float(aaa)
            hhh = float(hhh)
            kkk = float(kkk)

            ee =  hhh + 6
            ee1 = hhh - 5
            plt.switch_backend('agg')
            fig = plt.figure(figsize=(3.5, 3.8))
            ax = axisartist.Subplot(fig, 111)
            fig.add_axes(ax)
            # ax.axis["bottom"]=ax.new_floating_axis(0,0)
            # ax.axis["left"]=ax.new_floating_axis(1,0)
            ax.axis["bottom"].set_axisline_style("-|>", size=1.5)
            ax.axis["left"].set_axisline_style("->", size=1.5)
            # ax.axis["top"].set_visible(False)
            # ax.axis["right"].set_visible(False)
            plt.grid()
            if xx1 and xx2 and xx3:
                xx1 = float(xx1)
                xx2 = float(xx2)
                xx3 = float(xx3)
                x_values = np.arange(xx1, xx2, xx3)
            elif xx1 and xx2:
                xx1 = float(xx1)
                xx2 = float(xx2)
                x_values = np.arange(xx1, xx2, 1)
            elif xx3:

                xx3 = float(xx3)
                x_values = np.arange(-ee, ee, xx3)

            else:
                x_values = np.arange(ee1, ee, 1)

            y_values = [aaa * pow(x-hhh, 2)  + kkk for x in x_values]

            plt.plot(x_values, y_values, 'r')
            plt.vlines(hhh, min(y_values)-5, max(y_values)+3, colors="b", linestyles="dashed")

            # plt.plot(x_values,y_values1,color='b')
            sio = BytesIO()
            plt.savefig(sio, format='png')
            dat = base64.encodebytes(sio.getvalue()).decode()
            html = ''' <img src="data:image/png;base64,{}"/> '''
            plt.close()
            imd = html.format(dat)
            data['imd'] = imd
            data['status'] = "SUCCESS"
        return JsonResponse(data)
            
    else:
        data['message'] = '不能为空'
        data['status']="errors"
        return JsonResponse(data)

def FC(request):
    a = []
    for i in range(-30, 30, 1):
        a.append(i)
    # print(a)
    a.remove(0)
    shuffle(a)
    # fc = []
    html=''''''

    for i in range(len(a)):
        num = -30
        while (num <= 30):
            if num == 0:
                num += 1
            elif a[i] % num == 0:
                b = int(a[i] / num)
                c = b + num
                d = a[i]
                if c > 0 and d > 0:
                    e =  "+" + str(c) + "x+" + str(d) + "=" + str(0)
                    html0 = '''<a>x<SUP>2</SUP>%s&nbsp;&nbsp;&nbsp;&nbsp;</a>''' % e
                    html = html + html0
                    # fc.append(e)
                elif c < 0 and d > 0:
                    e = str(c) + "x+" + str(d) + "=" + str(0)
                    html0 = '''<a>x<SUP>2</SUP>%s&nbsp;&nbsp;&nbsp;&nbsp;</a>''' % e
                    html = html + html0
                elif c > 0 and d < 0:
                    e =  "+" + str(c) + "x" + str(d) + "=" + str(0)
                    html0 = '''<a>x<SUP>2</SUP>%s&nbsp;&nbsp;&nbsp;&nbsp;</a>''' % e
                    html = html + html0
                elif c == 0 and d < 0:
                    e = str(d) + "=" + str(0)
                    html0 = '''<a>x<SUP>2</SUP>%s&nbsp;&nbsp;&nbsp;&nbsp;</a>''' % e
                    html = html + html0
                elif c == 0 and d > 0:
                    e = "+" + str(d) + "=" + str(0)
                    html0 = '''<a>x<SUP>2</SUP>%s&nbsp;&nbsp;&nbsp;&nbsp;</a>''' % e
                    html = html + html0
                elif c < 0 and d == 0:
                    e = str(c) + "x" + "=" + str(0)
                    html0 = '''<a>x<SUP>2</SUP>%s&nbsp;&nbsp;&nbsp;&nbsp;</a>''' % e
                    html = html + html0
                elif c > 0 and d == 0:
                    e =  "+" + str(c) + "x" + "=" + str(0)
                    html0 = '''<a>x<SUP>2</SUP>%s&nbsp;&nbsp;&nbsp;&nbsp;</a>''' % e
                    html = html + html0
                else:
                    e =  str(c) + "x" + str(d) + "=" + str(0)
                    html0 = '''<a>x<SUP>2</SUP>%s&nbsp;&nbsp;&nbsp;&nbsp;</a>''' % e
                    html = html + html0
                num += 1
            else:
                num += 1
    # print("生成了" + str(len(fc)) + "个方程：")
    return render(request,'fangcheng.html',{"html":html})

         


def Zuotu1(request):

    return render(request,'zuotu1.html')
        
        
def homeworkg(request):
    # now=datetime.datetime.now()
    now0=Homework.objects.latest()
    now=now0.homeworktime
    start=now-datetime.timedelta(hours=120,minutes=0,seconds=0)
    homewmaa=Homework.objects.filter(Q(homeworktime__gt=start)&Q(homeworkscore='A+'))
    # homewmaa = Homework.objects.filter(Q(homeworktime__in=[-1:])

    homewma = Homework.objects.filter(Q(homeworktime__gt=start) & Q(homeworkscore='A'))
    now=now.strftime('%Y-%m-%d %H:%M:%S')
    start=start.strftime('%Y-%m-%d %H:%M:%S')

    return render(request,'homeworkg.html',{'homewmaa':homewmaa,'homewma':homewma,'now':now,'start':start})


def Guoguan(request, idd):
    teststudent = request.session.get("teststudent")
    idd = idd
    if not teststudent:
        return redirect('../testlogin')
    name = guoguanname.objects.filter(idd=idd)[0]
    guoguanrank = guoguan.objects.filter(guoguan_name__idd=idd)

    return render(request, 'guoguan.html',{'guoguanrank': guoguanrank,'name':name})

def Guoguanpic(request,iddd):
    teststudent = request.session.get("teststudent")
    idd=iddd
    if not teststudent:
        return redirect('../testlogin')

    name = guoguanname.objects.filter(idd=idd)[0]
    guoguanrank = guoguan.objects.filter(guoguan_name__idd=idd)
    summ = len(guoguanrank)
    rank = {}
    for a in range(summ):
        if guoguanrank[a].ornot=="是":
            rank[guoguanrank[a].student_name] = 100
        else:
            rank[guoguanrank[a].student_name] = 0
    rank = sorted(rank.items(), key=lambda e: e[1], reverse=False)

    scores = []
    names = []
    for i in rank:
        names.append(i[0])
        scores.append(i[1])
    plt.switch_backend('agg')
    plt.figure(figsize=(24,12), dpi= 80,frameon=False)

    matplotlib.rcParams['font.sans-serif'] = ["SimHei"]
    matplotlib.rcParams['axes.unicode_minus'] = False


    plt.bar(range(len(scores)), scores, color='r', alpha=0.8)
    plt.xticks(range(len(scores)), names,rotation=75,alpha=3,size=25)

    plt.ylabel("100过关")
    plt.title(name)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.grid(linestyle='-.')
    for x, y in enumerate(scores):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}" align="left"/> '''
    plt.close()
    imd = html.format(data)
    rankms2 = rankq.objects.filter(fenlei='A')

    return render(request,'rankqpic.html',{"imd":imd})
def addguoguan(request):
    teststudent = request.session.get("teststudent")

    if not teststudent:
        return redirect('../testlogin')
    if request.method == "GET":
        return render(request,'addchuanguan.html')
    if request.method == "POST":
        idd = request.POST.get('idd')
        idd = int(idd)
        contentid = request.POST.get('contentid')
        contentid = int(contentid)
        namesss = Students.objects.filter(pk=idd)
        namesss = namesss[0]

        ornot = guoguan.objects.filter(Q(student_name__studentname=namesss) & Q(guoguan_name__idd=contentid))


        # ornot = get_object_or_404(guoguan, guoguan_name__idd=contentid)
        for i in range(len(ornot)):
            # ornot[i].student_name=ornot[i].student_name
            # ornot[i].guoguan_name=ornot[i].guoguan_name
            ornot[i].ornot = '是'
            # ornot[i].time=ornot[i].time
            ornot[i].save()

        # guoguan.addgg(namesss,contentid)

        return render(request, 'addchuanguan.html')

def guoguanlist(request):
    teststudent = request.session.get("teststudent")

    if not teststudent:
        return redirect('../testlogin')

    ggms = guoguan.objects.filter(student_name__studentname=teststudent)


    return render(request,'guoguandetail.html',{"ggms":ggms})


def Rankq(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')

    rankms = rankq.objects.filter(fenlei = 'A')
    summ = len(rankms)
    rank = {}
    for a in range(summ):
        rank[rankms[a].student_name] = rankms[a].score

    rank = sorted(rank.items(), key=lambda e: e[1], reverse=False)

    scores = []
    names = []
    for i in rank:
        names.append(i[0])
        scores.append(i[1])

    plt.switch_backend('agg')
    plt.figure(figsize=(24,12), dpi= 80,frameon=False)

    matplotlib.rcParams['font.sans-serif'] = ["SimHei"]
    matplotlib.rcParams['axes.unicode_minus'] = False


    plt.bar(range(len(scores)), scores, color='r', alpha=0.8)
    plt.xticks(range(len(scores)), names,rotation=60,alpha=3,size=20)

    plt.ylabel("总分")
    plt.title("积分排行榜")
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.grid(linestyle='-.')
    for x, y in enumerate(scores):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}" align="left"/> '''
    plt.close()
    imd = html.format(data)
    rankms2 = rankq.objects.filter(fenlei='A')

    return render(request,'rankqA.html',{"imd":imd,"rankms2":rankms2})



def RankqB(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')

    rankms = rankq.objects.filter(fenlei = 'B')
    summ = len(rankms)
    rank = {}
    for a in range(summ):
        rank[rankms[a].student_name] = rankms[a].score

    rank = sorted(rank.items(), key=lambda e: e[1], reverse=False)

    scores = []
    names = []
    for i in rank:
        names.append(i[0])
        scores.append(i[1])

    plt.switch_backend('agg')
    plt.figure(figsize=(24,12), dpi= 80,frameon=False)

    matplotlib.rcParams['font.sans-serif'] = ["SimHei"]
    matplotlib.rcParams['axes.unicode_minus'] = False


    plt.bar(range(len(scores)), scores, color='r', alpha=0.8)
    plt.xticks(range(len(scores)), names,rotation=45,size=20)

    plt.ylabel("总分")
    plt.title("积分排行榜")
    # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.grid(linestyle='-.')
    for x, y in enumerate(scores):
        plt.text( x - 0.1,y + 0.2, '%s' % y)
        # plt.text(x, y + 100, '%s' % round(y, 1), ha='center')
    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}" align="left"/> '''
    plt.close()
    imd = html.format(data)
    rankms2 = rankq.objects.filter(fenlei='B')

    return render(request,'rankqB.html',{"imd":imd,"rankms2":rankms2})

def addrankq(request):
    teststudent = request.session.get("teststudent")

    if not teststudent:
        return redirect('../testlogin')
    if request.method == "GET":
        return render(request,'addrankq.html')
    if request.method == "POST":
        idd = request.POST.get('idd')
        idd = int(idd)
        score = request.POST.get('score')
        score = int(score)
        namesss = Students.objects.filter(pk=idd)
        namessss = namesss[0]
        ms = get_object_or_404(rankq,student_name__studentname=namessss)
        ms.score+=score
        ms.save()
        detail = "A-"+ "__加__"+str(score)+"分;"
        addrankqdetail.addd(detail=detail,name=namessss)
        return render(request, 'addrankq.html')

def addrankqb(request):
    teststudent = request.session.get("teststudent")

    if not teststudent:
        return redirect('../testlogin')
    if request.method == "GET":
        return render(request,'addrankqb.html')
    if request.method == "POST":
        idd = request.POST.get('idd')
        idd = int(idd)
        score = request.POST.get('score')
        score = int(score)
        namesss = Students.objects.filter(pk=idd)
        namessss = namesss[0]
        ms = get_object_or_404(rankq,student_name__studentname=namessss)
        ms.score+=score
        ms.save()
        detail = "B-"+ "__加__"+str(score)+"分;"
        addrankqdetail.addd(detail=detail,name=namessss)
        return render(request, 'addrankqb.html')


def badhomeworkms(request):
    teststudent = request.session.get("teststudent")

    if not teststudent:
        return redirect('../testlogin')
    if request.method == "GET":
        return render(request, 'badhomeworkms.html')
    if request.method == "POST":
        time0 = request.POST.get('time0')
        stu_id = request.POST.get('stu_id')
        ornot = request.POST.get('ornot')
        if time0 :
            ms = badhomework.objects.filter(time0=time0)
            return render(request, 'badhomeworkms.html',{"ms":ms})
        elif stu_id :
            ms = badhomework.objects.filter(stu_id=stu_id)
            return render(request, 'badhomeworkms.html',{"ms":ms})
        elif ornot :
            ms = badhomework.objects.filter(ornot=ornot)
            return render(request, 'badhomeworkms.html',{"ms":ms})
        else:
            ms="错误"
            return render(request, 'badhomeworkms.html', {"ms": ms})
def badhomeworkms2(request):
    teststudent = request.session.get("teststudent")

    if not teststudent:
        return redirect('../testlogin')
    ms = badhomework.objects.filter(student_name__studentname=teststudent)
    return render(request, 'badhomeworkms2.html', {"ms": ms})

def badhomeworkmsshow(request,time0):
    time0 = time0
    ms = badhomework.objects.filter(time0=time0)
    return render(request, 'badhomeworkmsshow.html', {"ms": ms})





def addhwbad(request):
    teststudent = request.session.get("teststudent")

    if not teststudent:
        return redirect('../testlogin')
    if request.method == "GET":
        return render(request,'addhwbad.html')

    if request.method == "POST":
        time0 = request.POST.get('time0')
        name = request.POST.get('name')
        ms = request.POST.get('ms')
        stu_id = request.POST.get('stu_id')
        ornot = request.POST.get('ornot')
        idd = int(stu_id)
        namesss = Students.objects.filter(pk=idd)
        namessss = namesss[0]
        badhomework.addbadhomework(time0=time0,name=name,stu_id=stu_id,student_name=namessss,ornot=ornot,ms=ms)

        return render(request, 'addhwbad.html')

def xiugaihwms(request):

    if request.method == "GET":
        return render(request,'xiugaihwms.html')

    if request.method == "POST":
        time0 = request.POST.get('time0')
        stu_id = request.POST.get('stu_id')
        ornot = request.POST.get('ornot')

        xiugai = get_object_or_404(badhomework,time0=time0,stu_id=stu_id)
        xiugai.ornot=ornot
        xiugai.save()

        return render(request, 'xiugaihwms.html')

#
#
# @csrf_exempt
# def weixin_main(request):
#     # if request.method=='GET':
#     #     signature = str(request.GET.get('signature',None))
#     #     timestamp =str(request.GET.get('timestamp',None))
#     #     nonce = str(request.GET.get('nonce',None))
#     #     echostr= str(request.GET.get('echostr',None))
#     #
#     #     token = 'hghgobi7727'
#     #
#     #     hashlist = [token,timestamp,nonce]
#     #     hashlist.sort()
#     #     hashstr = ''
#     #     for i in hashlist:
#     #         hashstr+=i
#     #     hashstr = hashlib.sha1(hashstr.encode(encoding="UTF-8")).hexdigest()
#     #     if hashstr == signature:
#     #         return HttpResponse(echostr)
#     #     else:
#     #         return HttpResponse("error")
#     # else :
#     #     msg = parse_message(request.body)
#     #     if msg.type == 'text':
#     #         reply = create_reply('这是条文字消息', msg)
#     #     elif msg.type == 'image':
#     #         reply = create_reply('这是条图片消息', msg)
#     #     elif msg.type == 'voice':
#     #         reply = create_reply('这是条语音消息', msg)
#     #     else:
#     #         reply = create_reply('这是条其他类型消息', msg)
#     #     response = HttpResponse(reply.render(), content_type="application/xml")
#     #     return response
#     if request.method == 'GET':
#         signature = request.GET.get('signature', '')
#         timestamp = request.GET.get('timestamp', '')
#         nonce = request.GET.get('nonce', '')
#         echo_str = request.GET.get('echostr', '')
#         try:
#             check_signature(token, signature, timestamp, nonce)
#         except InvalidSignatureException:
#             echo_str = '错误的请求'
#         response = HttpResponse(echo_str)
#         return response
#
#     # elif request.method == 'POST':
#     #     msg = parse_message(request.body)
#     #     if msg.type == 'text':
#     #         reply = create_reply('这是条文字消息', msg)
#     #     elif msg.type == 'image':
#     #         reply = create_reply('这是条图片消息', msg)
#     #     elif msg.type == 'voice':
#     #         reply = create_reply('这是条语音消息', msg)
#     #     else:
#     #         reply = create_reply('这是条其他类型消息', msg)
#     #     response = HttpResponse(reply.render(), content_type="application/xml")
#     #     return response
#     else:
#         othercontent= autoreply(request)
#         return HttpResponse(othercontent)
#
# import xml.etree.ElementTree as ET
#
# def autoreply(request):
#     try:
#         webData = request.body
#         xmlData = ET.fromstring(webData)
#
#         msg_type = xmlData.find('MsgType').text
#         ToUserName = xmlData.find('ToUserName').text
#         FromUserName = xmlData.find('FromUserName').text
#         CreateTime = xmlData.find('CreateTime').text
#         MsgType = xmlData.find('MsgType').text
#         MsgId = xmlData.find('MsgId').text
#
#         toUser = FromUserName
#         fromUser = ToUserName
#
#         if msg_type == 'text':
#             content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
#             replyMsg = TextMsg(toUser, fromUser, content)
#             print ('成功了!!!!!!!!!!!!!!!!!!!')
#             print (replyMsg)
#             return replyMsg.send()
#
#         elif msg_type == 'image':
#             content = "图片已收到,谢谢"
#             replyMsg = TextMsg(toUser, fromUser, content)
#             return replyMsg.send()
#         elif msg_type == 'voice':
#             content = "语音已收到,谢谢"
#             replyMsg = TextMsg(toUser, fromUser, content)
#             return replyMsg.send()
#         elif msg_type == 'video':
#             content = "视频已收到,谢谢"
#             replyMsg = TextMsg(toUser, fromUser, content)
#             return replyMsg.send()
#         elif msg_type == 'shortvideo':
#             content = "小视频已收到,谢谢"
#             replyMsg = TextMsg(toUser, fromUser, content)
#             return replyMsg.send()
#         elif msg_type == 'location':
#             content = "位置已收到,谢谢"
#             replyMsg = TextMsg(toUser, fromUser, content)
#             return replyMsg.send()
#         else:
#             msg_type == 'link'
#             content = "链接已收到,谢谢"
#             replyMsg = TextMsg(toUser, fromUser, content)
#             return replyMsg.send()
#     except Argment:
#         return  Argment
#
#
#
#
# class Msg(object):
#     def __init__(self, xmlData):
#         self.ToUserName = xmlData.find('ToUserName').text
#         self.FromUserName = xmlData.find('FromUserName').text
#         self.CreateTime = xmlData.find('CreateTime').text
#         self.MsgType = xmlData.find('MsgType').text
#         self.MsgId = xmlData.find('MsgId').text
#
# import time
# class TextMsg(Msg):
#     def __init__(self, toUserName, fromUserName, content):
#         self.__dict = dict()
#         self.__dict['ToUserName'] = toUserName
#         self.__dict['FromUserName'] = fromUserName
#         self.__dict['CreateTime'] = int(time.time())
#         self.__dict['Content'] = content
#
#     def send(self):
#         XmlForm = """
#         <xml>
#         <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
#         <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
#         <CreateTime>{CreateTime}</CreateTime>
#         <MsgType><![CDATA[text]]></MsgType>
#         <Content><![CDATA[{Content}]]></Content>
#         </xml>
#         """
#         return XmlForm.format(**self.__dict)


def Addtxl(request):
    return HttpResponse('因隐私问题，暂停通讯录服务，以后有需要再开放')

def Addtxl3(request):   #非异步提交
    if request.method=='GET':
        mss=TXL.objects.all()
        if mss :
            return render(request, 'tongxl.html', {'mss': mss})
        else:
            return render(request, 'tongxl.html')
    if request.method=='POST':
        mss = TXL.objects.all()
        name=request.POST.get('name')
        if name=='':
            return render(request, 'tongxl.html', {'error': '姓名不能为空！','mss': mss})
        company= request.POST.get('company')
        major=request.POST.get('major')
        gdtime= request.POST.get('gdtime')
        phone1= request.POST.get('phone1')
        if phone1.isdigit():
            pass
        else:
            return render(request, 'tongxl.html', {'error': '长号类型错误！', 'mss': mss})

        phone2= request.POST.get('phone2')
        if phone2.isdigit():
            pass
        else:
            phone2=int(0)
        TXL.createms(name,company,major,gdtime,phone1,phone2)
        mss = TXL.objects.all()
        return render(request, 'tongxl.html', {'mss': mss})

def Addtxl2(request): #通讯录异步提交1
    mss=TXL.objects.all()
    if mss :
        return render(request,'tongxl.html',{'mss':mss})
    else:
        return render(request,'tongxl.html')
def Addtxl22(request):
    data={}
    name=request.POST.get('name')
    if name:
        pass
    else:
        data['error']='姓名不能为空'
        data['status']='error'
        return JsonResponse(data)
    company=request.POST.get('company')
    major=request.POST.get('major')
    gdtime=request.POST.get('gdtime')
    phone1=request.POST.get('phone1')
    if phone1.isdigit():
        pass
    else:
        data['error']='手机号只能是数字'
        data['status']='error'
        return JsonResponse(data)
    phone2=request.POST.get('phone2')
    if phone2.isdigit():
        pass
    else:
        phone2=int(0)
    TXL.createms(name, company, major, gdtime, phone1, phone2)
    data['status'] = 'success'
    return JsonResponse(data)

def CS(request):
    return render(request,'cesi.html')


def leavems(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    ms = Leavems.objects.filter(name=teststudent)
    return render(request,'leavems.html',{'ms':ms,'teststudent':teststudent})

def addteacherms(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    if request.method=='GET':
        return render(request,'addteacherms.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        ornot = request.POST.get('ornot')
        category = request.POST.get('category')

        try:
            n = '未读'
            m = get_object_or_404(Leavems, name=teststudent, ornot=n)
            m.ornot = '已读'
            m.save()
            Leavems.addms(name, text, category, ornot)
        except:
            Leavems.addms(name,text,category,ornot)
        return render(request,'addteacherms.html')


def inputms(request):
    return render(request,'jsq.html')


def xxtest(request):
    if request.method=="GET":
        QS = Xxqs.objects.all()
        qslist = []
        for i in QS:
            qslist.append(i.pk)
        shuffle(qslist)
        a = qslist[0]
        ts = len(qslist)
        del qslist[0]
        # showquestionss = get_object_or_404(Wkqs, pk=a)
        # if showquestionss.category == 0:
        showquestions = Xxqs.objects.filter(pk=a)
        context = {'qslist': qslist, 'showquestions': showquestions, 'ts': ts, 'yzts': 1,
                   'correctamount': 0}
        yunsuan = get_object_or_404(Xxqs,pk=a)
        if yunsuan.yunsuan==1:
            return render(request, 'xxqs1.html', context)
        elif yunsuan.yunsuan==2:
            return render(request, 'xxqs2.html', context)
        elif yunsuan.yunsuan==3:
            return render(request, 'xxqs3.html', context)
        else:
            return render(request, 'xxqs4.html', context)

    if request.method == 'POST':
        questionanswer = request.POST.get('questionanswer')
        studentanswer = request.POST.get('studentanswer')
        qslist=request.POST.get('qslist')
        correctamount=request.POST.get('correctamount')
        ts = request.POST.get('ts')
        yzts=request.POST.get('yzts')
        correctamount=int(correctamount)
        ts = int(ts)
        yzts = int(yzts)

        if studentanswer==questionanswer:
            correctamount+=1
            mss ='''<a><font color="blue">上一题答对了</font></a>'''

        else:

            mss='''<a><font color="red">上一题没答对</font></a>'''

        yzts+=1

        qslist=list(eval(qslist))#将html传来的‘list’字符串转化为list
        a=qslist[0]
        del qslist[0]
        # showquestionss = get_object_or_404(Wkqs,pk=a)
        showquestions = Xxqs.objects.filter(pk=a)
        #
        # if showquestionss.category==0:
        #     context = {'qslist': qslist, 'showquestions': showquestions, 'ts': ts, 'yzts': yzts,
        #                'correctamount': correctamount, 'mss': mss}
        #     return render(request, 'showwkqs.html', context)
        #
        # else:
        context = {'qslist': qslist, 'showquestions': showquestions, 'ts': ts, 'yzts': yzts,
                   'correctamount': correctamount, 'mss': mss}
        yunsuan = get_object_or_404(Xxqs,pk=a)
        if yunsuan.yunsuan==1:
            return render(request, 'xxqs1.html', context)
        elif yunsuan.yunsuan==2:
            return render(request, 'xxqs2.html', context)
        elif yunsuan.yunsuan==3:
            return render(request, 'xxqs3.html', context)
        else:
            return render(request, 'xxqs4.html', context)



def xxtest2(request):
    if request.method=="GET":
        QS = Xxqs.objects.all()
        answer = []
        ornot = []
        tm = []
        for i in QS:
            if i.yunsuan==1:
                html = '''<div style="font-size:100px">%s+%s</div>'''%(i.num0,i.num1)
                tm.append(html)
                ornot.append(i.ornot)
                answer.append(i.answer)
            elif i.yunsuan==2:
                html = '''<div style="font-size:100px">%s-%s</div>'''%(i.num0,i.num1)
                tm.append(html)
                ornot.append(i.ornot)
                answer.append(i.answer)
            elif i.yunsuan==3:
                html = '''<div style="font-size:100px">%s &times %s</div>'''%(i.num0,i.num1)
                tm.append(html)
                ornot.append(i.ornot)
                answer.append(i.answer)
            else:
                html = '''<div style="font-size:100px">%s &divide %s</div>'''%(i.num0,i.num1)
                tm.append(html)
                ornot.append(i.ornot)
                answer.append(i.answer)

            # num0.append(i.num0)
            # num1.append(i.num1)
            # answer.append(i.answer)
            # ornot.append(i.ornot)
            # yunsuan.append(i.yunsuan)
            ts = len(answer)
    # return render(request,'xxtest.html',{'num0':json.dumps(num0),'num1':json.dumps(num1),'answer':json.dumps(answer),'ornot':json.dumps(ornot),'yunsuan':json.dumps(yunsuan),'ts':ts,'yzts': 0,'correctamount': 0})
    return render(request, 'xxtest.html',{'answer': json.dumps(answer),'tm':json.dumps(tm),'ts':ts,'yzts': 0,'correctamount': 0,'ornot':json.dumps(ornot)})


def getpic(request):
    pic = []
    picss = Wkqs.objects.filter(zid=23,jid=1)
    print(len(picss))

    # for i in picss:
    #
    #     a=i.questiontext.url
    #     aa = "E:/14_env/mytest"+a
    #     print(aa)
    # img = cv2.imread("E:/14_env/mytest/media/questions/54B_7TErtgm.png")
    for i in picss:
        a = i.questiontext.url
        # aa = "home/mytest" + a
        # print(aa)
        img = cv2.imread(a)
        try:
            aaa = base64.b64encode(cv2.imencode('.jpg',img)[1]).decode()
            html = ''' <img src="data:image/png;base64,{}" width="100%" height="50%"/> '''
            imd = html.format(aaa)
            pic.append(imd)
        except:
            pass

    return render(request,'testpic.html',{'pic':json.dumps(pic)})








