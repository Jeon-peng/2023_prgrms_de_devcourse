from polls.models import Question
from polls_api.serializers import QuestionSerializer, UserSerializer
from django.contrib.auth.models import User
# from django.contrib.auth.models import User

from rest_framework import generics
# from polls_api.serializers import UserSerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
    
