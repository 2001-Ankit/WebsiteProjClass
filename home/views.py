from django.shortcuts import render
from .views import *
from django.views.generic import View
# Create your views here.

class BaseView(View):
    context = {}



class HomeView(BaseView):

    def get(self,request):
        self.context['categories'] = Cate
