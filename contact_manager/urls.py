"""
URL configuration for contact_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from contacts.views import contact_list, contact_create, contact_update, contact_delete , landing


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing , name='landing_page'),
    path('list/', contact_list, name='contact_list'),
    path('create/', contact_create, name='contact_create'),
    path('update/<int:pk>/', contact_update, name='contact_update'),
    path('delete/<int:pk>/', contact_delete, name='contact_delete'),
]