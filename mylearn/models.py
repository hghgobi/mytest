from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

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
	class Meta:
		ordering = ['-examtime']




class Classnotes(models.Model):
	notename = models.CharField(max_length=200)
	notecontent = RichTextUploadingField()
	notetime = models.DateTimeField(auto_now_add=True)
	noteupdatetime = models.DateTimeField(auto_now=True)
	readed_num =models.IntegerField(default=0)
	def __str__(self):
		return self.notename
	class Meta:
		ordering = ['-id']
#在线测试
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

	







        	
        	

            	
            	

            	
		
		
		


