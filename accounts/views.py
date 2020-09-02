from django.shortcuts import render , redirect
from .form import signupform
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Create your views here.

def signup(request):

    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            login(request,user)
            return redirect('/accounts/profile')


    else:
        form = signupform()

    return render(request , 'registration/signup.html',{'form':form})