from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from fox.forms import RegistrationForm, LoginForm
from fox.models import Fox
from django.contrib.auth import authenticate, login, logout
import os

def FoxRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['username'],\
                                            email = form.cleaned_data['email'],\
                                            password = form.cleaned_data['password'])
            user.save()
            fox = Fox(user=user, ip=form.cleaned_data['ip'])
            fox.save()
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
    else:
        # Blank registration form
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))

@login_required
def Profile(request):
    fox = request.user.get_profile
    context = {'fox': fox}
    
    #command = "ssh pi@" +   + " sudo python /home/pi/.foxlatch/foxlatch.py lock > /users/u21/technicalfox/Projects/FoxLatch/site/static/stat.txt"
    #os.system(command)

    return render_to_response('profile.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            fox = authenticate(username=username, password=password)
            if fox is not None:
                login(request, fox)
                return HttpResponseRedirect('/profile/')
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        # show login form
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def ToggleLock(request):
    fox = request.user.get_profile
    context = {'fox': fox}

    command = "ssh pi@" + fox.ip + " sudo python /home/pi/.foxlatch/foxlatch.py lock > /users/u21/technicalfox/Projects/FoxLatch/site/static/response.txt"
    os.system(command)

    return render_to_response('profile.html', context, context_instance=RequestContext(request))

def index_view(request):
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def about_view(request):
    return render_to_response("about.html", locals(), context_instance=RequestContext(request))
