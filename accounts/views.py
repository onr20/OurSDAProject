from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView , PasswordChangeView
from django.urls import reverse_lazy
from .forms import MySignUpForm


class MyLoginView(LoginView):
    template_name = 'accounts/login.html'


class MyPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/login.html'
  success_url = reverse_lazy('movies')


class MySignUpView(CreateView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('movies')
    form_class = MySignUpForm