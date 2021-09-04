from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from accounts.models import Userdata
from django.contrib.auth.models import User
from .models import polls
def infor(request):
    user = User.objects.get(username = request.user.username)
    usr = Userdata.objects.get(username = user)
    return(usr)

def index(request):
    if request.user.is_anonymous:
        return redirect('accounts/login')
    userdata = infor(request)
    poll_data = polls.objects.all()
    context = {'userdata':userdata, 'poll_data':poll_data}
    return render(request,'index.html',context)
def create(request):
    userdata = infor(request)
    poll_data = polls.objects.filter(user_name = userdata)
    if request.method == 'POST':
        question = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        user_name = userdata
        Pol = polls(question = question, option_one=option1, option_two=option2, option_three=option3, option_four=option4, user_name = user_name)
        Pol.save()
        return redirect('index')
    if len(poll_data) < 5:
        return render(request,'create.html')
    else:
        return render(request, 'warning.html')
    
def vote(request):
    poll_id = request.GET.get('id')
    poll = polls.objects.get(pk=poll_id)
    userdata = infor(request)
    userdata = str(userdata)
    if (userdata in poll.uservote):
        return render(request, 'votewarning.html')
    else:
        if request.method == 'POST':

            selected_option = request.POST['poll']
            if selected_option == 'option1':
                poll.option_one_count +=1
                poll.uservote.append(userdata)
                poll.save()
            elif selected_option == 'option2':
                poll.option_two_count +=1
                poll.uservote.append(userdata)
                poll.save()
            elif selected_option == 'option3':
                poll.option_three_count +=1
                poll.uservote.append(userdata)
                poll.save()
            elif selected_option == 'option4':
                poll.option_four_count +=1
                poll.uservote.append(userdata)
                poll.save()
            else:
                return HttpResponse(400, 'Invalid form')

            return redirect('results', poll_id)

        context = {
            'poll' : poll
        }
        return render(request, 'vote.html', context)

def results(request, poll_id):
    #poll_id = request.GET.get('id')
    if poll_id == '':
        poll_id = 7
    poll = polls.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'results.html', context)

