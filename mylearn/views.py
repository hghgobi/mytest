from django.shortcuts import render,redirect,get_object_or_404
from .models import Classes
from django.http import HttpResponse,JsonResponse
from .models import Address1,Address2, Kzlogin,Kzms, Zbhf, Datirecord, Dati,Daticontrol, Costtimels, Timelimitzk, Yuxinamezk, Zktishu,Zkfx, Lasttime,Rankxhl, Xxqs22,Xxqs23,Xxqs24,Xxqs2,Wktestlimit0,Yuxiname0,Yuxitestcount0,Newnames0,Classnotes0,Classes,Courses,XHL,Homework,Exams,Students,rankq,Classnotes,onlinetestgrade,onlinetestlist,Questions,Scores,Searchstudentid,Loginrecord,Classingss,Homeworksum,TXL,guoguan,guoguanname,addrankqdetail,badhomework,Wkqs,Yuxiname,Newnames,Yuxitestcount,Leavems,Xxqs,Wkqs2,Wktestlimit,Testrm,Wkqs3,Wkqs4,Xxdata
import json
import random
import numpy as np
from django.core import serializers
from django.contrib import auth
from django.core.paginator import Paginator
from random import choice
import string
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment

import time
import hashlib



from matplotlib.figure import Figure                      
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
import datetime
import base64
from io import BytesIO

import mpl_toolkits.axisartist as axisartist
import matplotlib
import math
import time
from django.db.models import Q
from random import shuffle
import cv2
import requests
import urllib



import hashlib
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from wechatpy import parse_message,create_reply
from wechatpy.replies import TextReply
from wechatpy import WeChatClient
from wechatpy.exceptions import InvalidSignatureException

from wechatpy.utils import check_signature
from wechatpy.pay import logger


def Kz(request,code):
    if request.method=='GET':
        code=code
        get_object_or_404(Kzlogin,code=code)
        return render(request,"kz.html",{"code":code})
    if request.method=='POST':
        qu=request.POST.get('qu')
        jd=request.POST.get('jd')
        qu=int(qu)
        jd=int(jd)
        data={}
        code=code
        name=request.POST.get('name')
        idNumber=request.POST.get('idnumber')
        phone=request.POST.get('phone')
        addressDetail=request.POST.get('address')
        get_object_or_404(Kzlogin,code=code)
        Kzlogin.objects.filter(code=code).delete()
        a=Address1.objects.filter(id0=qu)
        b=Address2.objects.filter(id0=jd)
        address=str(a[0].name+b[0].name)
        addressCode=jd
        Kzms.addms(name,idNumber,phone,address,addressDetail,addressCode)
        data['status']='success'
        return JsonResponse(data)

def Kzgetms(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    datas=[]
    ms=Kzms.objects.all()
    for i in range(len(ms)):
        data = {}
        data['name']=ms[i].name
        data['idNumber']=ms[i].idNumber
        data['phone']=ms[i].phone
        data['phoneBackup']=""
        data['address']=ms[i].address
        data['addressDetail']=ms[i].addressDetail
        data['goodsCode']='kouzhao'
        data['addressCode']=ms[i].addressCode
        datas.append(data)
    return render(request,'kzgetms.html',{"ms":json.dumps(datas,ensure_ascii=False)})

def Kzurl(request,id0):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin')
    chars =string.digits
    codes='<p>手机号和身份证号要正确</p><a><font size="5">'
    for i in range(int(id0)):
        a = ''.join([choice(chars) for i in range(8)])
        Kzlogin.addcode(code=a)
        b="http://35925.top/kz/"+a
        codes=codes+b+'<p></p>'
    codes = codes+'</font></a>'

    return HttpResponse(codes)










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
        return redirect('../../')
    return render(request,'questionsindex.html')
def Login0(request):
    data = {}
    phone = request.POST.get('phone')
    # pwd = request.POST.get('pwd')
    if  phone.isdigit():

        # teststudent = Searchstudentid.objects.filter(phone=phone)
        try:
            teststudent = get_object_or_404(Searchstudentid, phone=phone)
        except:
            data['status'] = "success2"
            return JsonResponse(data)
        user = teststudent.student
        # teststudent=Students.objects.filter(studentname=user,studentid=pwd)

        if teststudent:
            request.session["teststudent"] = user
            data['status'] = "success3"
            return JsonResponse(data)
            # return redirect('../indexs')
        else:
            data['status'] = "success4"
            return JsonResponse(data)
            # return render(request,'questionsindex.html',{'errors':'手机号错误，或不存在！请微信群联系数学老师。'})
    else:
        data['status'] = "success1"
        return JsonResponse(data)



def Onlinetestlogin0(request):
    teststudent0 = request.session.get("teststudent0")
    if teststudent0:
        return redirect('../indexs0')

    if request.method == "POST":
        phone = request.POST.get('phone')
        # pwd = request.POST.get('pwd')
        if not phone.isdigit():
            return render(request, 'questionsindex.html', {'errors': '手机号类型错误！'})
        # teststudent = Searchstudentid.objects.filter(phone=phone)
        try:
            teststudent0 = get_object_or_404(XHL, phone=phone)
        except:
            return render(request, 'questionsindex.html', {'errors': '手机号错误，或不存在！请微信群联系数学老师。'})
        user = teststudent0.name

        # teststudent=Students.objects.filter(studentname=user,studentid=pwd)

        if teststudent0:
            request.session["teststudent0"] = user
            return redirect('../indexs0')
        else:
            return render(request, 'questionsindex.html', {'errors': '手机号错误，或不存在！请微信群联系数学老师。'})

    return render(request, 'questionsindex.html')
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
    teststudent = request.session.get("teststudent")
    if teststudent:
        ms=teststudent+"，欢迎！"
    else:
        ms=''
    return render(request, 'base3.html',{'ms':ms})
    # teststudent=request.session.get("teststudent")

    # if not teststudent:
    #     return redirect('../testlogin')
    #
    # loginrecord=get_object_or_404(Loginrecord,loginuser=teststudent)
    #
    # loginrecord.logincount =int(loginrecord.logincount)+1
    # loginrecord.save()
    # try:
    #     n='未读'
    #     m=get_object_or_404(Leavems,name=teststudent,ornot=n)
    #     m.ornot = '已读'
    #     m.save()
    #     return redirect('../teacherms')
    # # notes_all_list = Classnotes.objects.all()
    # # paginator = Paginator(notes_all_list,6)
    # # page_num = request.GET.get('page',1)
    # # page_of_notes = paginator.get_page(page_num)
    # # currentr_page_num = page_of_notes.number
    # # page_range = list(range(max(currentr_page_num - 2,1),currentr_page_num)) + \
    # #              list(range(currentr_page_num,min(currentr_page_num + 2,paginator.num_pages)+1))
    # except:
    #     return render(request, 'base3.html')

def Indexs0(request):
    # teststudent=request.session.get("teststudent0")
    #
    # if not teststudent:
    #     return redirect('../testlogin0')

    return render(request, 'xhlbase3.html')

def Classnewslist(request):
    # teststudent=request.session.get("teststudent")
    # if not teststudent:
    #     return redirect('../testlogin')

    notes_all_list = Classnotes.objects.all()
    paginator = Paginator(notes_all_list,6)
    page_num = request.GET.get('page',1)
    page_of_notes = paginator.get_page(page_num)
    currentr_page_num = page_of_notes.number
    page_range = list(range(max(currentr_page_num - 2,1),currentr_page_num)) + \
                 list(range(currentr_page_num,min(currentr_page_num + 2,paginator.num_pages)+1))

    return render(request,'base.html',{'page_of_notes':page_of_notes,'page_range':page_range})
def Classnewslist0(request):
    teststudent0=request.session.get("teststudent0")
    if not teststudent0:
        return redirect('../testlogin0')

    notes_all_list = Classnotes0.objects.all()
    paginator = Paginator(notes_all_list,6)
    page_num = request.GET.get('page',1)
    page_of_notes = paginator.get_page(page_num)
    currentr_page_num = page_of_notes.number
    page_range = list(range(max(currentr_page_num - 2,1),currentr_page_num)) + \
                 list(range(currentr_page_num,min(currentr_page_num + 2,paginator.num_pages)+1))

    return render(request,'xhlbase.html',{'page_of_notes':page_of_notes,'page_range':page_range})
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
    # teststudent=request.session.get("teststudent")
    notename_pk=notename_pk
    # user=teststudent
    # if not teststudent:
    #     return redirect('../testlogin')
    classnotesdetail=Classnotes.objects.filter(id=notename_pk)
    classnotes=get_object_or_404(Classnotes,id=notename_pk)
   
    classnotes.readed_num += 1
    classnotes.save()

    # notes_content_type = ContentType.objects.get_for_model(classnotes)
    # comments = Comment.objects.filter(content_type=notes_content_type, object_id=notename_pk)
  
    response = render(request,'classnotes.html',{'classnotesdetail':classnotesdetail,'notename_pk':notename_pk})
   
    return response
# 'comments':comments,'user':user,

def Classnotesdetail0(request, notename_pk):
    # teststudent0 = request.session.get("teststudent0")
    notename_pk = notename_pk
    # user = teststudent0
    # if not teststudent0:
    #     return redirect('../testlogin0')
    classnotesdetail = Classnotes0.objects.filter(id=notename_pk)
    classnotes = get_object_or_404(Classnotes0, id=notename_pk)

    classnotes.readed_num += 1
    classnotes.save()

    response = render(request, 'xhlclassnotes.html',
                      {'classnotesdetail': classnotesdetail,
                       'notename_pk': notename_pk})

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

def Showwkqs33(request,id0,id1):
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
                ornot = "已通过本节测试"
                ms = "恭喜你通过预习测试！"
                counts =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)
                nnnn = counts.count

                Yuxiname.addyxname(id0, id1,teststudent,ornot,nnnn)
                try:
                    Newnames.objects.filter(zid=id0,jid=id1,name=teststudent).delete()
                except:
                    pass

            else:
                ms = "测试不通过，请再次测试，祝你成功！"


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

            qsids = []

            qs = Wkqs.objects.filter(zid=id0 ,jid = id1)
            for e in qs:
                qsids.append(e.pk)
            wklm = Wktestlimit.objects.filter(zid=id0, jid=id1)
            limit = []
            shuffle(qsids)

            for j in wklm:
                limit.append(j.limit)
                limit.append(j.chances)

            qstext = []
            qsanswer1 = []
            qsid = []

            qsamount = len(qs)
            zid=id0
            jid=id1
            testrm=[]
            testrms = Testrm.objects.filter(zid=id0, jid=id1)
            for f in testrms:
                testrm.append(f.testrm.url)
            for i in range(len(qsids)):
                id00 = qsids[i]
                qss = get_object_or_404(Wkqs,pk=id00)
                qstext.append(qss.questiontext.url)
                qsanswer1.append(qss.questionanswer)
                qsid.append(qss.pk)

            return render(request, 'showwkqs3.html',
                          {'testrm':json.dumps(testrm),'qstext': json.dumps(qstext), 'qsanswer1': json.dumps(qsanswer1),
                            'qsid': qsid, 'qsamount': json.dumps(qsamount),
                           'zid': zid, 'jid': jid, 'limit': json.dumps(limit)})
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

