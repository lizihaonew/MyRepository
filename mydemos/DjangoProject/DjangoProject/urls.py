"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to allviews. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function allviews
    1. Add an import:  from my_app import allviews
    2. Add a URL to urlpatterns:  path('', allviews.home, name='home')
Class-based allviews
    1. Add an import:  from other_app.allviews import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jmeter/', include(('JmeterPlatform.urls', 'JmeterPlatform'), namespace='jmeter')),
    path('stress/', include('stressrunner.urls')),
    path('js/', include('stress_agent.urls')),
    path('xmind/', include('xmind_testcase.urls')),

]
