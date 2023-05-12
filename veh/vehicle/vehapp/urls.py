from . import views
from django.urls import path
app_name='vehapp'
urlpatterns = [
    path('',views.Vehicle_list,name='vehicle_list'),
    path('login/',views.login, name='login'),
    path('registration/',views.registration, name='register'),
    path('logout/',views.logout_view, name='logout'),
    path('read_update_delete/<int:id>/', views.Vehicle_RUD, name='read_update'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
    path('create/', views.Vehicle_Create, name='create')
]
