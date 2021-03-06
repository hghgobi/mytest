from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Q

# Create your models here.
class Classes(models.Model):
	classname=models.CharField(max_length = 50)
	teachername=models.CharField(max_length = 50)
	
	def __str__(self):
		return self.classname
	class Meta:
		ordering = ['id']
	@classmethod
	def createClass(cls,name,teach):
		clname =cls(classname = name,teachername = teach)
		clname.save()
		return clname
   
class Courses(models.Model):
	coursename = models.CharField(max_length=50)
	#coursescore = models.IntegerField()

	def __str__(self):
		return self.coursename

class Students(models.Model):
	studentname = models.CharField(max_length=50)
	studentid = models.IntegerField()
	studentclass = models.ForeignKey(Classes,on_delete=models.DO_NOTHING)
	
	
	def __str__(self):
		return self.studentname

class Homework(models.Model):
	homeworkname = models.CharField(max_length=200)
	homeworkscore = models.CharField(max_length=50)
	homeworktime =models.DateTimeField(auto_now_add=True)
	homeworkstudent = models.ForeignKey(Students,on_delete=models.DO_NOTHING)
	class Meta:
		ordering = ['-homeworktime']
		get_latest_by=['homeworktime']
	@classmethod
	def createhomework(cls,idd,score,homeworkname):
		name = Students.objects.filter(pk=idd)
		homeworkstudent=name[0]
		homework = cls(homeworkstudent=homeworkstudent,homeworkscore=score,homeworkname=homeworkname)
		homework.save()
		return homework

class Classingss(models.Model):
	classname = models.CharField(max_length=200)
	classscore = models.CharField(max_length=200)
	classtime =models.DateTimeField(auto_now_add=True)
	classstudent = models.ForeignKey(Students,on_delete=models.DO_NOTHING)
	class Meta:
		ordering = ['-classtime']
	@classmethod
	def createclass(cls,idd,score,classname):
		name = Students.objects.filter(pk=idd)
		classstudent=name[0]
		addclass = cls(classstudent=classstudent,classscore=score,classname=classname)
		addclass.save()
		return addclass
		
		
	

class Exams(models.Model):
	examname = models.CharField(max_length=200)
	examscore = models.IntegerField()
	examtime = models.CharField(max_length=200)
	examstudent = models.ForeignKey(Students,on_delete=models.DO_NOTHING)
	rank = models.IntegerField()
	class Meta:
		ordering = ['-id']




class Classnotes(models.Model):
	notename = models.CharField(max_length=200)
	notecontent = RichTextUploadingField()
	notetime = models.DateTimeField(auto_now_add=True)
	noteupdatetime = models.DateTimeField(auto_now=True)
	readed_num =models.IntegerField(default=0)
	bans = models.IntegerField()

	def __str__(self):
		return self.notename
	class Meta:
		ordering = ['-id']
#在线测试

class Classnotes0(models.Model):
	notename = models.CharField(max_length=200)
	notecontent = RichTextUploadingField()
	notetime = models.DateTimeField(auto_now_add=True)
	noteupdatetime = models.DateTimeField(auto_now=True)
	readed_num =models.IntegerField(default=0)
	def __str__(self):
		return self.notename
	class Meta:
		ordering = ['-id']
class onlinetestgrade(models.Model):
	gradename= models.CharField(max_length=50)
	def __str__(self):
		return self.gradename

class onlinetestlist(models.Model):
	listname = models.CharField(max_length = 200)
	listgrade = models.ForeignKey(onlinetestgrade,on_delete=models.DO_NOTHING)
	def __str__(self):
		return self.listname

class Questions(models.Model):
	questionid = models.IntegerField()
	questiontext = models.ImageField(upload_to='questions')
	questionanswer = models.CharField(max_length=50)
	questiongrade = models.ForeignKey(onlinetestgrade,on_delete=models.DO_NOTHING)
	questiontestlist = models.ForeignKey(onlinetestlist,on_delete=models.DO_NOTHING)
