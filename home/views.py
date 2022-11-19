from django.shortcuts import render
from .views import *
from .models import *
from django.views.generic import View
# Create your views here.

class BaseView(View):
    context = {}



class HomeView(BaseView):

    def get(self,request):
        self.context['categories'] = Category.objects.all()
        self.context['subcategories'] = SubCategory.objects.all()
        self.context['sliders'] = Slider.objects.all()
        self.context['brands'] = Brand.objects.all()
        self.context['ads'] = Ad.objects.all()
        self.context['news'] = Product.objects.filter(labels='new')
        self.context['hots'] = Product.objects.filter(labels ='hot')
        self.context['reviews'] =Reviews.objects.all()

        return render(request,'index.html',self.context)


class Categories(BaseView):
    def get(self,request,slug):
        ids = Category.objects.get(slug = slug).id
        self.context['category_product'] = Product.objects.filter(category_id = ids)
        return render(request,'category.html',self.context)