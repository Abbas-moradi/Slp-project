from django.shortcuts import render, redirect
from django.views import View
from core.forms import UserQuestionForm
from core.models import UserQuastion


class RegisterQuestion(View):
    question_form = UserQuestionForm
    question_model = UserQuastion

    def get(self, request):
        pass

    def post(self, request):
        form = self.question_form(request.POST)
        print(request.POST['desc'])

        if form.is_valid():
            question_instance = self.question_model.objects.create(issue=request.POST['issue'],
                                                child_name = request.POST['child_name'],
                                                child_age = request.POST['child_age'],
                                                description = request.POST['desc'],
                                                email = request.POST['email'],
                                                phone = request.POST['phone'])
            question_instance.save()
            return redirect('home:home')
        return redirect('home:home')
    
