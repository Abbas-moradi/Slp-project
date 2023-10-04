from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterationForm, VerifyCodeForm
from utils import send_otp_code
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .tasks import email_sender
import random
from .models import OtpCodeRegister, User


class UserRegisterView(View):
    form_class = UserRegisterationForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(10000, 99999)
            
            print(random_code)
           
            send_otp_code(form.cleaned_data['phone'], random_code)
            email_sender(random_code, form.cleaned_data['email'])
            OtpCodeRegister.objects.create(phone=form.cleaned_data['phone'], code=random_code)
            request.session['user_register_info'] = {
                'phone_number': form.cleaned_data['phone'],
            }
            return redirect('accounts:verify_code')
        return render(request,'register.html', {'form':form})


class UserRegisterVerifyCode(View):
    form_class = VerifyCodeForm
    template_name = 'verify_code.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_session = request.session['user_register_info']
        code_instance = OtpCodeRegister.objects.get(phone=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            if clean_data['code'] == code_instance.code:
                User.objects.create(phone=user_session['phone_number'], email=f'{user_session["phone_number"]}@email.com',
                                     full_name='Anonymous', password=user_session['phone_number'])
                code_instance.delete()
                return redirect('home:home')
            else:
                messages.error(request, 'کد وارد شده اشتباه است', 'danger')
                return redirect(self.template_name)
        return redirect('home:home')


