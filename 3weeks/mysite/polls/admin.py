from django.contrib import admin
from .models import Question,Choice
# or from .models import *


# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)