from django.shortcuts import render
from django.views import View
from .models import Category, ImageGallery
import random


class Home(View):
    template_name = 'index.html'

    def get(self, request):
        category = Category.objects.filter(status=True)
        img = ImageGallery.objects.filter(status=True)
        random_images = random.sample(list(img), 6)
        return render(request, self.template_name, {'categories': category, 'image': random_images})
    
    def post(self, request):
        pass