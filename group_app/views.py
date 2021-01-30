from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

############# LANDING PAGES #############################
def login(request):
    return render(request, 'login.html')
############# LANDING PAGES #############################
############# REGISTER & LOGIN ##########################
def register_user(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')
    pw_hash = bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        user_name = request.POST['first_name'],
        email = request.POST['email'],
        password = pw_hash,
    )
    request.session['user_id'] = new_user.id
    return redirect('/menu')

def login_user(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.loginval(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/login')
    user = User.objects.get(email = request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/menu')

def logout(request):
    request.session.flush()
    return redirect('/')
############# REGISTER & LOGIN ##########################