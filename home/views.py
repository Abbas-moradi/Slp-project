from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Category, ImageGallery, NewsUserEmail
from .forms import UserNewsEmailForm
from django.contrib import messages
import random


class Home(View):
    email_form = UserNewsEmailForm
    template_name = 'index.html'

    def get(self, request):
        category = Category.objects.filter(status=True)
        img = ImageGallery.objects.filter(status=True)
        random_images = random.sample(list(img), 6)
        return render(request, self.template_name, {'categories': category, 'image': random_images, 'email_form': self.email_form})
    
    def post(self, request):
        email_form = UserNewsEmailForm(request.POST)
        if email_form.is_valid():
            user_exists = NewsUserEmail.objects.filter(email=email_form.cleaned_data['email']).exists()
            if not user_exists:
                NewsUserEmail.objects.create(email=email_form.cleaned_data['email'])
                messages.success(request, 'ایمیل وارد شده ذخیره شد', 'success')
                return redirect('home:home')
            messages.error(request, 'ایمیل وارد شده تکراری است', 'danger')
        return redirect('home:home')