def Showwkqs1(request,id0,id1):
    id0 = id0
    id1 = id1
    if request.method == 'GET':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../../testlogin')
        timess = int(time.time())
        if Newnames.objects.filter(zid = id0,jid = id1,name = teststudent):
            try:
                count =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)

                nnn = count.count+1
                Yuxitestcount.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                Yuxitestcount.addyxcount(id0, id1,teststudent,nnn,timess)
            except:
                Yuxitestcount.addyxcount(id0, id1,teststudent,1,timess)

            qsids = []

            qs = Wkqs.objects.filter(zid=id0 ,jid = id1)
            for e in qs:
                qsids.append(e.pk)
            wklm = Wktestlimit.objects.filter(zid=id0, jid=id1)
            limit = []
            shuffle(qsids)

            for j in wklm:
                limit.append(j.limit)
                limit.append(j.chances)
            qstext = []
            qsanswer1 = []
            qsid = []
            categorys = []
            qsamount = len(qs)
            zid=id0
            jid=id1
            testrm=[]
            testrms = Testrm.objects.filter(zid=id0, jid=id1)
            for f in testrms:
                testrm.append(f.testrm.url)
            for i in range(len(qsids)):
                id00 = qsids[i]
                qss = get_object_or_404(Wkqs,pk=id00)
                qstext.append(qss.questiontext.url)
                qsanswer1.append(hashlib.md5(qss.questionanswer.encode()).hexdigest())
                qsid.append(qss.pk)
                categorys.append(qss.category)
            # if categorys[0]==3:
            return render(request,'showqs1.html',{'categorys':json.dumps(categorys),'testrm':json.dumps(testrm),'qstext':json.dumps(qstext),'qsanswer1':json.dumps(qsanswer1),'qsid':qsid,'qsamount':json.dumps(qsamount),'zid':zid,'jid':jid,'limit':json.dumps(limit)})
            # else:
            #     return render(request, 'showqs4.html',
            #                   {'testrm':json.dumps(testrm),'qstext': json.dumps(qstext), 'qsanswer1': json.dumps(qsanswer1),
            #                    'qsanswer2': json.dumps(qsanswer2), 'qsid': qsid, 'qsamount': json.dumps(qsamount),
            #                    'zid': zid, 'jid': jid, 'limit': json.dumps(limit)})
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

    if request.method == 'POST':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../testlogin')

        # costtime = request.POST.get('time')
        id0 = request.POST.get('zid')
        id1 = request.POST.get('jid')

        if Newnames.objects.filter(zid=id0, jid=id1, name=teststudent):
            pass
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

        counts =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)
        nnnn = counts.count
        time0 = counts.seconds
        time1 = int(time.time())
        a = datetime.datetime.utcfromtimestamp(time0)
        b = datetime.datetime.utcfromtimestamp(time1)
        costtime =(b-a).seconds
        ornot = "已通过本节测试"
        Yuxiname.addyxname(id0, id1,teststudent,ornot,nnnn,costtime)
        try:
            Newnames.objects.filter(zid=id0,jid=id1,name=teststudent).delete()
        except:
            pass
        ms = Yuxiname.objects.filter(zid=id0, jid=id1)
        mss = Newnames.objects.filter(zid=id0, jid=id1)
        n = len(mss)
        return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1, 'mss': mss, 'n': n})


def Showwkqs2(request,id0,id1):
    id0 = id0
    id1 = id1
    if request.method == 'GET':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../../testlogin')
        timess = int(time.time())
        if Newnames.objects.filter(zid = id0,jid = id1,name = teststudent):
            try:
                count =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)

                nnn = count.count+1
                Yuxitestcount.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                Yuxitestcount.addyxcount(id0, id1,teststudent,nnn,timess)
            except:
                Yuxitestcount.addyxcount(id0, id1,teststudent,1,timess)

            qsids = []

            qs = Wkqs2.objects.filter(zid=id0 ,jid = id1)
            for e in qs:
                qsids.append(e.pk)
            wklm = Wktestlimit.objects.filter(zid=id0, jid=id1)
            limit = []
            shuffle(qsids)

            for j in wklm:
                limit.append(j.limit)
                limit.append(j.chances)
            qstext = []
            qsanswer1 = []
            qsanswer2 = []
            qsid = []
            categorys = []
            qsamount = len(qs)
            zid=id0
            jid=id1
            testrm=[]
            testrms = Testrm.objects.filter(zid=id0, jid=id1)
            for f in testrms:
                testrm.append(f.testrm.url)
            for i in range(len(qsids)):
                id00 = qsids[i]
                qss = get_object_or_404(Wkqs2,pk=id00)
                qstext.append(qss.questiontext.url)
                qsanswer1.append(hashlib.md5(qss.questionanswer1.encode()).hexdigest())
                qsanswer2.append(hashlib.md5(qss.questionanswer2.encode()).hexdigest())
                qsid.append(qss.pk)
                categorys.append(qss.category)
            # if categorys[0]==3:
            return render(request,'showqs3.html',{'categorys':json.dumps(categorys),'testrm':json.dumps(testrm),'qstext':json.dumps(qstext),'qsanswer1':json.dumps(qsanswer1),'qsanswer2':json.dumps(qsanswer2),'qsid':qsid,'qsamount':json.dumps(qsamount),'zid':zid,'jid':jid,'limit':json.dumps(limit)})
            # else:
            #     return render(request, 'showqs4.html',
            #                   {'testrm':json.dumps(testrm),'qstext': json.dumps(qstext), 'qsanswer1': json.dumps(qsanswer1),
            #                    'qsanswer2': json.dumps(qsanswer2), 'qsid': qsid, 'qsamount': json.dumps(qsamount),
            #                    'zid': zid, 'jid': jid, 'limit': json.dumps(limit)})
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

    if request.method == 'POST':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../testlogin')

        # costtime = request.POST.get('time')
        id0 = request.POST.get('zid')
        id1 = request.POST.get('jid')

        if Newnames.objects.filter(zid=id0, jid=id1, name=teststudent):
            pass
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

        counts =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)
        nnnn = counts.count
        time0 = counts.seconds
        time1 = int(time.time())
        a = datetime.datetime.utcfromtimestamp(time0)
        b = datetime.datetime.utcfromtimestamp(time1)
        costtime =(b-a).seconds
        ornot = "已通过本节测试"
        Yuxiname.addyxname(id0, id1,teststudent,ornot,nnnn,costtime)
        try:
            Newnames.objects.filter(zid=id0,jid=id1,name=teststudent).delete()
        except:
            pass
        ms = Yuxiname.objects.filter(zid=id0, jid=id1)
        mss = Newnames.objects.filter(zid=id0, jid=id1)
        n = len(mss)
        return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1, 'mss': mss, 'n': n})

