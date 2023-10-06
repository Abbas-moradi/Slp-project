from django.shortcuts import render, redirect
from django.views import View
from .forms import UserQuestionForm
from .models import UserQuastion


class RegisterQuestion(View):
    question_form = UserQuestionForm
    question_model = UserQuastion

    def get(self, request):
        pass

    def post(self, request):
        form = self.question_form(request.POST)

        if form.is_valid():
            clean_data = form.cleaned_data
            print(clean_data, '*'*50)
            question_instance = self.question_model.objects.create(issue=clean_data['issue'],
                                               child_name = clean_data['child_name'],
                                               child_age = clean_data['child_age'],
                                               description = clean_data['desc'],
                                               email = clean_data['email'],
                                               phone = clean_data['phone'])
            question_instance.save()
            return redirect('home:home')
        return redirect('home:home')
    
