from django.shortcuts import render
from django.views import View
from .forms import UserRegisterationForm


class UserRegisterView(View):
    form_class = UserRegisterationForm


