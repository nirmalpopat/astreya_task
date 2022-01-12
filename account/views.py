from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from random import choice
from .models import Profile
from django.db.models import F

CHOICE = ['r', 'p', 's']
COUNT = 0

@login_required(login_url='login/')
def rps(request):
    return render(request, 'account/rps.html')


def won():
    Profile.objects.update(wins=F('wins') + 1)


def lost():
    Profile.objects.update(loses=F('loses') + 1)


def tied():
    Profile.objects.update(ties=F('ties') + 1)

@login_required(login_url='login/')
def rps_play(request):
    global COUNT
    COUNT += 1
    if request.method == 'POST':

        pc_choice = choice(CHOICE)

        if request.POST['option'] == 'r':
            if pc_choice == 'p':
                lost()
                request.session['response'] = "You lose. Computer chose paper."
            elif pc_choice == 's':
                won()
                request.session['response'] = "You win! Computer chose scissors."
            elif pc_choice == 'r':
                tied()
                request.session['response'] = "It's a tie! Computer chose rock as well."

        elif request.POST['option'] == 'p':
            if pc_choice == 'r':
                won()
                request.session['response'] = "You win! Computer chose rock. "
            elif pc_choice == 's':
                lost()
                request.session['response'] = "You lose. Computer chose scissors."
            elif pc_choice == 'p':
                tied()
                request.session['response'] = "It's a tie! Computer chose paper as well."

        elif request.POST['option'] == 's':
            if pc_choice == 'p':
                won()
                request.session['response'] = "You win! Computer chose paper."
            elif pc_choice == 'r':
                lost()
                request.session['response'] = "You lose. Computer chose rock."
            elif pc_choice == 's':
                tied()
                request.session['response'] = "It's a tie! Computer chose scissors as well."
        

        elif request.POST['option'] != CHOICE:
            request.session['response'] = "Please select one of the following choices: \'r\' \'p\' \'s\'"
        print(str(request.user),'=================================',type(request.user), str(request.user))
        if COUNT % 3 == 0 and str(request.user) != 'AnonymousUser':
            request.session['response'] = ''
            
            obj = Profile.objects.get(user=request.user)
            if obj.wins == obj.loses:
                request.session['result'] = 'Result of 3 Round is Tiee !!!'
            elif obj.wins > obj.loses:
                request.session['result'] = 'Result of 3 Round is, You are Winner!!!'
            elif obj.wins < obj.loses:
                request.session['result'] = 'Result of 3 Round is, You are Loser!!!'
            obj.wins = 0
            obj.loses = 0
            obj.ties = 0
            obj.save()
        else:
            request.session['result'] = ''

        return redirect('/')
    else:

        return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            Profile(user = request.user).save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'account/reg_form.html', {'form': form})

def index(request):
    print('=============index===================')
    return render(request, 'personal/home.html')
