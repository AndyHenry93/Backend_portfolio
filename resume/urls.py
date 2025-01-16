from django.urls import path
from . import views

urlpatterns = [
    # path('beta/',views.index, name='index'),
    # path('detail/<int:pk>/', views.detail, name='detail'),
    path('', views.home, name='home'),
]
