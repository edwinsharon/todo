from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:pk>/',views.delete_g,name='delete_g'),
    path('edit/<int:pk>/',views.edit_g,name='edit_g'),
]