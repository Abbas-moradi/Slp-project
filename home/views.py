from django.shortcuts import render
from django.views import View
from .models import Category, ImageGallery


class Home(View):
    template_name = 'index.html'

    def get(self, request):
        category = Category.objects.filter(status=True)
        img = ImageGallery.objects.filter(status=True)
        return render(request, self.template_name, {'categories': category, 'image': img})
    
    def post(self, request):
        pass