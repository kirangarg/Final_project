# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from demoupload.forms import SignUpForm , LoginForm
from django.contrib.auth.hashers import make_password,check_password
from demoupload.models import UserModel

# Create your views here.
def signup_view(request):
     if request.method == "POST":
         form = SignUpForm(request.POST)
         if form.is_valid():
             username = form.cleaned_data['username']
             name = form.cleaned_data['name']
             email = form.cleaned_data['email']
             password = form.cleaned_data['password']
             # save data to database
             user = UserModel(name=name, password=make_password(password), email=email, username=username)
             user.save()
             template_name = 'success.html'

     elif request.method == "GET":
         form = SignUpForm()
         template_name = 'signup.html'

     return render(request, template_name, {'form':form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = UserModel.objects.filter(username=username).first()
            if user:
                #compare password
                if check_password(password, user.password):
                    template_name = 'login_success.html'
                else:
                    template_name = 'login_fail.html'
            else:
                template_name = 'login_fail.htrml'

    elif request.method == "GET":
        #form = LoginForm()
        template_name = 'login.html'
        form = LoginForm()
    else:
        template_name = 'login_fail.html'
    return render(request, template_name, {'form': form})



