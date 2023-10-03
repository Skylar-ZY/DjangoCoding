import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from mydemo.models import Quiz
from mydemo.models import Question
from mydemo.models import Choice

# Create your views here.
#index page
def index(request):
    return render(request, "page/index.html")
    
#quiz page    
def quiz(request): 
    question_list = Choice.objects.all()
    option_list = Choice.objects.all()
  
    # Convert QuerySet to list of dictionaries
    questions = {"question_list": list(question_list.values()),
                 "option_list": list(option_list.values())}   
    return JsonResponse(questions, safe=False)
    
#evaluation page 
def evaluation(request):
    if (request.method == "POST"):
        answers = []
        request_data = json.loads(request.body)
        answer_list = request_data["question_list"]
       
        for i in range(0, len(answer_list)):
            if (answer_list[i]["is_multiple_choice"]):
                answer = Choice.objects.filter(question_id = answer_list[i]["question_id"], is_correct=True)

            else:
                answer = Choice.objects.filter(id = answer_list[i]["choice_id"])
            
            answer = list(answer.values())
            answers.append(answer)
            
        return JsonResponse({"answers": answers}, safe=False)
    else:
        return render(request, "page/index.html")


    
    
