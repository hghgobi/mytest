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
import datetime
#import mpld3
import base64
from io import BytesIO
import os,qrcode,image


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
    homeworkmessagesum = Homeworksum.objects.filter(student_name__studentname=teststudent)
    return render(request,'homework.html',{'homeworkmessages':homeworkmessages,'homeworkmessagesum':homeworkmessagesum})

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
    if score == 'A+ 很认真':
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
    if score == 'A+ 很认真':
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

def zuotu1(request):
    fig=Figure(figsize=(6,6))
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvasAgg(fig)
    response=HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    plt.close(fig)
    return response
def zuotu2(request):
    fig=Figure(figsize=(6,6))
    ax = fig.add_subplot() 
    ax.legend(loc='center left', bbox_to_anchor=(1,0.5))
    y=[1,4,9,16,25]
    x=[1,2,3,4,5]
    ax.plot(x, y, linewidth=2)
    canvas=FigureCanvasAgg(fig)
    response=HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)

    #html_graph = mpld3.fig_to_html(fig)
    plt.close(fig)



    return response
    #return render(request, 'tupiancs.html', {'html_graph':html_graph})
    #return render(request,'tupiancs.html',{'canvas':canvas})
def zuotu3(request):
    fig=Figure(figsize=(6,6))
    ax = fig.add_subplot() 
    ax.legend(loc='center left', bbox_to_anchor=(1,0.5))
    y=[1,4,9,16,25]
    x=[1,2,3,4,5]
    ax.plot(x, y, linewidth=2)
    sigma_spec=int(0.5)
    plot_data = multiChart(data,sigma_spec)
    plt.figure(figsize=(12,9))
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = base64.b64encode(plot_data)
    ims = imb.decode()
    imd = "data:image/png;base64,"+ims
    return render(request, "tupiancs.html",{"img":imd})
def multiChart(data,sigma_spec):
    plt.figure(figsize=(12,9))
    plt.subplot(311)
    plt.title("CTC Array FAB H3PO4 Monitor for BP Lack")
    plt.plot(data["time"],data["mean"],color="b",marker="*")
    plt.subplot(312)
    data["slope_spec"]=0
    plt.title("$mean{(y2-y1)}$")
    plt.plot(data["time"],data["slope"],color="b")
    plt.plot(data["time"],data["slope_spec"],color="r")
    plt.subplot(313)
    data["sigma_spec"]=sigma_spec
    plt.title("3$sigma$")
    plt.plot(data["time"],data["3sigma"],color="b")
    plt.plot(data["time"],data["sigma_spec"],color="r")
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    return plot_data

def makeQrcode(request):
    try:
        url = "1 A"
        filename = "./static/" + str(base64.b64encode(str(url).encode('utf-8')), 'utf-8')+'.png'
        if os.path.exists(filename):
            qrimg_data = open(filename, 'rb').read()
            return HttpResponse(qrimg_data, content_type="image/png")
        else:
            qr = qrcode.QRCode(version=1,
                               error_correction=qrcode.ERROR_CORRECT_L,
                               box_size=8,
                               border=8)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(filename)
            if os.path.exists(filename):
                qrimg_data = open(filename, 'rb').read()
                return HttpResponse(qrimg_data, content_type="image/png")
    except Exception as  e:
        return HttpResponse(str(e))






        
        
            

            
        


    