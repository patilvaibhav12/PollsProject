from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from accounts.models import Userdata
from mainapp.models import polls

def infor(request):
    user = User.objects.get(username = request.user.username)
    usr = Userdata.objects.get(username = user)
    context = {
    'userdata': usr
    }
    return(context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('/accounts/login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        phone = request.POST['phone']
        fullname = first_name + " " + last_name
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/accounts/register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                
                userdata = Userdata(username = username, fullname = fullname, email = email, phoneno = phone)
                userdata.save()
                print('user created')
                return redirect('/accounts/login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('/accounts/register')
        return redirect('/')
        
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/') 

# def dataupdate(request):
    
#     if request.method == 'POST':
#         user = User.objects.get(username = request.user.username)
#         usr = Userdata.objects.get(username = user)
#         usr.username = request.POST.get('username')
#         usr.fullname = request.POST.get('fullname')
#         usr.accountno = request.POST.get('accountno')
#         usr.ifsc = request.POST.get('ifsc')
#         usr.save()
#         messages.success(request, 'data updated successfully')
#     return render(request,'dataupdate.html')      

def profile(request):
    user = User.objects.get(username = request.user.username)
    usr = Userdata.objects.get(username = user)
    poll_data = polls.objects.filter(user_name = usr)
    context = {'userdata':usr, 'poll_data':poll_data}
    return render(request, 'profile.html', context)

def deletep(request, poll_id):
    poll = polls.objects.get(pk = poll_id)
    poll.delete()
    messages.info(request,'Poll deleted successfully')
    return redirect('/accounts/profile')