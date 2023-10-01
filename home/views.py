from django.shortcuts import render
from django.views import View
from .models import Category


class Home(View):
    template_name = 'index.html'

    def get(self, request):
        category = Category.objects.filter(status=True)
        return render(request, self.template_name, {'categories': category})
    
    def post(self, request):
        pass