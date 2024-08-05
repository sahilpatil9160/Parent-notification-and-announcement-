from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from parent_notification_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange
from .models import StuModel,EmailModel,GmailModel,MaModel,MailModel
from .forms import StuForm,MaForm
import requests
import bs4

def main(request):
	return render(request,"main.html")

def user_login(request):
	if request.method == "POST":
		fid = request.POST.get("fid")
		pw = request.POST.get("pw")
		usr = authenticate(username=fid, password=pw)
		if usr is None:
			return render(request,"user_login.html",{"msg":"login denied"})
		else:
			login(request,usr)
			return redirect("home")	
	else:
		return render(request,"user_login.html")

def user_signup(request):
	if request.method == "POST":
		fr = request.POST.get("fr")
		ls = request.POST.get("ls")
		fid = request.POST.get("fid")
		phone = request.POST.get("phone")
		em = request.POST.get("em")
		try:
			usr = User.objects.get(username=fid)
			return render(request, "user_signup.html", {"msg":"Faculty id is already registered"})
		except User.DoesNotExist:
			try:
				usr = User.objects.get(email=em)
				return render(request,"user_signup.html",{"msg":"Email id is already registered"})
			except User.DoesNotExist:
				pw = ""
				text = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
				for i in range(5):
					pw = pw + text[randrange(len(text))]
				print(pw)
				msg = "ur password is "+pw
				send_mail("Welcome to Parent Notification And Announcement", msg, EMAIL_HOST_USER, [str(em)])
				usr = User.objects.create_user(username=fid, password=pw,email=em)
				usr.save()
				return redirect("user_login")
	else:
		return render(request,"user_signup.html")

def user_logout(request):
	logout(request)
	return redirect("user_login")

def reset(request):
	return render(request,"reset.html")

def home(request):
	if request.user.is_authenticated:
		try:
			wa = "https://www.brainyquote.com/quote_of_the_day"
			res = requests.get(wa)
			print(res)
			data = bs4.BeautifulSoup(res.text,'html.parser')
			info = data.find('img', {'class':'p-qotd'})
			msg = info['alt']
			return render(request,"home.html",{'msg':msg})
		except Exception as e:
			msg = "Somthing went wrong"
			return render(request,"home.html",{'msg':msg})
		
	else:
		return redirect("user_login")

def about(request):
	return render(request,"about.html")

def filter(request):
	if request.method == "POST":
		dept = request.POST.get("dept")
		sem = request.POST.get("sem")
		div = request.POST.get("div")
		date = request.POST.get("div")
		data=StuModel.objects.filter(Department=dept,Semester=sem,Division=div).order_by('Rno')
		for d in data:
			e=MailModel()
			e.rno=d.Rno
			e.name=d.Name
			e.gmail=d.Email_Id
			e.save()
		return render(request,"mark_student.html",{'data':data,'dept':dept,'sem':sem,'div':div})
	else:
		return render(request, "filter.html")

def add_student(request):
	if request.method == "POST":
		f = StuForm(request.POST)
		if f.is_valid() :
			f.save()
			fm = StuForm()
			return render(request, "add_student.html", {'fm':fm, 'msg':'Student Added'})
		else:
			return render(request, "add_student.html", {'fm':f, 'msg':'Somthing went wrong'})
	else:
		fm = StuForm()
		return render(request, "add_student.html", {'fm':fm})

def mark_student(request):
		
	
	data = StuModel.objects.all()
	print(data)
	return render(request, "mark_student.html", {'data':data, 'raj':'something went wrong'})


def delete(reuqest,id):
	ds = StuModel.objects.get(Phone=id)
	ds.delete()
	
	return redirect('del_filter')



def stu_delete(request):
	data = StuModel.objects.all()
	print(data)
	return render(request, "stu_delete.html", {'data':data, 'raj':'something went wrong'})



def del_filter(request):
	if request.method == "POST":
		dept = request.POST.get("dept")
		sem = request.POST.get("sem")
		div = request.POST.get("div")
		date = request.POST.get("div")
		data=StuModel.objects.filter(Department=dept,Semester=sem,Division=div).order_by('Rno')
		return render(request,"stu_delete.html",{'data':data,'dept':dept,'sem':sem,'div':div})
	else:
		return render(request, "del_filter.html")



def submit(request):
	return redirect('filter')

def an_filter(request):
	if request.method == "POST":
		dept = request.POST.get("dept")
		sem = request.POST.get("sem")
		div = request.POST.get("div")
		date = request.POST.get("div")
		data=StuModel.objects.filter(Department=dept,Semester=sem,Division=div).order_by('Rno')
		for d in data:
			e=EmailModel()
			e.email=d.Email_Id
			e.save()
		return render(request,"send_ann.html",{'data':data,'dept':dept,'sem':sem,'div':div})
	else:
		return render(request, "an_filter.html")

def send_ann(request):
	msg=request.POST.get("msg")
	data = StuModel.objects.all()
	print(data)
	list_email=[]
	for i in data:
		list_email.append(i.email)
	print("********************************************",list_email)
	if list_email:
		send_mail("Welcome to Parent Notification And Announcement", msg, EMAIL_HOST_USER, list_email)
		return render(request,"home.html",{'msg':"lol"})
	else:
		return render(request, "send_ann.html", {'data':data, 'raj':'something went wrong'})

def send_email(request):
	if request.method == "POST":
		msg= request.POST.get("msg")
		print("************************************printing msg ::::::",msg)
		data = EmailModel.objects.all()
		print(data)
		list_email = []
		for i in data:
			list_email.append(i.email)
		print("********************************************",list_email)
		send_mail("Announcement", msg, EMAIL_HOST_USER, list_email)
		em = EmailModel.objects.all()
		em.delete()
		return render(request,"home.html")
	else:
		return render(request,"send_email.html")


def how(request):
	return render(request, 'how.html')

def at_mail(request):
	data = MailModel.objects.all()
	if request.method == "POST":
		msg = request.POST.get('raj')
		print(msg)
		print(data)
		li = ['r1','r2','r3']
		list = []
		i=0
		for d in data:
			i=i+1
			p = request.POST.get(str(i))
			print('i',i)
			print(d.id)
			print(d)
			print(p)
			print(d.rno)
			if p == 'absent':
				list.append(d.gmail)
			print(list)
		send_mail("Announcement", msg, EMAIL_HOST_USER, list)
		em = MailModel.objects.all()
		em.delete()
		return redirect("home")
	else:
		return render(request, "at_mail.html",{'data':data})