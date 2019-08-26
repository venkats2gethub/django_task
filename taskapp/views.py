from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.models import User, auth 

# Create your views here.

def form1(request):

	if request.method == 'POST':

		text1 = request.POST['text1']
		text2 = request.POST['text2']
		text3 = request.POST['text3']
		text4 = request.POST['text4']
		text5 = request.POST['text5']
		text6 = request.POST['text6']
		num1 = request.POST['num1']
		text7 = request.POST['text7']
		date1 = request.POST['date1']
		num2 = request.POST['num2']

		destination = Destination(text1=text1, text2=text2, text3=text3, text4=text4, text5=text5, text6=text6, num1=num1, text7=text7, date1=date1, num2=num2)
		destination.save();
		print('Data added successfully')
		
		return redirect('/')
	

	else:
		return render(request, 'form1.html')


def details(request):
    istekler = Destination.objects.all()
    return render(request, 'details.html', locals())