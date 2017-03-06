from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime


email_valid = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
name_valid = r'^[ a-zA-Z]{3,}$'
pass_valid = r'^[a-zA-Z0-9.+_-]{8,}$'
entry_valid = r'^[ a-zA-Z0-9.+_-]{1,}$'


class UserManager(models.Manager):

    def login(self, logData):
        no_errors = True
        login_errors =[]
        # result = no_errors, login_errors
        try:
            username = User.objects.get(email=logData["username_login"].lower())
            if bcrypt.hashpw(logData["password_login"].encode(), username.password.encode()) == username.password:
                result = no_errors, login_errors, username.id
            else:
                no_errors = False
                login_errors.append("Password does not Match")
                result = no_errors, login_errors


        except:
            no_errors = False
            login_errors.append("Email does not exist")
            result = no_errors, login_errors

        return result


    def register(self, postData):
        no_errors = True
        error_messages =[]
        if re.match(email_valid, postData["email"]):
            print "valid email"
            try:
                User.objects.get(email=postData["email"])
                no_errors = False
                error_messages.append("Email address already in use")
            except:
                print "New user"
        else:
            no_errors = False
            error_messages.append("Invalid Email Address")



        if re.match(name_valid, postData["name"]):
            print "valid Name"
            try:
                User.objects.get(name=postData["name"])
                no_errors = False
                error_messages.append("Name already in use")
            except:
                print "New Name"
        else:
            no_errors = False
            error_messages.append("Invalid Name, please enter 3 or more Letters")



        if re.match(name_valid, postData["username"]):
            print "valid Username"
            try:
                User.objects.get(username=postData["username"])
                no_errors = False
                error_messages.append("Username already in use")
            except:
                print "New Username"
        else:
            no_errors = False
            error_messages.append("Invalid Username, please enter 3 or more Letters")


        if re.match(pass_valid, postData["password"]):
            print "valid Password"
        else:
            no_errors = False
            error_messages.append("Invalid Password, please enter 8 or more characters")
        if postData["password"]== postData["confirm"]:
            print "Password Confirmed"
        else:
            no_errors = False
            error_messages.append("Password confirmation did no match")

        if datetime.datetime.strptime(postData["dob"],'%Y-%m-%d').date()<datetime.date.today():
            print "valid date of birth"
        else:
            no_errors=False
            error_messages.append("Invalid date of birth, please enter a date prior to todays date")



        if no_errors:
            hashed = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())
            User.objects.create(name=postData["name"].lower(), username=postData["username"].lower(), email=postData["email"].lower(), password=hashed)

        return no_errors, error_messages

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    user_id = models.ManyToManyField("self", related_name="friender")
    friend_id = models.ManyToManyField("self", related_name="friendee")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return "email: {}".format(self.email)