class Wkqs(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	category = models.IntegerField(default=0)
	questiontext = models.ImageField(upload_to='questions')
	questionanswer = models.CharField(max_length=50)
	wrongcount = models.IntegerField(default=1)
class Wkqs2(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	questiontext = models.ImageField(upload_to='questions')
	questionanswer1 = models.CharField(max_length=50)
	questionanswer2 = models.CharField(max_length=50)
	wrongcount = models.IntegerField(default=0)
	category = models.IntegerField(default=2)

class Wkqs3(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	questiontext = models.ImageField(upload_to='questions')
	questionanswer1 = models.CharField(max_length=50)
	questionanswer2 = models.CharField(max_length=50)
	questionanswer3 = models.CharField(max_length=50)
	wrongcount = models.IntegerField(default=0)
	category = models.IntegerField(default=3)
class Wkqs4(models.Model):
	zid = models.IntegerField(default=0)
	jid = models.IntegerField(default=0)
	questiontext = models.CharField(max_length=500)
	questionanswer1 = models.CharField(max_length=50)
	questionanswer2 = models.CharField(max_length=50)


	@classmethod
	def createfc(cls,zid,jid,questiontext,questionanswer1,questionanswer2):
		addfc = cls(zid=zid,jid=jid,questiontext=questiontext,questionanswer1=questionanswer1,questionanswer2=questionanswer2)
		addfc.save()
		return addfc

class Testrm(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	testrm = models.ImageField(upload_to='questions')


class Wktestlimit(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	limit = models.IntegerField()
	chances = models.IntegerField()

class Wktestlimit0(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	limit = models.IntegerField()
	chances = models.IntegerField()

class Scores(models.Model):
	testscore = models.IntegerField()
	scoreid = models.CharField(max_length=100)
	scorename = models.CharField(max_length=100)
	scoretime =models.DateTimeField(auto_now_add=True)
	scoreupdatetime =models.DateTimeField(auto_now=True)
	correctpercent=models.DecimalField(max_digits=3,decimal_places=2)
	testamount=models.IntegerField()
	class Mata:
		ordering=['-testscore']

	@classmethod
	def createscore(cls,teststudent,score,scoreid,correctpercent,testamount):
		names=Scores.objects.filter(scorename=teststudent)
		if names:
			if names[0].testscore<=int(score):
				#names[0].testscore=score
				#names[0].correctpercent=correctpercent
				#names[0].testamount=testamount
				#names[0].save()
				names.delete()
				clscore =cls(scorename=teststudent,testscore = score,scoreid=scoreid,correctpercent=correctpercent,testamount=testamount)
				clscore.save()
				return clscore

			else:
				pass
			
		else:
			clscore =cls(scorename=teststudent,testscore = score,scoreid=scoreid,correctpercent=correctpercent,testamount=testamount)
			clscore.save()
			return clscore
     
class Searchstudentid(models.Model):
	phone = models.BigIntegerField()
	student= models.CharField(max_length=200)
	studentid = models.IntegerField()
	def __str__(self):
		return self.student

class Loginrecord(models.Model):
	logintime = models.DateTimeField(auto_now_add=True)
	lastlogintime=models.DateTimeField(auto_now=True)
	loginuser = models.CharField(max_length=50)
	logincount = models.IntegerField(default=0)
	class Meta:
		ordering=['-lastlogintime']
class Homeworksum(models.Model):
	student_name = models.ForeignKey(Students,on_delete=models.DO_NOTHING)
	lasttime=models.DateTimeField(auto_now=True)
	aacount = models.IntegerField(default=0)

	acount = models.IntegerField(default=0)
	bcount = models.IntegerField(default=0)
	ccount = models.IntegerField(default=0)
	dcount = models.IntegerField(default=0)
	ecount = models.IntegerField(default=0)
	fcount = models.IntegerField(default=0)
	class Meta:
		ordering=['-lasttime']

class TXL(models.Model):
	name=models.CharField(max_length=200)
	company=models.CharField(max_length=200)
	major=models.CharField(max_length=200)
	gdtime=models.CharField(max_length=200)
	phone1=models.BigIntegerField()
	phone2=models.BigIntegerField()
	addtime = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['-addtime']
	@classmethod
	def createms(cls,name,company,major,gdtime,phone1,phone2):
		names=TXL.objects.filter(name=name)
		if names :
			names.delete()
			addms = cls(name=name, company=company, major=major, gdtime=gdtime, phone1=phone1, phone2=phone2)
			addms.save()
			return addms
		else:
			addms = cls(name=name, company=company, major=major, gdtime=gdtime, phone1=phone1, phone2=phone2)
			addms.save()
			return addms
class guoguanname(models.Model):
	name = models.CharField(max_length=100)
	#coursescore = models.IntegerField()
	idd = models.IntegerField()

	def __str__(self):
		return self.name

class guoguan(models.Model):
	student_name = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
	guoguan_name = models.ForeignKey(guoguanname, on_delete=models.DO_NOTHING)
	ornot = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-time']
	@classmethod
	def addgg(cls,namesss,contentid):
		ms = guoguan.objects.filter(Q(student_name__studentname=namesss) & Q(guoguan_name__idd=contentid))
		ms.delete()
		namect=guoguanname.objects.filter(idd=contentid)[0]
		addms = cls(student_name=namesss,guoguan_name=namect,ornot="jghhj")
		addms.save()
		return addms

class rankq(models.Model):
	student_name = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
	fenlei = models.CharField(max_length=100)
	score = models.IntegerField()
	time = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['score']

class addrankqdetail(models.Model):
	name = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
	detail = models.CharField(max_length=200)
	time = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['time']


	@classmethod
	def addd(cls,detail,name):

		addms = cls(detail=detail,name=name)
		addms.save()
		return addms


class badhomework(models.Model):
	time0 = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	stu_id = models.CharField(max_length=100)
	student_name = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
	ms = models.CharField(max_length=200)
	ornot = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['time']

	@classmethod
	def addbadhomework(cls,time0,name,stu_id,student_name,ornot,ms):

		addms = cls(time0=time0,name=name,stu_id=stu_id,student_name=student_name,ornot=ornot,ms=ms)
		addms.save()
		return addms


class Yuxiname(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	name = models.CharField(max_length=200)
	ornot = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now=True)
	count = models.IntegerField(default=0)
	costtime = models.IntegerField(default=0)

	class Meta:
		ordering = ['-time']

	@classmethod
	def addyxname(cls,zid,jid,name,ornot,count,costtime):

		addms = cls(zid=zid,jid=jid,name=name,ornot=ornot,count=count,costtime=costtime)
		addms.save()

class Yuxiname0(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	name = models.CharField(max_length=200)
	ornot = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now=True)
	count = models.IntegerField(default=0)
	costtime = models.IntegerField(default=0)

	class Meta:
		ordering = ['-time']

	@classmethod
	def addyxname0(cls,zid,jid,name,ornot,count,costtime):

		addms = cls(zid=zid,jid=jid,name=name,ornot=ornot,count=count,costtime=costtime)
		addms.save()

class Yuxinamezk(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	bj = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	ornot = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now=True)
	fs = models.CharField(max_length=200)
	costtime = models.IntegerField(default=0)
	count = models.IntegerField(default=0)

	class Meta:
		ordering = ['fs','count','costtime']

	@classmethod
	def addyxname(cls,bj,zid,jid,name,ornot,fs,costtime,count):

		addms = cls(bj=bj,zid=zid,jid=jid,name=name,ornot=ornot,fs=fs,costtime=costtime,count=count)
		addms.save()


class Yuxitestcount(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	name = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now=True)
	count = models.IntegerField(default=0)
	seconds = models.BigIntegerField(default=0)



	class Meta:
		ordering = ['-time']

	@classmethod
	def addyxcount(cls,zid,jid,name,count,seconds):

		addms = cls(zid=zid,jid=jid,name=name,count=count,seconds=seconds)
		addms.save()



class Newnames(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	bj = models.IntegerField(default=0)
	name = models.CharField(max_length=200)

	@classmethod
	def addname(cls,zid,jid,bj,name):

		addms = cls(zid=zid,jid=jid,bj=bj,name=name)
		addms.save()
		return addms
class Costtimels(models.Model):
	id0 = models.IntegerField()
	id1 = models.IntegerField()
	timels = models.IntegerField()
	name=models.CharField(max_length=200)

	@classmethod
	def addtime(cls,id0,id1,timels,name):

		addms = cls(id0=id0,id1=id1,timels=timels,name=name)
		addms.save()
		return addms

class Newnames0(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	name = models.CharField(max_length=200)

	@classmethod
	def addname0(cls,zid,jid,name):

		addms = cls(zid=zid,jid=jid,name=name)
		addms.save()
		return addms

class Yuxitestcount0(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	name = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now=True)
	count = models.IntegerField(default=0)
	seconds = models.BigIntegerField(default=0)



	class Meta:
		ordering = ['-time']

	@classmethod
	def addyxcount0(cls,zid,jid,name,count,seconds):

		addms = cls(zid=zid,jid=jid,name=name,count=count,seconds=seconds)
		addms.save()

class Leavems(models.Model):
	name = models.CharField(max_length=50)
	text = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=50)
	ornot = models.CharField(max_length=50)

	class Meta:
		ordering = ['-time']

	@classmethod
	def addms(cls,name,text,category,ornot):

		addms = cls(name=name,text=text,category=category,ornot=ornot)
		addms.save()

class Xxqs(models.Model):
	id1 = models.IntegerField()
	id2 = models.IntegerField()
	num0 = models.IntegerField()
	num1 = models.IntegerField()
	yunsuan = models.IntegerField()
	answer = models.IntegerField(default=0)
	ornot = models.IntegerField(default=0)

class Xxqs2(models.Model):
	num0 = models.IntegerField()
	num1 = models.IntegerField()
	yunsuan = models.IntegerField()
	answer = models.CharField(max_length=500)
	ornot = models.IntegerField(default=0)

	@classmethod
	def addqs(cls,num0,num1,yunsuan,answer,ornot):

		addqs = cls(num0=num0,num1=num1,yunsuan=yunsuan,answer=answer,ornot=ornot)
		addqs.save()
class Xxqs22(models.Model):
	num0 = models.IntegerField()
	num1 = models.IntegerField()
	yunsuan = models.IntegerField()
	answer = models.CharField(max_length=500)
	ornot = models.IntegerField(default=0)

	@classmethod
	def addqs2(cls,num0,num1,yunsuan,answer,ornot):

		addqs2 = cls(num0=num0,num1=num1,yunsuan=yunsuan,answer=answer,ornot=ornot)
		addqs2.save()
class Xxqs23(models.Model):
	num0 = models.IntegerField()
	num1 = models.IntegerField()
	yunsuan = models.IntegerField()
	answers = models.CharField(max_length=500)
	ornot = models.IntegerField(default=0)

	@classmethod
	def addqs3(cls,num0,num1,yunsuan,answer,ornot):

		addqs3 = cls(num0=num0,num1=num1,yunsuan=yunsuan,answers=answer,ornot=ornot)
		addqs3.save()

class Xxqs24(models.Model):
	num0 = models.IntegerField()
	num1 = models.IntegerField()
	yunsuan = models.IntegerField()
	answer = models.CharField(max_length=500)
	ornot = models.IntegerField(default=0)

	@classmethod
	def addqs4(cls,num0,num1,yunsuan,answer,ornot):

		addqs4 = cls(num0=num0,num1=num1,yunsuan=yunsuan,answer=answer,ornot=ornot)
		addqs4.save()
class Xxdata(models.Model):
	category = models.CharField(max_length=500)
	name = models.CharField(max_length=500)
	kaoqin = models.IntegerField()
	kaohui = models.IntegerField()
	shijia = models.IntegerField()
	bingjia = models.IntegerField()
	hunjia= models.IntegerField()
	sangjia = models.IntegerField()
	chanjia = models.IntegerField()
	hulijia = models.IntegerField()
	summ = models.IntegerField()

class XHL(models.Model):
	name=models.CharField(max_length=200)
	classs=models.CharField(max_length=200)
	phone=models.BigIntegerField()
	addtime = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['-addtime']
	@classmethod
	def createms(cls,name,classs,phone):
		names=XHL.objects.filter(name=name)
		if names :
			names.delete()
			addms = cls(name=name,classs=classs , phone=phone)
			addms.save()
			return addms
		else:
			addms = cls(name=name,classs=classs , phone=phone)
			addms.save()
			return addms


class Rankxhl(models.Model):
	name = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now=True)
	costtime = models.IntegerField(default=0)
	zid= models.IntegerField(default=0)
	jid = models.IntegerField(default=0)

	class Meta:
		ordering = ['costtime']

	@classmethod
	def addrankxhl(cls,name,costtime,zid,jid):

		addms = cls(name=name,costtime=costtime,zid=zid,jid=jid)
		addms.save()
class Lasttime(models.Model):
	name = models.CharField(max_length=200)
	costtime = models.IntegerField(default=0)
	time = models.DateTimeField(auto_now=True)
	@classmethod
	def addtime(cls,name,costtime):

		addms = cls(name=name,costtime=costtime)
		addms.save()

class Zkfx(models.Model):
	id2 = models.IntegerField()
	id3 = models.IntegerField()
	questiontext = models.ImageField(upload_to='questions')
	questionanswer = models.CharField(max_length=50)
	wrongcount = models.IntegerField(default=0)
        	
class Zktishu(models.Model):
	id0 = models.IntegerField()
	id1 = models.IntegerField()
	id2 = models.IntegerField()
	id3 = models.IntegerField()
	id4 = models.IntegerField(default=0)
	ts = models.IntegerField()
	zs = models.IntegerField(default=0)

class Timelimitzk(models.Model):
	id0 = models.IntegerField()
	id1 = models.IntegerField()
	limit1 = models.IntegerField()
	limit2 = models.IntegerField()
	limit3 = models.IntegerField(default=0)


class Dati(models.Model):
	a = models.IntegerField(default=0)
	b = models.IntegerField(default=0)
	c = models.IntegerField(default=0)
	d = models.IntegerField(default=0)
	e = models.IntegerField(default=0)
	@classmethod
	def adddt(cls, a, b,c,d,e):
		addms = cls(a=a,b=b,c=c,d=d,e=e)
		addms.save()
class Daticontrol(models.Model):
	onoff = models.IntegerField(default=0)
	seconds = models.BigIntegerField(default=0)
	@classmethod
	def adddt(cls, onoff,seconds):
		addms = cls(onoff=onoff,seconds=seconds)
		addms.save()
class Datirecord(models.Model):
	name=models.CharField(max_length=50)
	xx=models.CharField(max_length=50)
	costtime = models.IntegerField(default=0)
	class Meta:
		ordering = ['costtime']
	@classmethod
	def addrc(cls,name,xx,costtime):
		addms = cls(name=name,xx=xx,costtime=costtime)
		addms.save()
		
class Zbhf(models.Model):
	id0 = models.IntegerField()
	id1 = models.IntegerField()
	ornot = models.IntegerField(default=0)
	@classmethod
	def addhf(cls,id0,id1,ornot):
		addms = cls(id0=id0,id1=id1,ornot=ornot)
		addms.save()

class Kzms(models.Model):
	name=models.CharField(max_length=500)
	idNumber=models.CharField(max_length=500)
	phone=models.CharField(max_length=500)
	address=models.CharField(max_length=500)
	addressDetail=models.CharField(max_length=500)
	addressCode=models.CharField(max_length=500)
	@classmethod
	def addms(cls,name,idNumber,phone,address,addressDetail,addressCode):
		addms = cls(name=name,idNumber=idNumber,phone=phone,address=address,addressDetail=addressDetail,addressCode=addressCode)
		addms.save()

class Kzlogin(models.Model):
	code=models.IntegerField()

	@classmethod
	def addcode(cls,code):
		addms = cls(code=code)
		addms.save()


class Kzlogin1(models.Model):
	code = models.IntegerField()

	@classmethod
	def addcode(cls, code):
		addms = cls(code=code)
		addms.save()

class Kzonoff(models.Model):
	onoff=models.IntegerField()

class Kzidrecord(models.Model):
	idNumber = models.CharField(max_length=500)
	time=models.DateTimeField(auto_now=True)
	@classmethod
	def addcode(cls, idNumber):
		addms = cls(idNumber=idNumber)
		addms.save()


class Address1(models.Model):
	id0=models.IntegerField()
	name=models.CharField(max_length=500)
class Address2(models.Model):
	id0=models.IntegerField()
	name=models.CharField(max_length=500)

class Wrongqs(models.Model):
	studentname = models.CharField(max_length=200)
	questionid = models.IntegerField()
	@classmethod
	def addcuoti(cls,studentname,questionid):
		addcuoti = cls(studentname=studentname,questionid=questionid)
		addcuoti.save()

class Sdengji(models.Model):
	sname = models.CharField(max_length=200)
	srank = models.CharField(max_length=200)

class Sshuliang(models.Model):
	zid = models.IntegerField()
	jid = models.IntegerField()
	seta = models.IntegerField()
	setb = models.IntegerField()
	setc = models.IntegerField()

class Getflowerrecord(models.Model):
	name = models.CharField(max_length=200)
	hwname=models.CharField(max_length=500)
	flower=models.IntegerField()
	time=models.DateTimeField(auto_now=True)
	reason=models.CharField(max_length=200)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addflower(cls,name,hwname,flower,reason):

		addms = cls(name=name,hwname=hwname,flower=flower,reason=reason)
		addms.save()

class Homeworks(models.Model):
	name = models.CharField(max_length=500)
	hwname=models.CharField(max_length=500)
	time = models.IntegerField()
	ornot=models.CharField(max_length=200)
	clas=models.IntegerField()
	stuid=models.IntegerField()
	ornots=models.CharField(max_length=200)
	num = models.IntegerField(default=0)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addhw(cls,name,hwname,time,ornot,clas,stuid,ornots,num):
		addms = cls(name=name,hwname=hwname,time=time,ornot=ornot,clas=clas,stuid=stuid,ornots=ornots,num=num)
		addms.save()
class Homeworksid(models.Model):
	time = models.IntegerField()
	hwname = models.CharField(max_length=500)
	num = models.IntegerField(default=0)
	class Meta:
		ordering = ['-time']

class Badnews(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now=True)
	hwname = models.CharField(max_length=500)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,hwname):
		addms = cls(name=name,hwname=hwname)
		addms.save()
class Lucky(models.Model):
	num = models.IntegerField()
	name = models.CharField(max_length=500)
	reason = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,reason,num):
		addms = cls(name=name,reason=reason,num=num)
		addms.save()

class Uselucky(models.Model):
	name = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now_add=True)
	num = models.IntegerField()
	ornot = models.IntegerField()
	clas = models.IntegerField(default=3)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,num,ornot,clas):
		addms = cls(name=name,num=num,ornot=ornot,clas=clas)
		addms.save()
class Music(models.Model):
	name = models.CharField(max_length=500)
class Musics(models.Model):
	name = models.CharField(max_length=500)
	names = models.CharField(max_length=500)
	num = models.IntegerField(default=0)
	idd = models.IntegerField()
	cost = models.IntegerField(default=0)
class Setgoodns(models.Model):
	name = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now_add=True)
	num = models.IntegerField()
	reason = models.CharField(max_length=500)
	ornot = models.IntegerField(default=0)
	clas = models.IntegerField(default=3)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,num,reason,ornot,clas):
		addms = cls(name=name,num=num,reason=reason,ornot=ornot,clas=clas)
		addms.save()
