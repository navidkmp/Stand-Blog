from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from account.forms import LoginForm, UserEditForm

def user_login(request):
    if request.user.is_authenticated == True:
        return redirect("/")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {"form":form})

def user_register(request):
    context = {"errors":[]}
    if request.user.is_authenticated == True:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['errors'].append("Passwords don't match")
            return render(request, "account/register.html", context)

        user = User.objects.create(username=username, email=email, password=password1)
        login(request, user)
        return redirect("/")
    return render(request, "account/register.html", {})

def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == "POST":
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, "account/edit.html", {"form":form})

def user_logout(request):
    logout(request)
    return redirect('/')