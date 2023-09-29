from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterationForm, VerifyCodeForm
from utils import send_otp_code
from django.contrib import messages
import random
from .models import OtpCodeRegister, User


class UserRegisterView(View):
    form_class = UserRegisterationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid:
            random_code = random.randint(10000, 99999)
            send_otp_code(self.cleaned_data['phone'], random_code)
            OtpCodeRegister.objects.create(phone=self.cleaned_data['phone'], code=random_code)
            request.session['user_register_info'] = {
                'phone_number': self.cleaned_data['phone'],
            }
            return redirect('accounts:verify_code')
        return render(request,'accounts/register.html', {'form':form})


class UserRegisterVerifyCode(View):
    form_class = VerifyCodeForm
    template_name = 'accounts/verify_code.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_session = request.session['user_register_info']
        code_instance = OtpCodeRegister.objects.get(phone=user_session['phone'])
        form = self.form_class(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            if clean_data['code'] == code_instance.code:
                User.objects.create(phone=user_session['phone'], email=f'{user_session["phone"]}@email.com',
                                     full_name='Anonymous', password=user_session['phone'])
                code_instance.delete()
                return redirect('home:home')
            else:
                messages.error(request, 'کد وارد شده اشتباه است', 'danger')
                return redirect(self.template_name)
        return redirect('home:home')


