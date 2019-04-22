from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

)
from .models import Item,User
from django.urls import reverse
#import feedparser
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponse
from .forms import UserLoginForm, UserRegisterForm, Contactform
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
		title = "Login"
		form= UserLoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username,password=password)
			login(request,user)
			print(request.user.is_authenticated)
			return redirect('/user_stockoverflow/')
			#redirect
		return render(request, "form.html",{"form":form, "title": title})

def register_view(request):
		title = "Sign Up"
		form = UserRegisterForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			new_user = authenticate(username=user.username,password = password)
			login(request,user)
			print(request.user.is_authenticated)
			return redirect('/user_stockoverflow/')


		context = {
			"form": form,
			"title": title
		}
		return render(request, "form.html",context)  

def logout_view(request):
	if request.method == "POST":
		logout(request)
		return redirect('/login/')
def login_redirect(request):
	return redirect('login/')
def reg_redirect(request):
	return HttpResponseRedirect('/login/')
@login_required
def user_view(request):
		

		return render(request, "user.html")	
def contact_view(request):
		form = Contactform(request.POST or None)
		if form.is_valid():
			form.save()
		return render(request,"contact.html")

def news_view(request):
		return render(request, "news.html" )

def addtoitem(request):
	if request.method == 'POST':
		itm = Item(userid=request.user.id,name=request.POST['item_name'],price=request.POST['option'],qty=request.POST['qty'])
		itm.save()
		return HttpResponseRedirect('/user_stockoverflow/')
@login_required
def user_home(request):
	return render(request,"user.html")


def user_stock(request):
	dict = {'Reliance':'reliance.png','Tatamotors':'tata.png','Sensex':'sensex.png'}	
	itm = Item.objects.filter(userid=request.user.id)
	no = itm.count()
	sum = 0
	for k in itm:
		sum += k.price * k.qty
	return render(request,'userstock.html',{'i':itm,'d':dict, 'no':no ,'sum':sum})

#def removefromitem(request):
#	if request.method=='POST':
#	itm = Item.objects.filter(name= request.POST['name'],qty=request.POST['qty']).delete()
#	return HttpResponseRedirect('/userstocks/')