class Luckys(models.Model):
	num = models.IntegerField()
	name = models.CharField(max_length=500)
	reason = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now=True)
	clas = models.IntegerField(default=3)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,reason,num,clas):
		addms = cls(name=name,reason=reason,num=num,clas=clas)
		addms.save()
class Classnews(models.Model):
	name = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-time']

class Hardqs(models.Model):
	id = models.AutoField(primary_key=True)
	questiontext = models.ImageField(upload_to='hardquestions')
	answerdetail = models.ImageField(upload_to='hardquestions')
	questionanswer = models.CharField(max_length=50)
	ornot = models.IntegerField(default=0)
	ornot4 = models.IntegerField(default=0)
	ornots = models.CharField(max_length=50)
	ornots4 = models.CharField(max_length=50)
	num = models.IntegerField()
	time = models.DateTimeField(auto_now=True)
	killer = models.CharField(max_length=5000)
	killer4 = models.CharField(max_length=5000)
	nums = models.IntegerField(default=0)
	jihui = models.IntegerField(default=2)
	sum = models.IntegerField(default=0)
	sum4=models.IntegerField(default=0)
	class Meta:
		ordering = ['-time']

class Hardqsrecord(models.Model):
	idd= models.IntegerField()
	num = models.IntegerField()
	name = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now=True)
	ornot=models.IntegerField(default=0)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,idd,num,name,ornot):
		addms = cls(idd=idd,num=num,name=name,ornot=ornot)
		addms.save()
