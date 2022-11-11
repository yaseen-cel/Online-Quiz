from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from candidateApp.models import Candidate
# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        username=request.POST['email']
        email=request.POST['email']
        mobile =request.POST['mobile']
        password=request.POST['password']
        password1=request.POST['password1']

        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already exist')
                return redirect('register')

            # elif User.objects.filter(email = email).exists():
            #     messages.info(request,'email already exist')
            #     return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name)
                user.save();
                user_details = User.objects.get(username = username) 
                user1 = Candidate(email=email,name=first_name,mobile = mobile,user_id = user_details.id)
                user1.save()
                print("user created")
                return redirect('register')
        else:
            messages.info(request,'Password didnt match')
            return redirect('register')
    else:    
        return render(request,"accounts/register.html")
