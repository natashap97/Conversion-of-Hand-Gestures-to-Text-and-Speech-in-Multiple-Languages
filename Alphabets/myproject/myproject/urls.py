"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path,include
from homepage.views import button,output,test,upload_img,dynamic,speech,preprocess
urlpatterns = [
	path('',button,name='home'),
    path('output', output, name='script'),
    path('upload/',upload_img,name="upload_img"),
    path('upload/recognize/',test,name="test"),
    path('dynamic/',dynamic,name="script"),
    path('preprocess/',preprocess,name="preprocess"),
    path('upload/recognize/speech/',speech,name="speech"),
    path('admin/', admin.site.urls),
    ]
