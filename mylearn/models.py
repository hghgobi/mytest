from django.db import models

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
	homeworktime =models.CharField(max_length=200)
	homeworkstudent = models.ForeignKey(Students,on_delete=models.DO_NOTHING)
	class Meta:
		ordering = ['-homeworktime']

class Exams(models.Model):
	examname = models.CharField(max_length=200)
	examscore = models.IntegerField()
	examtime = models.CharField(max_length=200)
	examstudent = models.ForeignKey(Students,on_delete=models.DO_NOTHING)
	class Meta:
		ordering = ['-examtime']




class Classnotes(models.Model):
	notename = models.CharField(max_length=200)
	notecontent = models.TextField()
	notetime = models.DateTimeField(auto_now_add=True)
	noteupdatetime = models.DateTimeField(auto_now=True)
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
     
        
        	
        	
        	

            	
            	

            	
		
		
		


