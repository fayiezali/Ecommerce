from django.db import models

from django.contrib.auth.models import User # إستيراد اسم المستخدم

class UsersTable(models.Model):
    first_name = models.CharField(max_length=20)
        # for CharField its mandatory to pass max_length parameter & initialize it.
        # By default field is not null to make it nullable add parameter, null = true
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=300)
    is_verified = models.BooleanField(default=False, null=True)
    token = models.CharField(max_length=300,default=None, null=True)
    
    # Note : All these validation as per parameter passed will work if data inserted using django (either using form api or from django admin panel)

    def __str__(self):
        return self.username
            # this will make data labelled using username in table in django admin
        # dataLabel = self.username + ", " + self.email
        # return dataLabel


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username