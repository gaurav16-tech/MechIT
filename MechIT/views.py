from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'base.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class UserPage(TemplateView):
    template_name = 'user.html'
