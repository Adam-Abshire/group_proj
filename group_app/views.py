from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

############# LANDING PAGES #############################
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'registration.html')

def main(request):
    this_user = User.objects.get(id = request.session['user_id'])
    context = {
        'user' : this_user,
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
    pw_hash = bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        user_name = request.POST['user_name'],
        email = request.POST['email'],
        password = pw_hash,
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
    user = User.objects.get(email = request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/main')

def logout(request):
    request.session.flush()
    return redirect('/')
############# REGISTER & LOGIN ##########################