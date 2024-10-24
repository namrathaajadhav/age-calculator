"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from agecalculator import views  # Import views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home view
    path('about/', views.about, name='about'),  # About view
    path('services/', views.services, name='services'),  # Services view
    path('contact/', views.contact, name='contact'),  # Contact view
    path('age-calculator/', views.age_calculator, name='age_calculator'),  # Age calculator view
    path('agecalculator/', include('agecalculator.urls')),  # Include agecalculator URLs
]