class Hardqsname(models.Model):
	idd= models.IntegerField()
	num = models.IntegerField()
	name = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now=True)
	clas = models.IntegerField(default=3)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,idd,num,name,clas):
		addms = cls(idd=idd,num=num,name=name,clas=clas)
		addms.save()
# class Sendms(models.Model):
# 	send = models.CharField(max_length=500)
# 	reply= models.CharField(max_length=500)
# 	time = models.DateTimeField(auto_now=True)
# 	clas = models.IntegerField(default=3)
# 	class Meta:
# 		ordering = ['-time']
#
# 	@classmethod
# 	def addmss(cls,idd,num,name,clas):
# 		addms = cls(idd=idd,num=num,name=name,clas=clas)
# 		addms.save()
class Hardkilleronoff(models.Model):
	hard= models.IntegerField(default=1)
	middle= models.IntegerField(default=1)
	easy= models.IntegerField(default=1)

class Hardqslimit(models.Model):
	name = models.IntegerField(default=1)
	num = models.IntegerField(default=1)
	time = models.DateTimeField(auto_now=True)

class Middleqslimit(models.Model):
	name = models.IntegerField(default=1)
	num = models.IntegerField(default=1)
	time = models.DateTimeField(auto_now=True)

class Easyqslimit(models.Model):
	name = models.IntegerField(default=1)
	num = models.IntegerField(default=1)
	time = models.DateTimeField(auto_now=True)
