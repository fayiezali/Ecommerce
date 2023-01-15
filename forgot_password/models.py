from django.db import models

from django.contrib.auth.models import User

class QuestionMODEL(models.Model):
    question = models.CharField(max_length=60,null=True)

    def __str__(self):
        return self.question

class UserQuestionMODEL(models.Model):
    question = models.ForeignKey(QuestionMODEL,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)

class ProfileMODEL(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
        
        

class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    def __str__(self):
        return str(self.Mobile)