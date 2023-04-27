from polls.models import Question
from polls_api.serializers import *
from django.contrib.auth.models import User
from .permissions import *
# from django.contrib.auth.models import User

from rest_framework import generics,permissions
# from polls_api.serializers import UserSerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
    
class RegisterUser(generics.ListCreateAPIView):
    queryset= User.objects.all()
    
    serializer_class = RegisterSerializier 