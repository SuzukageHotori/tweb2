"""tweb2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .view import hello
from .view import home
from .view import tool


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
	#url(r'^hello', hello.hello),
	url(r'^tool/b64Encode', tool.b64Encode),
	url(r'^tool/b64Decode', tool.b64Decode),
	url(r'^tool/b64', tool.b64),

	url(r'^tool', tool.index),

	url(r'^index', home.index),

	url(r'', home.index),
]
