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
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': this_user,
    }
    return render(request, 'game_page.html', context)


def user_choice(request):
    list = ["Metal", "Earth", "Water", "Fire", "Wood"]
    this_user = User.objects.get(id=request.session['user_id'])
    user_gold = this_user.gold
    computer = list[randint(0, 4)]
    bet_amount = request.POST['bet_amount']
    user_choice = request.POST['choice']
    messages.success(request, 'You picked ' + user_choice)
    messages.success(request, 'Computer picked ' + computer)
    if user_choice == computer:
        messages.success(request, 'It is a tie!')
        return redirect('game_page')
    if user_choice == "Metal":
        if computer == "Wood":
            this_user.gold = user_gold + int(bet_amount)
            this_user.save()
            messages.success(
                request, 'Metal Beats Wood, you win ' + bet_amount + ' gold :)')
            return redirect('game_page')
        if computer == "Fire":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Fire Beats Metal, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        if computer == "Water":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Metal lose to Water, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    if user_choice == "Earth":
        if computer == "Water":
            this_user.gold = user_gold + int(bet_amount)
            this_user.save()
            messages.success(
                request, 'Earth Beats Water, you win ' + bet_amount + ' gold :)')
            return redirect('game_page')
        if computer == "Wood":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Wood Beats Earth, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        if computer == "Metal":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Earth lose to Metal, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    if user_choice == "Water":
        if computer == "Fire":
            this_user.gold = user_gold + int(bet_amount)
            this_user.save()
            messages.success(
                request, 'Water Beats Fire, you win ' + bet_amount + ' gold :)')
            return redirect('game_page')
        if computer == "Earth":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Earth Beats Water, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        if computer == "Wood":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Water lose to Wood, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    if user_choice == "Fire":
        if computer == "Metal":
            this_user.gold = user_gold + int(bet_amount)
            this_user.save()
            messages.success(
                request, 'Fire Beats Metal, you win ' + bet_amount + ' gold :)')
            return redirect('game_page')
        if computer == "Water":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Water Beats Fire, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        if computer == "Earth":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Fire lose to Earth, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    if user_choice == "Wood":
        if computer == "Earth":
            this_user.gold = user_gold + int(bet_amount)
            this_user.save()
            messages.success(
                request, 'Wood Beats Earth, you win ' + bet_amount + ' gold :)')
            return redirect('game_page')
        if computer == "Metal":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Metal Beats Wood, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        if computer == "Fire":
            this_user.gold = user_gold - int(bet_amount)
            this_user.save()
            messages.error(
                request, 'Wood lose to Fire, you lose ' + bet_amount + ' gold :(')
            return redirect('game_page')
        else:
            messages.success(request, 'No winner this round!!')
            return redirect('game_page')
    return redirect('game_page')
