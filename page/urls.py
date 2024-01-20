from django.urls import path
from .views import MyClass,MyAboutView

urlpatterns = [
    path('', MyClass.as_view(),name='home'),
    path('about/',MyAboutView.as_view(), name='about' )
]