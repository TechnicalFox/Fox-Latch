from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from fox.forms import RegistrationForm
from fox.models import Fox

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            pass
        else:
            pass
            # Return a 'disabled account' error message
    else:
        pass
        # Return an 'invalid login' error message.

def logout_view(request):
    logout(request)
    pass
    # Redirect to a success page.

def loginForm_view(request):
    return render_to_response("login.html", locals(), context_instance=RequestContext(request))

def FoxRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = user.objects.create_user(username = form.cleaned_data['username'],\
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

def index_view(request):
    return render_to_response("index.html", locals(), context_instance=RequestContext(request))

def about_view(request):
    return render_to_response("about.html", locals(), context_instance=RequestContext(request))
