from django.shortcuts import render
from django.views import View
from .forms import UserRegisterationForm


class UserRegisterView(View):
    form_class = UserRegisterationForm

    def get(self, request):
        pass

    def post(self, request):
        pass