class Easyqs(models.Model):
	id = models.AutoField(primary_key=True)
	questiontext = models.ImageField(upload_to='easyqs')
	questionanswer = models.CharField(max_length=50)
	num = models.IntegerField()
	time = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-time']
class Easyrecord(models.Model):
	idd= models.IntegerField()
	num = models.IntegerField()
	name = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now=True)
	clas = models.IntegerField(default=3)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,idd,num,name,clas):
		addms = cls(idd=idd,num=num,name=name,clas=clas)
		addms.save()

class Draws(models.Model):
	idd= models.IntegerField()
	sum = models.IntegerField()
	num =models.IntegerField()
	pl = models.FloatField()
	time = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,idd,sum,num,pl):
		addms = cls(idd=idd,sum=sum,num=num,pl=pl)
		addms.save()

class Jifeng(models.Model):
	name = models.CharField(max_length=50)
	sum = models.IntegerField(default=0)
	time = models.DateTimeField(auto_now=True)
	clas = models.IntegerField(default=0)
	class Meta:
		ordering = ['-time']
class Jifengrecord(models.Model):
	name= models.CharField(max_length=50)
	num =models.IntegerField()
	reason = models.CharField(max_length=50)
	time = models.DateTimeField(auto_now=True)
	clas =models.IntegerField(default=0)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,num,reason,clas):
		addms = cls(name=name,num=num,reason=reason,clas=clas)
		addms.save()
