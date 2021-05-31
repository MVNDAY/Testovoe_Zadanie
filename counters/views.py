from django.shortcuts import render
from .models import Counter
from .forms import CounterForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
	current_user = request.user
	counter_id = current_user.id
	context = {'counter_id' : counter_id}
	return render(request, 'index.html', context)

@login_required
def getcounter(request,counter_id):
	try:
		current_user = request.user
		counter_id = current_user.id
		counter = Counter.objects.get(id=counter_id)
		counter_value = counter.counter_value
		context = {'counter_value' : counter_value, 'counter_id' : counter_id}
		return render(request,'getcounter.html', context )
	except ObjectDoesNotExist:
		if request.method != 'POST':
			form = CounterForm()
			if form.is_valid():
				form.save()
		else:
			form = CounterForm(data=request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('counters:changecounter', args=[counter_id]))
		context = {'form': form, 'counter_id' : counter_id}
		return render(request, 'changecounter.html', context)
		

@login_required
def changecounter(request,counter_id):
	current_user = request.user
	counter_id = current_user.id
	try:
		counter = Counter.objects.get(id=counter_id)
		if request.method != 'POST':
			form = CounterForm(instance=counter)
			if form.is_valid():
				form.save()
		else:
			form = CounterForm(instance=counter,data=request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('counters:changecounter', args=[counter_id]))
		context = {'form': form, 'counter_id' : counter_id}
		return render(request, 'changecounter.html', context)
	except ObjectDoesNotExist:
		if request.method != 'POST':
			form = CounterForm()
			if form.is_valid():
				form.save()
		else:
			form = CounterForm(data=request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('counters:changecounter', args=[counter_id]))
		context = {'form': form, 'counter_id' : counter_id}
		return render(request, 'changecounter.html', context)



