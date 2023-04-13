from . import views
from django.urls import path
from .views import  application_form, success_view
app_name='storeapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', application_form, name='new'),
    path('success/', success_view, name='success'),
    path('saved/', views.saved_forms, name='saved'),

]

