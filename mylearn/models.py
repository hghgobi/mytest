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

	class Meta:
		ordering = ['-time']

	@classmethod
	def addyxname(cls,bj,zid,jid,name,ornot,fs,costtime):

		addms = cls(bj=bj,zid=zid,jid=jid,name=name,ornot=ornot,fs=fs,costtime=costtime)
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
	answer = models.IntegerField(default=0)
	ornot = models.IntegerField(default=0)

	@classmethod
	def addqs(cls,num0,num1,yunsuan,answer,ornot):

		addqs = cls(num0=num0,num1=num1,yunsuan=yunsuan,answer=answer,ornot=ornot)
		addqs.save()
class Xxqs22(models.Model):
	num0 = models.IntegerField()
	num1 = models.IntegerField()
	yunsuan = models.IntegerField()
	answer = models.IntegerField(default=0)
	ornot = models.IntegerField(default=0)

	@classmethod
	def addqs2(cls,num0,num1,yunsuan,answer,ornot):

		addqs2 = cls(num0=num0,num1=num1,yunsuan=yunsuan,answer=answer,ornot=ornot)
		addqs2.save()
class Xxqs23(models.Model):
	num0 = models.IntegerField()
	num1 = models.IntegerField()
	yunsuan = models.IntegerField()
	answer = models.IntegerField(default=0)
	ornot = models.IntegerField(default=0)

	@classmethod
	def addqs3(cls,num0,num1,yunsuan,answer,ornot):

		addqs3 = cls(num0=num0,num1=num1,yunsuan=yunsuan,answer=answer,ornot=ornot)
		addqs3.save()

class Xxqs24(models.Model):
	num0 = models.IntegerField()
	num1 = models.IntegerField()
	yunsuan = models.IntegerField()
	answer = models.IntegerField(default=0)
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

	class Meta:
		ordering = ['costtime']

	@classmethod
	def addrankxhl(cls,name,costtime):

		addms = cls(name=name,costtime=costtime)
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

class Cuoti(models.Model):
	studentname = models.CharField(max_length=200)
	questionid = models.IntegerField()
	@classmethod
	def addcuoti(cls,studentname,questionid):
		addcuoti = cls(studentname=studentname,questionid=questionid)
		addcuoti.save()