def Showwkqs3(request,id0,id1):
    id0 = id0
    id1 = id1
    if request.method == 'GET':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../../testlogin')
        timess = int(time.time())
        if Newnames.objects.filter(zid = id0,jid = id1,name = teststudent):
            try:
                count =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)

                nnn = count.count+1
                Yuxitestcount.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                Yuxitestcount.addyxcount(id0, id1,teststudent,nnn,timess)
            except:
                Yuxitestcount.addyxcount(id0, id1,teststudent,1,timess)

            qsids = []

            qs = Wkqs3.objects.filter(zid=id0 ,jid = id1)
            for e in qs:
                qsids.append(e.pk)
            wklm = Wktestlimit.objects.filter(zid=id0, jid=id1)
            limit = []
            shuffle(qsids)

            for j in wklm:
                limit.append(j.limit)
                limit.append(j.chances)
            qstext = []
            qsanswer = []
            qsid = []
            categorys = []
            qsamount = len(qs)
            zid=id0
            jid=id1
            testrm=[]
            testrms = Testrm.objects.filter(zid=id0, jid=id1)
            for f in testrms:
                testrm.append(f.testrm.url)
            for i in range(len(qsids)):
                aaaa=[]
                id00 = qsids[i]
                qss = get_object_or_404(Wkqs3,pk=id00)
                qstext.append(qss.questiontext.url)
                aaaa.append(hashlib.md5(qss.questionanswer1.encode()).hexdigest())
                aaaa.append(hashlib.md5(qss.questionanswer2.encode()).hexdigest())
                aaaa.append(hashlib.md5(qss.questionanswer3.encode()).hexdigest())
                qsanswer.append(aaaa)
                qsid.append(qss.pk)
                categorys.append(qss.category)
            # if categorys[0]==3:
            return render(request,'showqs9.html',{'categorys':json.dumps(categorys),'testrm':json.dumps(testrm),'qstext':json.dumps(qstext),'qsanswer':json.dumps(qsanswer),'qsid':qsid,'qsamount':json.dumps(qsamount),'zid':zid,'jid':jid,'limit':json.dumps(limit)})
            # else:
            #     return render(request, 'showqs4.html',
            #                   {'testrm':json.dumps(testrm),'qstext': json.dumps(qstext), 'qsanswer1': json.dumps(qsanswer1),
            #                    'qsanswer2': json.dumps(qsanswer2), 'qsid': qsid, 'qsamount': json.dumps(qsamount),
            #                    'zid': zid, 'jid': jid, 'limit': json.dumps(limit)})
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

    if request.method == 'POST':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../testlogin')

        # costtime = request.POST.get('time')
        id0 = request.POST.get('zid')
        id1 = request.POST.get('jid')

        if Newnames.objects.filter(zid=id0, jid=id1, name=teststudent):
            pass
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

        counts =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)
        nnnn = counts.count
        time0 = counts.seconds
        time1 = int(time.time())
        a = datetime.datetime.utcfromtimestamp(time0)
        b = datetime.datetime.utcfromtimestamp(time1)
        costtime =(b-a).seconds
        ornot = "已通过本节测试"
        Yuxiname.addyxname(id0, id1,teststudent,ornot,nnnn,costtime)
        try:
            Newnames.objects.filter(zid=id0,jid=id1,name=teststudent).delete()
        except:
            pass
        ms = Yuxiname.objects.filter(zid=id0, jid=id1)
        # mss = Newnames.objects.filter(zid=id0, jid=id1)
        # n = len(mss)
        return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})


def  Jfc(request,id0,id1):
    id0 = id0
    id1 = id1
    if request.method == 'GET':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../../testlogin')
        timess = int(time.time())
        if Newnames.objects.filter(zid = id0,jid = id1,name = teststudent):
            try:
                count =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)

                nnn = count.count+1
                Yuxitestcount.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                Yuxitestcount.addyxcount(id0, id1,teststudent,nnn,timess)
            except:
                Yuxitestcount.addyxcount(id0, id1,teststudent,1,timess)

            qsids = []

            qs = Wkqs4.objects.filter(zid=id0 ,jid = id1)
            for e in qs:
                qsids.append(e.pk)
            wklm = Wktestlimit.objects.filter(zid=id0, jid=id1)
            limit = []
            shuffle(qsids)

            for j in wklm:
                limit.append(j.limit)
                limit.append(j.chances)
            qstext = []
            qsanswer = []
            qsid = []
            qsamount = len(qs)
            zid=id0
            jid=id1
            testrm=[]
            testrms = Testrm.objects.filter(zid=id0, jid=id1)
            for f in testrms:
                testrm.append(f.testrm.url)
            for i in range(len(qsids)):
                aaaa=[]
                id00 = qsids[i]
                qss = get_object_or_404(Wkqs4,pk=id00)
                qstext.append(qss.questiontext)
                aaaa.append(hashlib.md5(qss.questionanswer1.encode()).hexdigest())
                aaaa.append(hashlib.md5(qss.questionanswer2.encode()).hexdigest())
                qsanswer.append(aaaa)
                qsid.append(qss.pk)
            # if categorys[0]==3:
            return render(request,'showqs10.html',{'testrm':json.dumps(testrm),'qstext':json.dumps(qstext),'qsanswer':json.dumps(qsanswer),'qsid':qsid,'qsamount':json.dumps(qsamount),'zid':zid,'jid':jid,'limit':json.dumps(limit)})
            # else:
            #     return render(request, 'showqs4.html',
            #                   {'testrm':json.dumps(testrm),'qstext': json.dumps(qstext), 'qsanswer1': json.dumps(qsanswer1),
            #                    'qsanswer2': json.dumps(qsanswer2), 'qsid': qsid, 'qsamount': json.dumps(qsamount),
            #                    'zid': zid, 'jid': jid, 'limit': json.dumps(limit)})
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

    if request.method == 'POST':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../testlogin')

        # costtime = request.POST.get('time')
        id0 = request.POST.get('zid')
        id1 = request.POST.get('jid')

        if Newnames.objects.filter(zid=id0, jid=id1, name=teststudent):
            pass
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

        counts =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)
        nnnn = counts.count
        time0 = counts.seconds
        time1 = int(time.time())
        a = datetime.datetime.utcfromtimestamp(time0)
        b = datetime.datetime.utcfromtimestamp(time1)
        costtime =(b-a).seconds
        ornot = "已通过本节测试"
        Yuxiname.addyxname(id0, id1,teststudent,ornot,nnnn,costtime)
        try:
            Newnames.objects.filter(zid=id0,jid=id1,name=teststudent).delete()
        except:
            pass
        ms = Yuxiname.objects.filter(zid=id0, jid=id1)
        # mss = Newnames.objects.filter(zid=id0, jid=id1)
        # n = len(mss)
        return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})






def Testresult(request):
    if request.method == 'POST':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../testlogin')

        costtime = request.POST.get('time')
        id0 = request.POST.get('zid')
        id1 = request.POST.get('jid')
        if Newnames.objects.filter(zid=id0, jid=id1, name=teststudent):
            pass
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

        counts =get_object_or_404(Yuxitestcount,zid = id0,jid = id1,name = teststudent)
        nnnn = counts.count
        ornot = "已通过本节测试"
        Yuxiname.addyxname(id0, id1,teststudent,ornot,nnnn,costtime)
        try:
            Newnames.objects.filter(zid=id0,jid=id1,name=teststudent).delete()
        except:
            pass
        data = {}
        data['status'] = 'success'
        return JsonResponse(data)


def showqserror(request):
    id=request.POST.get('id')
    lx = request.POST.get('categorys')
    print(lx)
    if lx==1:
        ms = get_object_or_404(Wkqs, pk=id)
        ms.wrongcount += 1
        ms.save()
    elif lx == 2:
        ms = get_object_or_404(Wkqs2, pk=id)
        ms.wrongcount+=1
        ms.save()
    else:
        ms = get_object_or_404(Wkqs3, pk=id)
        ms.wrongcount+=1
        ms.save()

    data={}
    data['status'] = lx
    return JsonResponse(data)



def yuxiname(request,id0,id1):
    id0 = id0
    id1 = id1
    ms = Yuxiname.objects.filter(zid=id0,jid=id1)
    # mss = Newnames.objects.filter(zid=id0,jid=id1)
    # n = len(mss)
    return render(request,'yuxiname.html',{'ms':ms,'id0':id0,'id1':id1})

def zkfxnametg(request,id0,id1):
    teststudent = request.session.get("teststudent")
    if teststudent:
        try:
            ggg=get_object_or_404(Yuxinamezk, zid=id0, jid=id1, name=teststudent)

            mss = teststudent + ',本次作业，'+ggg.ornot+ggg.fs+'!'
        except:
            mss = teststudent + ",你尚未完成本次作业！请抓紧时间完成！"
    else:
        mss=''
    id0 = id0
    id1 = id1
    ms = Yuxinamezk.objects.filter(zid=id0,jid=id1)
    # mss = Newnames.objects.filter(zid=id0,jid=id1)
    # n = len(mss)
    return render(request,'yuxiname2.html',{'ms':ms,'id0':id0,'id1':id1,'mss':mss})

