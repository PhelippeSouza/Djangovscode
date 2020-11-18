"""lola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include,path
from blogloh import views
from Primavera import viewsprimavera


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('Primavera/', include('Primavera.urls')),
   # path('contact/',include('contact.urls')),
    path('', include('blogloh.urls')),
    # path('primavera.html', views.Primavera_View, name = 'Primavera'),
    path('verão.html', views.Verão_View, name = 'Verão'),
    path('outono.html', views.Outono_View, name = 'Outono'),
    path('inverno.html', views.Inverno_View, name = 'Inverno'),
    path('post_new.html', views.BlogCreateView.as_view(), name = 'Nova Postagem'),
    path('post_edit.html', views.BlogUpdateView.as_view(),name='post_edit'),
    path('post_detail.html', views.Detail_View,name='Detail'),
    path('primaverahome.html', views.Primavera_View, name = 'PrimaveraHome'),
    path('devocionais.html', views.Devocional_View, name = 'Devocional'),
    path('primavera_new.html', views.NovaPrimavera_View, name = 'Nova Primavera'),
    
]

# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
