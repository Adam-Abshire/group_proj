from django.db import models
import re
from django.contrib import messages
import bcrypt

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        all_users_names = []
        all_users = User.objects.all()
        for user in all_users:
            all_users_names.append(user.user_name)
        if postData['user_name'] in all_users_names:
            errors['user_name'] = "User Name Has Been Taken"
        if len(postData['user_name']) < 2:
            errors['user_name'] = "First Name must contain 2 characters"
        if len(postData['pword']) < 8:
            errors['pword'] = "Password must contain 8 characters"
        if postData['pword'] != postData['pword_confirm']:
            errors['pword_confirm'] = "Passwords do not match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = ("Invalid email address!")
        return errors

    def editval(self, postData):
        errors = {}
        if len(postData['user_name']) < 2:
            errors['user_name'] = "First Name must contain 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = ("Invalid email address!")
        return errors
    
    def loginval(self, postData):
        errors = {}
        all_users = User.objects.all()
        all_emails = []
        for user in all_users:
            all_emails.append(user.email)
        if postData['email'] not in all_emails:
            errors['email'] = "Email is not recognized, please register"
        if postData['email'] in all_emails:
            user = User.objects.filter(email= postData['email'])
            if bcrypt.checkpw(postData['pword'].encode(), user[0].password.encode()) == False:
                errors['pword'] = "Password is not correct"
        return errors

class User(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()