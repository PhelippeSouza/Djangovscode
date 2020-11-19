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
from Verao import viewsverao
from outono import viewsoutono
from inverno import viewsinverno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('Primavera/', include('Primavera.urls')),
    path('outono/', include('outono.urls')),

    path('', include('Verao.urls')),
    path('', include('blogloh.urls')),
    path('verãohome.html', viewsverao.Verãohome_View, name = 'Verão'),
    path('primaverahome.html', views.BlogCreateView.as_view(), name = 'Nova Postagem'),
    path('post_edit.html', views.BlogUpdateView.as_view(),name='post_edit'),
    path('primaverahome.html', viewsprimavera.NovaPrimavera_View, name = 'Primavehome'),
    path('devocionais.html', views.Devocional_View, name = 'Devocional'),
    path('primavera_new.html', viewsprimavera.Primavera_View, name = 'Primavera_new'),
    path('verãoview.html', viewsverao.BlogCreateView.as_view(), name = 'Nova Postagem'),
    path('veraodetail.html', viewsverao.BlogDetailView,name='verão_detail'),
    path('primaveradetail.html', viewsprimavera.BlogDetailView,name='verão_detail'),
    path('outonohome.html', viewsoutono.OutonoView,name='outonohome'),
    # path('outononew.html', viewsoutono.Novooutono_View,name='outonohome'),
    path('invernohome.html', viewsinverno.Invernohome_View,name='invernonohome'),
    # path('invernonew.html', viewsinverno.Inverno_View,name='invernoview'),
    #path('invernonew.html', viewsinverno.Inverno_New,name='invernoview'),
    path('invernodetail.html', viewsinverno.Inverno_New,name='invernoview'),
    path('invernonew.html', viewsinverno.BlogCreateView.as_view(), name = 'Nova Postagem'),
    path('outonoview.html', viewsoutono.BlogCreateView.as_view(), name = 'Nova Postagem'),





]

# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
