from django.shortcuts import render
from django.http import HttpResponse
from testproject.models import Category, News

def index(request):
    news_list = News.objects.order_by('-date')[:5]
    category_list = Category.objects.all()

    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['news'] = news_list

    return render(request, 'testproject/index.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        news = News.objects.filter(category=category)
        context_dict['news'] = news
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['news'] = None
    return render(request, 'testproject/category.html', context=context_dict)

# Create your views here.
