from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name = '질문')
    pub_data = models.DateTimeField(auto_now_add = True, verbose_name='생성일')
    # score = models.FloatField(default = 0)
    # is_something_wrong = models.BooleanField(default = False)
    # json_field = models.JSONField(default=dict)
    
    @admin.display(boolean=True, description='최근생성(하루기준)')
    def was_published_recently(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        if self.was_published_recently :
            new_badge = 'NEW!!!'
        else :
            new_badge = ''
        return f'{new_badge}제목 : {self.question_text}, 날짜: {self.pub_data}'
    
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    
    def __str__(self):
        return f'[{self.question.question_text}] {self.choice_text}'