class Homewrecord(models.Model):
	name= models.CharField(max_length=50)
	hwname =models.CharField(max_length=50)
	qk = models.CharField(max_length=50)
	time = models.DateTimeField(auto_now=True)
	times= models.CharField(max_length=50)
	clas = models.IntegerField()
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,hwname,qk,times,clas):
		addms = cls(name=name,hwname=hwname,qk=qk,times=times,clas=clas)
		addms.save()

class Limitin(models.Model):
	id0 = models.IntegerField()
	id1 = models.IntegerField()
	id2 = models.IntegerField()

class Zslimit(models.Model):
	name = models.CharField(max_length=50)
	year= models.IntegerField()
	month = models.IntegerField()
	day =models.IntegerField()
	num = models.IntegerField()
	time = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,year,month,day,num):
		addms = cls(name=name,year=year,month=month,day=day,num=num)
		addms.save()
class Sumrecord(models.Model):
	name= models.CharField(max_length=50)
	reason = models.CharField(max_length=500)
	time = models.DateTimeField(auto_now=True)
	clas = models.IntegerField()
	num= models.IntegerField()
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,reason,clas,num):
		addms = cls(name=name,reason=reason,clas=clas,num=num)
		addms.save()
class Getlucky(models.Model):
	name = models.CharField(max_length=50)
	idd = models.IntegerField()
	time = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,idd):
		addms = cls(name=name,idd=idd)
		addms.save()
