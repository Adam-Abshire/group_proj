from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, GameInfo
from random import randint

############# LANDING PAGES #############################


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'registration.html')


def main(request):
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': this_user,
    }
    return render(request, 'main.html', context)
############# LANDING PAGES #############################
############# REGISTER & LOGIN ##########################


def register_user(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/register')
    pw_hash = bcrypt.hashpw(
        request.POST['pword'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        user_name=request.POST['user_name'],
        email=request.POST['email'],
        password=pw_hash,
    )
    request.session['user_id'] = new_user.id
    return redirect('/main')


def login_user(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.loginval(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/main')


def logout(request):
    request.session.flush()
    return redirect('/')
############# REGISTER & LOGIN ##########################


def game_page(request):
    return render(request, 'game_page.html')


def user_choice(request):
    list = ["Metal", "Earth", "Water", "Fire", "Wood"]
    computer = list[randint(0, 4)]

    user_choice = request.POST['choice']
    messages.success(request, 'You picked ' + user_choice)
    messages.success(request, 'Computer picked ' + computer)
    if user_choice == computer:
        messages.success(request, 'It is a tie!')
        return redirect('game_page')
    if user_choice == "Metal":
        if computer == "Wood":
            messages.success(request, 'Metal Beats Wood, you win :)')
            return redirect('game_page')
        if computer == "Fire":
            messages.success(request, 'Fire Beats Metal, you lose :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    if user_choice == "Earth":
        if computer == "Water":
            messages.success(request, 'Earth Beats Water, you win :)')
            return redirect('game_page')
        if computer == "Wood":
            messages.success(request, 'Wood Beats Earth, you lose :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    if user_choice == "Water":
        if computer == "Fire":
            messages.success(request, 'Water Beats Fire, you win :)')
            return redirect('game_page')
        if computer == "Earth":
            messages.success(request, 'Earth Beats Water, you lose :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    if user_choice == "Fire":
        if computer == "Metal":
            messages.success(request, 'Fire Beats Metal, you win :)')
            return redirect('game_page')
        if computer == "Water":
            messages.success(request, 'Water Beats Fire, you lose :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    if user_choice == "Wood":
        if computer == "Earth":
            messages.success(request, 'Wood Beats Earth, you win :)')
            return redirect('game_page')
        if computer == "Metal":
            messages.success(request, 'Metal Beats Wood, you lose :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    return redirect('game_page')
