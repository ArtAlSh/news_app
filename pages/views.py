from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    user = User
    context_object_name = 'con_ob'