class Getluckynames(models.Model):
	name = models.CharField(max_length=50)
	idd = models.IntegerField()
	time = models.DateTimeField(auto_now=True)
	num = models.IntegerField()
	rank = models.IntegerField()
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,idd,num,rank):
		addms = cls(name=name,idd=idd,num=num,rank=rank)
		addms.save()
class Getluckyornot(models.Model):
	idd = models.IntegerField()
	ornot = models.IntegerField(default=0)
	time = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,idd,ornot):
		addms = cls(idd=idd,ornot=ornot)
		addms.save()
class Studentids(models.Model):
	name = models.CharField(max_length=50)
	idd = models.IntegerField()
	clas = models.IntegerField()
class Hweveryday(models.Model):
	hwname = models.CharField(max_length=50)
	time = models.CharField(max_length=500)
	num = models.IntegerField(default=0)
class Hweverydayrecord(models.Model):
	hwname = models.CharField(max_length=50)
	time = models.CharField(max_length=500)
	num = models.IntegerField(default=0)
	name = models.CharField(max_length=50)
	clas = models.IntegerField(default=0)
	ornot = models.CharField(max_length=50)
	times =  models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-time']
	@classmethod
	def addmss(cls,hwname,time,num,name,clas,ornot):
		addms = cls(hwname=hwname,time=time,num=num,name=name,clas=clas,ornot=ornot)
		addms.save()
