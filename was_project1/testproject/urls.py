from django.urls import path
from testproject import views

app_name = 'testproject'

urlpatterns = [
    path('', views.index, name='index'),

]