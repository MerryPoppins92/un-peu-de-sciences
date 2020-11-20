"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from generator import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('generatedpassword/', views.password, name='password'), 
    path('passwordpage/', views.about, name='passwordpage'),

    # path('createpassword/', views.createpassword, name='createpassword'), 
    path('prime/', views.prime, name='prime'),
    path('primepage/', views.primepage, name='primepage'),

    path('fibo/', views.fibo, name='fibo'),
    path('fibopage/', views.fibopage, name='fibopage'),

    path('romain/', views.romain, name='romain'),
    path('romainpage/', views.romainpage, name='romainpage'),

    path('factor/', views.factor, name='factor'),
    path('factorpage/', views.factorpage, name='factorpage'),

    path('base16/', views.base16, name='base16'),
    path('base16page/', views.base16page, name='base16page'),

    path('base2/', views.base2, name='base2'),
    path('base2page/', views.base2page, name='base2page'),

    path('seconddegre/', views.seconddegre, name='seconddegre'),
    path('seconddegrepage/', views.seconddegrepage, name='seconddegrepage'),

    path('cesaer/', views.cesaer, name='cesaer'),
    path('cesaerpage/', views.cesaerpage, name='cesaerpage'),

    path('sysdeq/', views.sysdeq, name='sysdeq'),
    path('sysdeqpage/', views.sysdeqpage, name='sysdeqpage'),

    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)