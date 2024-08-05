from django.db import models

class StuModel(models.Model):
	Rno = models.IntegerField()
	Name = models.CharField(max_length=50)
	Email_Id = models.EmailField(max_length = 200)
	Phone = models.IntegerField(primary_key = True)
	Department = models.CharField(max_length=50)
	Semester = models.CharField(max_length=50)
	Division = models.CharField(max_length=50)

	def __str__(self):
		return self.Name

class EmailModel(models.Model):
	email=models.EmailField(max_length=50)

class GmailModel(models.Model):
	rno = models.IntegerField(primary_key =True)
	name = models.CharField(max_length=50)
	gmail = models.EmailField(max_length=50)

class MaModel(models.Model):
	role=(('present',"Present"),
		('absent',"Absent"))
	ro = models.CharField(max_length=10,choices=role, default="present	")
	def __str__(self):
		return self.ro



class MailModel(models.Model):
	rno = models.IntegerField()
	name = models.CharField(max_length=50)
	gmail = models.EmailField(max_length=50)
	
