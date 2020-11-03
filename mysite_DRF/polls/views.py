from django.http import HttpResponse
from django.http import Http404
from .models import Question, Choice

from rest_framework import generics
from .serializers import QuestionSerializer, ChoiceSerializer
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    question_list = Question.objects.all()
    return HttpResponse('http://127.0.0.1:8000' + reverse('list'))


def index_other(request):
    return HttpResponse("Hello, OTHER world. You're at the polls index.")


class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):        
        return Choice.objects.filter(question_id=self.kwargs.get('question_id'))


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer

    def get_object(self):
        return get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = QuestionSerializer

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))
