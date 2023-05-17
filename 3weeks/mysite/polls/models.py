from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name = '질문')
    pub_data = models.DateTimeField(auto_now_add = True, verbose_name='생성일')

    
class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return f'[{self.question.question_text}] {self.choice_text}'
    
    
class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete = models.CASCADE)
    voter = models.ForeignKey(User, on_delete = models.CASCADE)
    
    class Meta :
        constraints = [
            models.UniqueConstraint(fields = ['question','voter'], name = 'unique_voter_for_questions')
        ]
    