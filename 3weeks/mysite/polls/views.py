from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
# from django.http import Http404


def index(request):
    
    # questioin에서 order by를 통해 5개를 가져와서 latest_question_list를 만든다
    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    
    # 5개의의 데이터 중 question_text 만 뽑아온다
    # output = ', '.join([q.question_text for q in latest_question_list])
    
    context = {'questions' :latest_question_list }
    
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try :
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except  (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message': "선택이 없습니다."})
    else :
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args = (question_id,)))
    


def result(request, question_id) :
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/result.html', {'question': question})