def yuxiname0(request,id0,id1):
    teststudent = request.session.get("teststudent0")
    if teststudent:
        try:
            get_object_or_404(Yuxiname0, zid=id0, jid=id1, name=teststudent)
            mss = teststudent + ",恭喜你！已完成本次作业！"
        except:
            mss = teststudent + ",你尚未完成本次作业！请抓紧时间完成！"
    else:
        mss=''
    id0 = id0
    id1 = id1
    ms = Yuxiname0.objects.filter(zid=id0,jid=id1)
    # mss = Newnames0.objects.filter(zid=id0,jid=id1)
    # n = len(mss)
    try:
        exammessages = Yuxiname0.objects.filter(name=teststudent)
        sunn = len(exammessages)
        dates, scores = [], []
        for i in range(sunn):
            # date=datetime.strptime(exammessages[i].examtime,'"%Y.%m.%d"')
            dates.append(exammessages[i].time)
            scores.append(exammessages[i].costtime)
        dates.reverse()
        scores.reverse()
        plt.switch_backend('agg')
        fig = plt.figure(figsize=(4, 3))

        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False
        plt.plot(dates, scores, c='red')
        plt.title(teststudent + ",100题速算情况")
        fig.autofmt_xdate(rotation=85)
        plt.ylim(250, 1200)

        plt.ylabel("用时（秒）")
        plt.tick_params(axis='both', which='major', labelsize=8)
        sio = BytesIO()

        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        html = ''' <img src="data:image/png;base64,{}"/> '''
        plt.close()
        imd = html.format(data)

    except:
        imd=''
    return render(request,'xhlyuxiname.html',{'ms':ms,'id0':id0,'id1':id1,'mss':mss,'imd':imd})
def Zuji(request):
    ms = Loginrecord.objects.all()
    return render(request,'zuji.html',{'ms':ms})
def Addnames(request,id0,id1):
    zid = id0
    jid = id1
    # nameid = [20,16,32,27,9,19,22,5,10,17,15,12,14,31,13,18,24,25,11,8,7,56,60,54,53,68,63,66,58,77,67,47,52,71,65,48,61,59,64,49,51,50,55,62,23,75,57,72,26,69,73,29]
    for i in range(200):
        id = i
        try:

            names =Students.objects.filter(pk = id)
            name = names[0]
            Newnames.addname(zid=zid, jid=jid, name=name)
            Costtimels.addtime(id0=zid, id1=jid,timels=0, name=name)
        except:
            pass
    return HttpResponse("成功！")

def Addnames0(request,id0,id1):
    zid = id0
    jid = id1

    for i in range(150):
        id = i
        try:

            names =XHL.objects.filter(pk = id)
            name = names[0].name
            Newnames0.addname0(zid=zid, jid=jid, name=name)
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

def FC2(request):
    a = []
    for i in range(-30, 30, 1):
        a.append(i)
    # print(a)
    a.remove(0)
    shuffle(a)
    # fc = []
    # html=''''''

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
                    qstest = '''<a>x<SUP>2</SUP>%s</a>''' % e
                    qsanswer1 =0-num
                    qsanswer2 = 0-b
                    Wkqs4.createfc(0,0,qstest,qsanswer1,qsanswer2)
                    # fc.append(e)
                elif c < 0 and d > 0:
                    e = str(c) + "x+" + str(d) + "=" + str(0)
                    qstest = '''<a>x<SUP>2</SUP>%s</a>''' % e
                    qsanswer1 =0-num
                    qsanswer2 = 0-b
                    Wkqs4.createfc(0,0,qstest, qsanswer1, qsanswer2)
                elif c > 0 and d < 0:
                    e =  "+" + str(c) + "x" + str(d) + "=" + str(0)
                    qstest = '''<a>x<SUP>2</SUP>%s</a>''' % e
                    qsanswer1 =0-num
                    qsanswer2 = 0-b
                    Wkqs4.createfc(0,0,qstest, qsanswer1, qsanswer2)
                elif c == 0 and d < 0:
                    e = str(d) + "=" + str(0)
                    qstest = '''<a>x<SUP>2</SUP>%s</a>''' % e
                    qsanswer1 =0-num
                    qsanswer2 = 0-b
                    Wkqs4.createfc(0,0,qstest, qsanswer1, qsanswer2)
                elif c == 0 and d > 0:
                    e = "+" + str(d) + "=" + str(0)
                    qstest = '''<a>x<SUP>2</SUP>%s</a>''' % e
                    qsanswer1 =0-num
                    qsanswer2 = 0-b
                    Wkqs4.createfc(0,0,qstest, qsanswer1, qsanswer2)
                elif c < 0 and d == 0:
                    e = str(c) + "x" + "=" + str(0)
                    qstest = '''<a>x<SUP>2</SUP>%s</a>''' % e
                    qsanswer1 =0-num
                    qsanswer2 = 0-b
                    Wkqs4.createfc(0,0,qstest, qsanswer1, qsanswer2)
                elif c > 0 and d == 0:
                    e =  "+" + str(c) + "x" + "=" + str(0)
                    qstest = '''<a>x<SUP>2</SUP>%s</a>''' % e
                    qsanswer1 =0-num
                    qsanswer2 = 0-b
                    Wkqs4.createfc(0,0,qstest, qsanswer1, qsanswer2)
                else:
                    e =  str(c) + "x" + str(d) + "=" + str(0)
                    qstest = '''<a>x<SUP>2</SUP>%s</a>''' % e
                    qsanswer1 =0-num
                    qsanswer2 = 0-b
                    Wkqs4.createfc(0,0,qstest, qsanswer1, qsanswer2)
                num += 1
            else:
                num += 1
    # print("生成了" + str(len(fc)) + "个方程：")
    # return render(request,'fangcheng.html',{"html":html})
    return HttpResponse("SUCESS!")


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


def Datilogin(request):
    teststudent = request.session.get("teststudent")
    if teststudent:
        return redirect('../dt')
    if request.method=='GET':
        return render(request, 'datilogin.html')
    if request.method == "POST":
        data = {}
        phone = request.POST.get('phone')
        # pwd = request.POST.get('pwd')
        if phone.isdigit():

            # teststudent = Searchstudentid.objects.filter(phone=phone)
            try:
                teststudent = get_object_or_404(Searchstudentid, phone=phone)
            except:
                data['status'] = "success2"
                return JsonResponse(data)
            user = teststudent.student
            # teststudent=Students.objects.filter(studentname=user,studentid=pwd)

            if teststudent:
                request.session["teststudent"] = user
                data['status'] = "success3"
                return JsonResponse(data)
                # return redirect('../indexs')
            else:
                data['status'] = "success4"
                return JsonResponse(data)
                # return render(request,'questionsindex.html',{'errors':'手机号错误，或不存在！请微信群联系数学老师。'})
        else:
            data['status'] = "success1"
            return JsonResponse(data)

        # phone = request.POST.get('phone')
        # # pwd = request.POST.get('pwd')
        # if not phone.isdigit():
        #     return render(request, 'questionsindex.html', {'errors': '手机号类型错误！'})
        # # teststudent = Searchstudentid.objects.filter(phone=phone)
        # try:
        #     teststudent = get_object_or_404(Searchstudentid, phone=phone)
        # except:
        #     return render(request, 'questionsindex.html', {'errors': '手机号错误，或不存在！请微信群联系数学老师。'})
        # user = teststudent.student
        # # teststudent=Students.objects.filter(studentname=user,studentid=pwd)
        #
        # if teststudent:
        #     request.session["teststudent"] = user
        #     return redirect('../dt')
        # else:
        #     return render(request, 'questionsindex.html', {'errors': '手机号错误，或不存在！请微信群联系数学老师。'})