class Paotui(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=500)
	studentname = models.CharField(max_length=50)
	ornot = models.CharField(max_length=50)
	ornots = models.CharField(max_length=50)
	clas = models.IntegerField(default=3)
	time = models.DateTimeField(auto_now=True)
	num = models.IntegerField()
	jihui = models.IntegerField(default=1)
	class Meta:
		ordering = ['-time']

class Mintest(models.Model):
	testtime = models.IntegerField()
	name = models.CharField(max_length=100)
	sumscore = models.IntegerField()
	time = models.DateTimeField(auto_now=True)
	idd = models.IntegerField()
	class Meta:
		ordering = ['-time']
class Mintestdata(models.Model):
	testtime = models.IntegerField()
	name = models.CharField(max_length=100)
	score = models.IntegerField()
	sumscore = models.IntegerField()
	time = models.DateTimeField(auto_now=True)
	idd = models.IntegerField()
	name1 = models.CharField(max_length=100)
	name2 = models.CharField(max_length=100)
	clas = models.IntegerField()
	class Meta:
		ordering = ['-idd','-score']

	@classmethod
	def addmss(cls,testtime,name,score,sumscore,idd,name1,name2,clas):
		addms = cls(testtime=testtime,name=name,score=score,sumscore=sumscore,idd=idd,name1=name1,name2=name2,clas=clas)
		addms.save()


class Mintestrecord(models.Model):
	stuname = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now=True)
	idd = models.IntegerField()
	clas = models.IntegerField()
	sumscore = models.IntegerField()
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,stuname,name,idd,clas,sumscore):
		addms = cls(stuname=stuname,name=name,idd=idd,clas=clas,sumscore=sumscore)
		addms.save()

class Wks(models.Model):
	name = models.CharField(max_length=500)
	zid = models.IntegerField()
	time = models.DateTimeField(auto_now=True)
	link = models.CharField(max_length=1000)
	class Meta:
		ordering = ['time']

	@classmethod
	def addmss(cls,name,zid,link):
		addms = cls(name=name,zid=zid,link=link)
		addms.save()
class Wksrecord(models.Model):
	name = models.CharField(max_length=500)
	learn = models.CharField(max_length=500)
	num = models.IntegerField()
	time = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ['-time']

	@classmethod
	def addmss(cls,name,learn,num):
		addms = cls(name=name,learn=learn,num=num)
		addms.save()