def Datiget(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin1')
    return render(request, 'dati.html')


def Datipost(request):
    teststudent = request.session.get("teststudent")
    data={}
    if not teststudent:
        data['status']='nologin'
        return JsonResponse(data)

    xuanx=request.POST.get('as')
    if xuanx:
        pass
    else:
        data['error']='姓名不能为空'
        data['status']='success0'
        return JsonResponse(data)
    control=Daticontrol.objects.all()
    onoff=control[0].onoff
    time1=control[0].seconds

    if onoff==0:
        datirecord=Datirecord.objects.filter(name=teststudent)
        if datirecord:
            data['status']='success1'
        else:
            time2 = int(time.time())
            costtime=time2-time1
            dtdata = get_object_or_404(Dati, pk=1)
            if xuanx == 'A':
                dtdata.a += 1
                dtdata.save()
            elif xuanx == 'B':
                dtdata.b += 1
                dtdata.save()
            elif xuanx == 'C':
                dtdata.c += 1
                dtdata.save()
            elif xuanx == 'D':
                dtdata.d += 1
                dtdata.save()
            else:
                dtdata.e += 1
                dtdata.save()
            data['status'] = 'success2'
            Datirecord.addrc(name=teststudent, xx=xuanx,costtime=costtime)
    else:
        data['status']='success3'
    return JsonResponse(data)


def Datimanage(request):
    return render(request,"datimanage.html")

def Daticount(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin1')
    data={}
    datas=Datirecord.objects.all()
    data['count']="已答题人数："+str(len(datas))
    return JsonResponse(data)
def Datistart(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin1')
    Datirecord.objects.all().delete()
    timess = int(time.time())
    sta=get_object_or_404(Daticontrol,pk=1)
    sta.onoff=0
    sta.seconds=timess
    sta.save()
    zerodata=get_object_or_404(Dati,pk=1)
    zerodata.a=0
    zerodata.b=0
    zerodata.c=0
    zerodata.d=0
    zerodata.e=0
    zerodata.save()
    data={}
    return JsonResponse(data)

def Datiend(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin1')
    staa = get_object_or_404(Daticontrol, pk=1)
    staa.onoff=1
    staa.save()
    data={}
    return JsonResponse(data)

def Datitongji(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../testlogin1')
    data = {}
    datatj=get_object_or_404(Dati,pk=1)
    a=datatj.a
    b=datatj.b
    c=datatj.c
    d=datatj.d
    e=datatj.e
    plt.switch_backend('agg')
    fig = plt.figure(figsize=(8,8))

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    labels = 'A','B','C','D','不会'
    sizes = a,b,c,d,e
    colors = 'lightgreen', 'gold', 'lightskyblue', 'lightcoral','red'
    explode = 0.1,0.1,0.1,0.1,0.1
    plt.pie(sizes, explode=explode, labels=labels,
            colors=colors, autopct='%1.1f%%', shadow=True, startangle=50,labeldistance=0.9,textprops={'fontsize':40,'color':'black'})


    plt.axis('equal')
    plt.legend(loc="upper right", fontsize=20, bbox_to_anchor=(1.11, 1.11), borderaxespad=0.11)
    sio = BytesIO()
    plt.savefig(sio, format='png')
    dat = base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}"/> '''
    plt.close()
    imd = html.format(dat)
    data['imd'] = imd
    data['status'] = "SUCCESS"
    ac="选A有："
    bc="选B有："
    cc="选C有："
    dc="选D有："
    ec="选不会有："

    datirc1 = Datirecord.objects.filter(xx='a')
    if datirc1:
        for i in range(len(datirc1)):
            ac=ac+str(datirc1[i].name)+'-'+str(datirc1[i].costtime)+","

    datirc2 = Datirecord.objects.filter(xx='b')
    if datirc2:
        for i in range(len(datirc2)):
            bc=bc+str(datirc2[i].name)+'-'+str(datirc2[i].costtime)+","
    datirc3 = Datirecord.objects.filter(xx='c')
    if datirc3:
        for i in range(len(datirc3)):
            cc=cc+str(datirc3[i].name)+'-'+str(datirc3[i].costtime)+","
    datirc4 = Datirecord.objects.filter(xx='d')
    if datirc4:
        for i in range(len(datirc4)):
            dc=dc+str(datirc4[i].name)+'-'+str(datirc4[i].costtime)+","
    datirc5 = Datirecord.objects.filter(xx='e')
    if datirc5:
        for i in range(len(datirc5)):
            ec=ec+str(datirc5[i].name)+'-'+str(datirc5[i].costtime)+","
    data['a']=ac
    data['b']=bc
    data['c']=cc
    data['d']=dc
    data['e']=ec
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



def xxtest3(request):
    if request.method=="GET":
        QS = Xxqs.objects.filter()
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

def  xxtest2(request,id0,id1):
    id0 = id0
    id1 = id1
    if request.method == 'GET':
        teststudent0 = request.session.get("teststudent0")
        if not teststudent0:
            return redirect('../../testlogin0')
        timess = int(time.time())
        if Newnames0.objects.filter(zid = id0,jid = id1,name = teststudent0):
            try:
                count =get_object_or_404(Yuxitestcount0,zid = id0,jid = id1,name = teststudent0)

                nnn = count.count+1
                Yuxitestcount0.objects.filter(zid=id0, jid=id1, name=teststudent0).delete()
                Yuxitestcount0.addyxcount0(id0, id1,teststudent0,nnn,timess)
            except:
                Yuxitestcount0.addyxcount0(id0, id1,teststudent0,1,timess)
            QS = Xxqs.objects.filter(id1=id0,id2=id1)
            answer = []
            ornot = []
            tm = []
            for i in QS:
                if i.yunsuan == 1:
                    html = '''<div style="font-size:100px">%s+%s</div>''' % (i.num0, i.num1)
                    tm.append(html)
                    ornot.append(i.ornot)
                    answer.append(i.answer)
                elif i.yunsuan == 2:
                    html = '''<div style="font-size:100px">%s-%s</div>''' % (i.num0, i.num1)
                    tm.append(html)
                    ornot.append(i.ornot)
                    answer.append(i.answer)
                elif i.yunsuan == 3:
                    html = '''<div style="font-size:100px">%s &times %s</div>''' % (i.num0, i.num1)
                    tm.append(html)
                    ornot.append(i.ornot)
                    answer.append(i.answer)
                else:
                    html = '''<div style="font-size:100px">%s &divide %s</div>''' % (i.num0, i.num1)
                    tm.append(html)
                    ornot.append(i.ornot)
                    answer.append(i.answer)

                ts = len(answer)
            wklm = Wktestlimit0.objects.filter(zid=id0, jid=id1)
            limit = []
            for j in wklm:
                limit.append(j.limit)
                limit.append(j.chances)
            return render(request, 'xxtest.html',
                          {'zid':id0,'jid':id1,'answer': json.dumps(answer), 'tm': json.dumps(tm), 'ts': ts, 'yzts': 0, 'correctamount': 0,
                           'ornot': json.dumps(ornot),'limit':json.dumps(limit)})

        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'xhlyuxi.html', {'ms': ms})

    if request.method == 'POST':
        teststudent0 = request.session.get("teststudent0")
        if not teststudent0:
            return redirect('../testlogin0')

        # costtime = request.POST.get('time')
        id0 = request.POST.get('id0')
        id1 = request.POST.get('id1')

        if Newnames0.objects.filter(zid=id0, jid=id1, name=teststudent0):
            pass
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'xhlyuxi.html', {'ms': ms})

        counts =get_object_or_404(Yuxitestcount0,zid = id0,jid = id1,name = teststudent0)
        nnnn = counts.count
        time0 = counts.seconds
        time1 = int(time.time())
        a = datetime.datetime.utcfromtimestamp(time0)
        b = datetime.datetime.utcfromtimestamp(time1)
        costtime =(b-a).seconds
        ornot = "已通过本节测试"
        Yuxiname0.addyxname0(id0, id1,teststudent0,ornot,nnnn,costtime)
        try:
            Newnames0.objects.filter(zid=id0,jid=id1,name=teststudent0).delete()
        except:
            pass
        ms = Yuxiname0.objects.filter(zid=id0, jid=id1)
        mss = Newnames0.objects.filter(zid=id0, jid=id1)
        n = len(mss)
        return render(request, 'xhlyuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1, 'mss': mss, 'n': n})

def  xxtest22(request,id0,id1):
    id0 = id0
    id1 = id1
    if request.method == 'GET':
        teststudent0 = request.session.get("teststudent0")
        if not teststudent0:
            return redirect('../../testlogin0')
        timess = int(time.time())
        if Newnames0.objects.filter(zid = id0,jid = id1,name = teststudent0):
            try:
                count =get_object_or_404(Yuxitestcount0,zid = id0,jid = id1,name = teststudent0)

                nnn = count.count+1
                Yuxitestcount0.objects.filter(zid=id0, jid=id1, name=teststudent0).delete()
                Yuxitestcount0.addyxcount0(id0, id1,teststudent0,nnn,timess)
            except:
                Yuxitestcount0.addyxcount0(id0, id1,teststudent0,1,timess)


            QS=[]
            a10 = [e1 for e1 in range(1, 821)]
            a20 = [e2 for e2 in range(1, 1702)]
            a30 = [e3 for e3 in range(1, 46)]
            a40 = [e4 for e4 in range(1, 117)]
            shuffle(a10)
            shuffle(a20)
            shuffle(a30)
            shuffle(a40)
            a1 = a10[:40]
            a2 = a20[:40]
            a3 = a30[:10]
            a4 = a40[:10]
            for i in range(40):
                ls=Xxqs2.objects.filter(pk=a1[i])
                QS.append(ls)
            for i in range(40):
                ls=Xxqs22.objects.filter(pk=a2[i])
                QS.append(ls)
            for i in range(10):
                ls=Xxqs23.objects.filter(pk=a3[i])
                QS.append(ls)
            for i in range(10):
                ls=Xxqs24.objects.filter(pk=a4[i])
                QS.append(ls)
            random.shuffle(QS)
            answer = []
            ornot = []
            tm = []
            for g in range(100):
                gg=QS[g]

                if gg[0].yunsuan == 1:
                    html = '''<div style="font-size:100px">%s+%s</div>''' % (gg[0].num0, gg[0].num1)
                    tm.append(html)
                    ornot.append(gg[0].ornot)
                    answer.append(gg[0].answer)
                elif gg[0].yunsuan == 2:
                    html = '''<div style="font-size:100px">%s-%s</div>''' % (gg[0].num0, gg[0].num1)
                    tm.append(html)
                    ornot.append(gg[0].ornot)
                    answer.append(gg[0].answer)
                elif gg[0].yunsuan == 3:
                    html = '''<div style="font-size:100px">%s &times %s</div>''' % (gg[0].num0, gg[0].num1)
                    tm.append(html)
                    ornot.append(gg[0].ornot)
                    answer.append(gg[0].answer)
                else:
                    html = '''<div style="font-size:100px">%s &divide %s</div>''' % (gg[0].num0, gg[0].num1)
                    tm.append(html)
                    ornot.append(gg[0].ornot)
                    answer.append(gg[0].answer)

            ts = len(answer)
            wklm = Wktestlimit0.objects.filter(zid=id0, jid=id1)
            limit = []
            for j in wklm:
                limit.append(j.limit)
                limit.append(j.chances)
            return render(request, 'xxtest.html',
                          {'zid':id0,'jid':id1,'answer': json.dumps(answer), 'tm': json.dumps(tm), 'ts': ts, 'yzts': 0, 'correctamount': 0,
                           'ornot': json.dumps(ornot),'limit':json.dumps(limit)})

        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'xhlyuxi.html', {'ms': ms})

    if request.method == 'POST':
        teststudent0 = request.session.get("teststudent0")
        if not teststudent0:
            return redirect('../testlogin0')

        # costtime = request.POST.get('time')
        id0 = request.POST.get('id0')
        id1 = request.POST.get('id1')

        if Newnames0.objects.filter(zid=id0, jid=id1, name=teststudent0):
            pass
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'xhlyuxi.html', {'ms': ms})

        counts =get_object_or_404(Yuxitestcount0,zid = id0,jid = id1,name = teststudent0)
        nnnn = counts.count
        time0 = counts.seconds
        time1 = int(time.time())
        a = datetime.datetime.utcfromtimestamp(time0)
        b = datetime.datetime.utcfromtimestamp(time1)
        costtime =(b-a).seconds
        ornot = "已通过本节测试"
        Yuxiname0.addyxname0(id0, id1,teststudent0,ornot,nnnn,costtime)
        try:
            Newnames0.objects.filter(zid=id0,jid=id1,name=teststudent0).delete()
        except:
            pass
        ms = Yuxiname0.objects.filter(zid=id0, jid=id1)
        mss = Newnames0.objects.filter(zid=id0, jid=id1)
        n = len(mss)
        return render(request, 'xhlyuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1, 'mss': mss, 'n': n})

def  xxtest23(request):
    if request.method == 'GET':
        teststudent0 = request.session.get("teststudent0")
        if not teststudent0:
            return redirect('../../testlogin0')
        timess = int(time.time())

        try:
            count =get_object_or_404(Yuxitestcount0,zid = 1000,jid = 1000,name = teststudent0)

            nnn = count.count+1
            Yuxitestcount0.objects.filter(zid=1000, jid=1000, name=teststudent0).delete()
            Yuxitestcount0.addyxcount0(1000, 1000,teststudent0,nnn,timess)
        except:
            Yuxitestcount0.addyxcount0(1000, 1000,teststudent0,1,timess)


        QS=[]
        a10=[e1 for e1 in range(1,821)]
        a20=[e2 for e2 in range(1,1702)]
        a30=[e3 for e3 in range(1,46)]
        a40=[e4 for e4 in range(1,117)]
        shuffle(a10)
        shuffle(a20)
        shuffle(a30)
        shuffle(a40)
        a1=a10[:40]
        a2=a20[:40]
        a3=a30[:10]
        a4=a40[:10]
        for i in range(40):
            ls=Xxqs2.objects.filter(pk=a1[i])
            QS.append(ls)
        for i in range(40):
            ls=Xxqs22.objects.filter(pk=a2[i])
            QS.append(ls)
        for i in range(10):
            ls=Xxqs23.objects.filter(pk=a3[i])
            QS.append(ls)
        for i in range(10):
            ls=Xxqs24.objects.filter(pk=a4[i])
            QS.append(ls)
        random.shuffle(QS)
        answer = []
        ornot = []
        tm = []
        for g in range(100):
            gg=QS[g]
            print(gg)

            if gg[0].yunsuan == 1:
                html = '''<div style="font-size:100px">%s+%s</div>''' % (gg[0].num0, gg[0].num1)
                tm.append(html)
                ornot.append(gg[0].ornot)
                answer.append(gg[0].answer)
            elif gg[0].yunsuan == 2:
                html = '''<div style="font-size:100px">%s-%s</div>''' % (gg[0].num0, gg[0].num1)
                tm.append(html)
                ornot.append(gg[0].ornot)
                answer.append(gg[0].answer)
            elif gg[0].yunsuan == 3:
                html = '''<div style="font-size:100px">%s &times %s</div>''' % (gg[0].num0, gg[0].num1)
                tm.append(html)
                ornot.append(gg[0].ornot)
                answer.append(gg[0].answer)
            else:
                html = '''<div style="font-size:100px">%s &divide %s</div>''' % (gg[0].num0, gg[0].num1)
                tm.append(html)
                ornot.append(gg[0].ornot)
                answer.append(gg[0].answer)

        ts = len(answer)
        wklm = Wktestlimit0.objects.filter(zid=1000, jid=1000)
        limit = []
        for j in wklm:
            limit.append(j.limit)
            limit.append(j.chances)
        return render(request, 'xxtest.html',
                      {'zid':1000,'jid':1000,'answer': json.dumps(answer), 'tm': json.dumps(tm), 'ts': ts, 'yzts': 0, 'correctamount': 0,
                       'ornot': json.dumps(ornot),'limit':json.dumps(limit)})



    if request.method == 'POST':
        teststudent0 = request.session.get("teststudent0")
        if not teststudent0:
            return redirect('../testlogin0')
        counts =get_object_or_404(Yuxitestcount0,zid = 1000,jid = 1000,name = teststudent0)
        nnnn = counts.count
        time0 = counts.seconds
        time1 = int(time.time())
        a = datetime.datetime.utcfromtimestamp(time0)
        b = datetime.datetime.utcfromtimestamp(time1)
        costtime =(b-a).seconds
        ss=Rankxhl.objects.filter(name=teststudent0)
        if ss:
            time0=get_object_or_404(Rankxhl,name=teststudent0)
            if costtime<time0.costtime:
                Rankxhl.objects.filter(name=teststudent0).delete()
                Rankxhl.addrankxhl(teststudent0,costtime)
            else:
                pass
        else:
            Rankxhl.addrankxhl(teststudent0, costtime)
        #
        #
        #
        # try:
        #     rankms=get_object_or_404(Rankxhl,name=teststudent0)
        #     if costtime<rankms.costime:
        #         Rankxhl.object.filter(name=teststudent0).delete()
        #         Rankxhl.addrankxhl(teststudent0,costtime)
        #     else:
        #         pass
        # except:
        #     Rankxhl.addrankxhl(teststudent0, costtime)
        gg=Lasttime.objects.filter(name=teststudent0)
        if gg:
            Lasttime.objects.filter(name=teststudent0).delete()
            Lasttime.addtime(teststudent0, costtime)
        else:
            Lasttime.addtime(teststudent0, costtime)

        ms0=costtime
        ms1=get_object_or_404(Rankxhl,name=teststudent0).costtime
        ms=Rankxhl.objects.all()
        return render(request, 'rankxhl.html',{'name':teststudent0,'ms0':ms0,'ms1':ms1,'ms':ms})
def rankmss(request):
    teststudent0 = request.session.get("teststudent0")
    if not teststudent0:
        return redirect('../../testlogin0')
    else:
        pass
    msag = Rankxhl.objects.all()
    summ = len(msag)
    rank = {}

    for a in range(summ):
        rank[msag[a].name] = msag[a].costtime

    rank = sorted(rank.items(), key=lambda e: e[1], reverse=True)

    scores = []
    names = []
    for i in rank:
        names.append(i[0])
        scores.append(i[1])


    plt.switch_backend('agg')
    plt.figure(figsize=(4, 13))

    matplotlib.rcParams['font.sans-serif'] = ["SimHei"]
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.barh(range(len(scores)), scores, height=0.7, color='r', alpha=0.8)
    plt.yticks(range(len(scores)), names)
    plt.xlabel("用时(秒)")
    plt.title("100题速算排行榜")
    for x, y in enumerate(scores):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}"/> '''
    plt.close()
    imd = html.format(data)
    try:
        ms0 = get_object_or_404(Lasttime,name=teststudent0).costtime
        ms1 = get_object_or_404(Rankxhl,name=teststudent0).costtime
        ms = Rankxhl.objects.all()
        return render(request, 'rankxhl.html', {'imd':imd,'ms0': ms0, 'ms1': ms1, 'ms': ms})

    except:
        ms0='-无数据-'
        ms1='-无数据-'
        ms = Rankxhl.objects.all()
        return render(request, 'rankxhl.html', {'imd':imd,'name':teststudent0,'ms0': ms0, 'ms1': ms1, 'ms': ms})


def Xhltestms(request):
    teststudent0 = request.session.get("teststudent0")
    if not teststudent0:
        return redirect('../testlogin0')

    exammessages = Yuxiname0.objects.filter(name=teststudent0)
    sunn = len(exammessages)
    dates, scores = [], []
    for i in range(sunn):
        # date=datetime.strptime(exammessages[i].examtime,'"%Y.%m.%d"')
        dates.append(exammessages[i].time)
        scores.append(exammessages[i].costtime)
    dates.reverse()
    scores.reverse()
    plt.switch_backend('agg')
    fig = plt.figure(figsize=(3.3, 3.3))

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.plot(dates, scores, c='red')
    plt.title(teststudent0+",100题速算情况")
    fig.autofmt_xdate(rotation=85)
    plt.ylim(0, 120)

    plt.ylabel("用时（秒）")
    plt.tick_params(axis='both', which='major', labelsize=8)
    sio = BytesIO()

    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    html = ''' <img src="data:image/png;base64,{}"/> '''
    plt.close()
    imd = html.format(data)

    return render(request, 'exam.html', {'exammessages': exammessages, 'imd': imd})



def addqs2(request,yunsuan):
    teststudent0 = request.session.get("teststudent0")
    if not teststudent0:
        return redirect('../../testlogin0')
    else:
        pass
    yunsuan=yunsuan
    if yunsuan==1:
        for i in range(2, 100):
            a = i

            for j in range(i, 100):

                b = j
                c = a + b
                if c <= 100:
                    e = a % 10
                    f = b % 10
                    if e + f > 10:
                        num0 = a
                        num1 = b
                        answer = c
                        f = c / 10
                        if f >= 10:
                            ornot = 3
                        elif f >= 1:
                            ornot = 2
                        else:
                            ornot=1
                        Xxqs2.addqs(num0,num1,yunsuan,answer,ornot)

                    else:
                        pass

                else:
                    pass
    elif yunsuan==2:
        a = []
        for i in range(1, 101):
            a.append(i)
        a.reverse()
        for i in range(100):
            b = a[i]
            for j in range(1, b):
                c = j
                if b - c > 10:
                    e = b % 10
                    f = c % 10
                    if e < f:
                        num0 = b
                        num1 = c
                        answer = b - c
                        f = answer / 10
                        if f >= 10:
                            ornot = 3
                        elif f >= 1:
                            ornot = 2
                        else:
                            ornot = 1
                        Xxqs22.addqs2(num0, num1, yunsuan, answer, ornot)
                    else:
                        pass
                else:
                    pass
    elif yunsuan==3:
        for i in range(2, 11):
            a = i
            for j in range(i, 11):

                b = j
                num0 = a
                num1 = b
                answer = a * b
                f = answer / 10
                if f >= 10:
                    ornot = 3
                elif f >= 1:
                    ornot = 2
                else:
                    ornot = 1
                Xxqs23.addqs3(num0, num1, yunsuan, answer, ornot)

    elif yunsuan==4:
        a = [4, 6, 8, 10, 12, 14, 16, 18, 20, 9, 12, 15, 18, 21, 24, 27, 30, 16, 20, 24, 28, 32, 36, 40, 25, 30, 35, 40,
             45, 50, 36, 42, 48, 54, 60, 49, 56, 63, 70, 64, 72, 80, 81, 90, 100]
        e = []
        for z in range(1, 11):
            e.append(z)

        for i in range(len(a)):
            b = a[i]
            for j in range(2, 11):
                c = j
                d = b / c
                if d in e:

                    num0 = b
                    num1 = c
                    answer = int(d)
                    f = answer / 10
                    if f >= 10:
                        ornot = 3
                    elif f >= 1:
                        ornot = 2
                    else:
                        ornot = 1
                    Xxqs24.addqs4(num0, num1, yunsuan, answer, ornot)

                else:
                    pass
    else:
        pass
    return HttpResponse("成功！")





def getpic(request):
    pic = []
    picss = Wkqs.objects.filter(zid=24,jid=2)
#     # print(len(picss))
#
#     # for i in picss:
#     #
#     #     a=i.questiontext.url
#     #     aa = "E:/14_env/mytest"+a
#     #     print(aa)
#     # img = cv2.imread("E:/14_env/mytest/media/questions/54B_7TErtgm.png")
    for i in picss:
        a = i.questiontext.url
        aa = "/home/mytest" + a
        # print(aa)
        img = cv2.imread(aa)
        try:
            aaa = base64.b64encode(cv2.imencode('.jpg',img)[1]).decode()
            html = ''' <img src="data:image/png;base64,{}" width="100%" height="50%"/> '''
            imd = html.format(aaa)
            pic.append(imd)
        except:
            pass

    return render(request,'testpic.html',{'pic':json.dumps(pic)})

def Xxdatasearch(request):
    if request.method == "GET":
        return render(request,"xxdata1.html")
    if request.method == "POST":
        name = request.POST.get('name')
        data = Xxdata.objects.filter(name=name)

        if data:
            biaoti = data[0].category
            return render(request, "xxdata2.html", {'data': data,'biaoti':biaoti})
        else:
            return render(request, "xxdata1.html", {'error': "姓名输入错误或不存信息,请重新查询！"})

def Addxhl2(request): #注册学生
    mss=XHL.objects.all()
    if mss :
        return render(request,'xhl.html',{'mss':mss})
    else:
        return render(request,'xhl.html')


def Addxhl0(request):
    data={}
    name=request.POST.get('name')
    if name:
        pass
    else:
        data['error']='姓名不能为空'
        data['status']='error'
        return JsonResponse(data)
    classs=request.POST.get('classs')
    phone=request.POST.get('phone')
    if phone.isdigit():
        pass
    else:
        data['error']='手机号只能是数字'
        data['status']='error'
        return JsonResponse(data)

    XHL.createms(name,classs,phone)
    data['status'] = 'success'
    return JsonResponse(data)


def zkfx(request,id0,id1):
    id0 = id0
    id1 = id1
    if request.method == 'GET':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../../testlogin')
        timess = int(time.time())
        timels0=Costtimels.objects.filter(id0=id0,id1=id1,name=teststudent)
        if timels0:
            pass
        else:
            Costtimels.addtime(id0=id0,id1=id1,timels=0,name=teststudent)
        if Newnames.objects.filter(zid = id0,jid = id1,name = teststudent):
            try:
                Yuxitestcount.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                Yuxitestcount.addyxcount(id0, id1,teststudent,0,timess)
            except:
                Yuxitestcount.addyxcount(id0, id1,teststudent,1,timess)

            shuxing=Zktishu.objects.filter(id0=id0,id1=id1)
            id2=shuxing[0].id2
            id3=shuxing[0].id3
            ts = shuxing[0].ts
            zs = shuxing[0].zs
            qstext = []
            qsanswer = []
            qsid = []
            qsid0 = []
            try:
                zbhf=get_object_or_404(Zbhf,id0=id0,id1=id1)
                ornot=zbhf.ornot
            except:
                ornot=0
            if id2==1  and id3==1:
                ts2=0
                tss=Zkfx.objects.all()
                for e in tss:
                    ts2=ts2+1
                    qsid0.append(e.pk)

                a1=qsid0[-ts:]
                shuffle(a1)
                a1=a1[-zs:]
                for i in range(zs):
                    qs=get_object_or_404(Zkfx,pk=a1[i])
                    qstext.append(qs.questiontext.url)
                    qsanswer.append(hashlib.md5(qs.questionanswer.encode()).hexdigest())
                    qsid.append(a1[i])
                return render(request, 'showqszk.html',                              {
                               'qstext': json.dumps(qstext), 'qsanswer': json.dumps(qsanswer),'qsid':qsid,
                               'qsamount': json.dumps(zs),'id0':id0,'id1':id1,'ornot':ornot})
            elif id2==0  and id3==0:
                ts2=0
                tss=Zkfx.objects.all()
                for e in tss:
                    ts2=ts2+1
                    qsid0.append(e.pk)
                if ts>ts2:
                    ts=ts2
                else:
                    pass
                shuffle(qsid0)
                a1=qsid0[:ts]
                for i in range(ts):
                    qs=get_object_or_404(Zkfx,pk=a1[i])
                    qstext.append(qs.questiontext.url)
                    qsanswer.append(hashlib.md5(qs.questionanswer.encode()).hexdigest())
                    qsid.append(a1[i])
                return render(request, 'showqszk.html',                              {
                               'qstext': json.dumps(qstext), 'qsanswer': json.dumps(qsanswer),'qsid':qsid,
                               'qsamount': json.dumps(ts),'id0':id0,'id1':id1,'ornot':ornot})
            elif id3==0:
                ts2=0
                a2=[]
                tss=Zkfx.objects.filter(id2=id2)
                for e in tss:
                    a2.append(e.pk)
                    ts2=ts2+1
                if ts>ts2:
                    ts=ts2
                else:
                    pass
                shuffle(a2)
                a3=a2[:ts]
                for jj in range(len(a3)):
                    qs = get_object_or_404(Zkfx, pk=a3[jj])
                    qstext.append(qs.questiontext.url)
                    qsanswer.append(hashlib.md5(qs.questionanswer.encode()).hexdigest())
                    qsid.append(a3[jj])
                return render(request, 'showqszk.html', {
                    'qstext': json.dumps(qstext), 'qsanswer': json.dumps(qsanswer), 'qsid': qsid,
                    'qsamount': json.dumps(ts),'id0':id0,'id1':id1,'ornot':ornot})
            elif id2==0:
                ts3=0
                a3=[]
                tss=Zkfx.objects.filter(id3=id3)
                for e in tss:
                    a3.append(e.pk)
                    ts3=ts3+1
                if ts>ts3:
                    ts=ts3
                else:
                    pass
                shuffle(a3)
                a4=a3[:ts]
                for jj in range(len(a4)):
                    qs = get_object_or_404(Zkfx, pk=a4[jj])
                    qstext.append(qs.questiontext.url)
                    qsanswer.append(hashlib.md5(qs.questionanswer.encode()).hexdigest())
                    qsid.append(a4[jj])
                return render(request, 'showqszk.html', {
                    'qstext': json.dumps(qstext), 'qsanswer': json.dumps(qsanswer), 'qsid': qsid,
                    'qsamount': json.dumps(ts),'id0':id0,'id1':id1,'ornot':ornot})
            else:
                return HttpResponse("请求失败！")
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

    # if request.method=="POST":

    if request.method == 'POST':
        teststudent = request.session.get("teststudent")
        if not teststudent:
            return redirect('../testlogin')

        # costtime = request.POST.get('time')
        id0 = request.POST.get('zid')
        id1 = request.POST.get('jid')
        ts = request.POST.get('ts')
        dd = request.POST.get('dd')
        dd=int(dd)
        wrong = request.POST.get('wrong')
        wrongs=wrong.split(",")
        print(wrongs)

        if Newnames.objects.filter(zid=id0, jid=id1, name=teststudent):
            pass
        else:
            ms = '已通过本节测试，无需重复测试！可前往尚未测试的'
            return render(request, 'yuxi.html', {'ms': ms})

        for fff in range(len(wrongs)):
            if wrongs[fff]:
                jjs = get_object_or_404(Zkfx, pk=wrongs[fff])
                jjs.wrongcount = jjs.wrongcount + 1
                jjs.save()
            else:
                pass
        counts = get_object_or_404(Yuxitestcount, zid=id0, jid=id1, name=teststudent)
        time0 = counts.seconds
        time1 = int(time.time())
        a = datetime.datetime.utcfromtimestamp(time0)
        b = datetime.datetime.utcfromtimestamp(time1)
        costtime = (b - a).seconds
        timelimit=get_object_or_404(Timelimitzk,id0=id0,id1=id1)
        limit1=timelimit.limit1
        limit2=timelimit.limit2
        timelss=get_object_or_404(Costtimels,id0=id0,id1=id1,name=teststudent)
        timelss.timels=timelss.timels+costtime
        timelss.save()

        if dd>=int(0.95*float(ts)):
            try:
                Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
            except:
                pass
            fs="优秀"

            ornot = "通过，"
            timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
            costtime2=timelss2.timels

            Yuxinamezk.addyxname(id0, id1, teststudent, ornot, fs, costtime2)
            Costtimels.objects.filter(id0=id0, id1=id1, name=teststudent).delete()

            try:
                Newnames.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
            except:
                pass
            # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
            paths='../../zkfxnametg/'+str(id0)+'/'+str(id1)
            return redirect(paths)

            # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})


        elif dd>=int(0.85*float(ts)):
            try:
                Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
            except:
                pass
            fs="良好"

            ornot = "通过，"
            timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
            costtime2=timelss2.timels

            Yuxinamezk.addyxname(id0, id1, teststudent, ornot, fs, costtime2)
            Costtimels.objects.filter(id0=id0, id1=id1, name=teststudent).delete()


            try:
                Newnames.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
            except:
                pass
            paths='../../zkfxnametg/'+str(id0)+'/'+str(id1)
            return redirect(paths)
            # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
            #
            # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})

        elif dd>=int(0.75*float(ts)):

            if costtime>=limit1:
                ornot = "通过，"
                fs="及格"

                try:
                    Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                except:
                    pass
                timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
                costtime2 = timelss2.timels

                Yuxinamezk.addyxname(id0, id1, teststudent, ornot, fs, costtime2)
                Costtimels.objects.filter(id0=id0, id1=id1, name=teststudent).delete()


                try:
                    Newnames.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                except:
                    pass
                paths = '../../zkfxnametg/' + str(id0) + '/' + str(id1)
                return redirect(paths)
                # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
                #
                # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})
            else:
                try:
                    Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                except:
                    pass
                ornot="不通过，"
                fs="重做!"
                timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
                costtime2 = timelss2.timels

                Yuxinamezk.addyxname(id0, id1, teststudent, ornot, fs, costtime2)
                paths = '../../zkfxnametg/' + str(id0) + '/' + str(id1)
                return redirect(paths)

                # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
                #
                #
                # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})
        else:
            try:
                Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
            except:
                pass
            if costtime>limit2:
                ornot = "通过，"
                fs="及格"
                try:
                    Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                except:
                    pass
                timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
                costtime2 = timelss2.timels

                Yuxinamezk.addyxname(id0, id1, teststudent, ornot, fs, costtime2)
                Costtimels.objects.filter(id0=id0, id1=id1, name=teststudent).delete()

                try:
                    Newnames.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                except:
                    pass
                paths = '../../zkfxnametg/' + str(id0) + '/' + str(id1)
                return redirect(paths)
                # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
                #
                # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})
            else:
                try:
                    Yuxinamezk.objects.filter(zid=id0, jid=id1, name=teststudent).delete()
                except:
                    pass
                fs = "重做!"
                ornot = "不通过，"
                timelss2 = get_object_or_404(Costtimels, id0=id0, id1=id1, name=teststudent)
                costtime2 = timelss2.timels

                Yuxinamezk.addyxname(id0, id1, teststudent, ornot, fs, costtime2)
                paths = '../../zkfxnametg/' + str(id0) + '/' + str(id1)
                return redirect(paths)

                # ms = Yuxinamezk.objects.filter(zid=id0, jid=id1)
                #
                # return render(request, 'yuxiname2.html', {'ms': ms, 'id0': id0, 'id1': id1})


def zkfxname(request):
    teststudent = request.session.get("teststudent")
    if not teststudent:
        return redirect('../../testlogin')
    if request.method=='GET':
        return render(request,'zkfxname.html')
    if request.method=='POST':
        id0 = request.POST.get('id0')
        id1 = request.POST.get('id1')

        mss = Newnames.objects.filter(zid=id0, jid=id1)
        n = len(mss)
        msss=Yuxinamezk.objects.filter(zid=id0,jid=id1,fs = "重做!")
        namwz=[]
        nameid = ['梁雨欣', '梁宇昊',  '朱语涵', '颜千', '梁君豪', '吴家辉', '王佳英',  '梁悦然', '梁心怡', '陈茜', '陈柯宇', '张航', '芦美婷', '梁炜兴', '蔡雨航', '梁鑫宇', '马成作', '罗欣', '缪可盈', '应彤彤', '李丞卿', '吴佳欣', '梁嘉妮', '周荣欢', '梁雨轩', '郏琪隆',  '陈优优', '梁航瑜', '徐权俊', '陈依琳', '黄紫怡', '梁晶', '厉涵婷', '周乐', '毛宇迪', '梁旖康', '徐梦婷', '金琦峰', '梁迈之', '吴妙建', '丁雨晴', '李程凯', '陈怡兴', '应璐忆', '王海滔', '韩雨欣', '陈昕妤', '吴嘉乐', '徐纯耀', '沈昊哲', '陈佳意', '梁宇帆', '陈安琪', '廖伟丹', '陈培鑫', '杨奇钢', '徐晨皓', '沈佳雪', '汪可柠', '梁家律']
        for name in range(len(nameid)):
            if Newnames.objects.filter(zid=id0, jid=id1,name=nameid[name]):
                namwz.append(nameid[name])
            else:
                pass
        return render(request, 'zkfxname.html', {'mss': mss, 'n':n,'msss':msss,'namwz':namwz})

